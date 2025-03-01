import streamlit as st
import random
import time
import pandas as pd
import config

# ページのアイコンやタイトルなどの設定
st.set_page_config(
    page_title="内定者クイズ",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

def load_quiz_data_from_csv(csv_path: str):
    df = pd.read_csv(csv_path, encoding="utf-8-sig") 
    quiz_data = []

    # DataFrameの各行を問題データに変換
    for index, row in df.iterrows():
        question_text = "次の特徴を持った人物は誰でしょう？ 「" +  row["内定者800人中、〇〇なのは私くらいだろう"] + "」" # 問題文
        answer_text = row["名前"]  # 正解はその行の名前

        # 他の行からランダムに3人分の名前を取得
        df_others = df.drop(index)  # 自分自身の行を除外
        others_sample = df_others.sample(n=3, random_state=None)  # 3人分のデータを抽出

        # 選択肢(正解 + ランダム3人)
        options = [answer_text] + others_sample["名前"].tolist()
        random.shuffle(options)  # 選択肢の順番をシャッフル

        # 選択肢に対応するヒントを取得
        hints = []
        for option_name in options:
            person_data = df[df["名前"] == option_name].iloc[0]  # 該当する人物のデータを取得
            hint_text = f"ハッシュタグ: {person_data['ハッシュタグ']}, 出身地: {person_data['出身地']}, 出身校: {person_data['出身校']}, MBTI: {person_data['MBTI']}, 誕生日: {person_data['誕生日']}"
            hints.append(hint_text)

        # 画像のプレースホルダ
        image_placeholder = ["", "", "", ""]

        quiz_data.append({
            "question": question_text,
            "options": options,
            "answer": answer_text,
            "image": image_placeholder,
            "hints": hints  # 各選択肢に対応するヒント
        })
    return quiz_data



def main(): #main関数を定義してこの中にページのコンテンツを書いておく
    # ダークテーマの各コンテンツのスタイル設定
    st.markdown(
        """
        <style>
            body {
                background: linear-gradient(90deg, #3A3A44, #28282F);
                color: #FFFFFF;
            }
            .block-container {
                padding: 2rem;
            }
            .stButton > button {
                background-color: #00FFB0 !important;
                color: black !important;
                border-radius: 10px;
                padding: 10px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.4);
            }
            .stRadio label {
                font-size: 1.2rem;
            }
            .score-container {
                background-color: rgba(0, 255, 176, 0.2);
                padding: 15px;
                border-radius: 12px;
                text-align: center;
                font-size: 1.8rem;
                font-weight: bold;
                margin: 20px 0;
                border: 2px solid #00FFB0;
                box-shadow: 0 4px 10px rgba(0, 255, 176, 0.4);
            }
            .timer {
                font-size: 1.2rem;
                font-weight: bold;
                color: #FFC107;
            }
            .correct {
                color: #00FFB0;
                font-weight: bold;
                font-size: 1.5rem;
            }
            .incorrect {
                color: #DC3545;
                font-weight: bold;
                font-size: 1.5rem;
            }
            .question-container {
                background-color: rgba(255, 255, 255, 0.1);
                padding: 15px;
                border-radius: 12px;
                text-align: center;
                font-size: 1.5rem;
                font-weight: bold;
                margin: 20px 0;
                border: 2px solid #FFFFFF;
                box-shadow: 0 4px 10px rgba(255, 255, 255, 0.2);
            }
            .options-container {
                display: flex;
                justify-content: space-around;
                gap: 10px;
            }
         .hint-card {
            background-color: rgba(255, 255, 255, 0.1);
            padding: 15px;
            border-radius: 10px;
            margin: 10px 0;
            border: 2px solid #FFFFFF;
            box-shadow: 0 4px 6px rgba(255, 255, 255, 0.2);
        }
        .hint-title {
            font-size: 1.3rem;
            font-weight: bold;
            color: #00FFB0;
        }
        .hint-text {
            font-size: 1.1rem;
            color: #DDDDDD;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    #CSVファイルからクイズデータを取得
    quiz_data = load_quiz_data_from_csv("team_data_dummy.csv")

    # セッションステートの初期化(streamlitではセッションステートを使って状態を保持できる)
    if "current_question" not in st.session_state:
        st.session_state.current_question = random.choice(quiz_data) # ランダムに問題を選択
        st.session_state.score = 0 # スコアの初期化
        st.session_state.elapsed_time = 0 # 経過時間の初期化
    
    if "start_time" not in st.session_state:
        st.session_state.start_time = time.time() # クイズ開始時の時間を保持
    
    if "check_answer" not in st.session_state:
        st.session_state.check_answer = False # 回答済みかどうかのフラグ
    
    if "true_or_false" not in st.session_state:
        st.session_state.true_or_false = None # 正解かどうかのフラグ
    if "total_questions" not in st.session_state: # 総問題数を数える変数
        st.session_state.total_questions = 0
    
    # タイトル
    st.markdown("""
        # 💡 内定者クイズ！！
    """)
    
    # 問題の表示
    st.markdown(f"""
        ## 問題: {st.session_state.current_question['question']}
    """)
    
    # 選択肢の表示(question_contentにHTMLタグを追加していく)
    question_content = """
        <div class='question-container'>
            <div class='options-container'>
    """
    for i in range(len(st.session_state.current_question['options'])):
        question_content += f"<div class='option-item'><p><strong>{st.session_state.current_question['options'][i]}</strong></p>"
        question_content += f"<img src='{st.session_state.current_question['image'][i]}'></div>"
    question_content += """
            </div>
        </div>
    """
    
    # 選択肢の表示
    st.markdown(question_content, unsafe_allow_html=True)
    
    # ヒントを表示するボタン
    if st.button("🔍 ヒントを表示"):
        st.markdown("### 📝 ヒント一覧")
        # 2カラム（2列×2段）で表示
        col1, col2 = st.columns(2)
        
        for i, option in enumerate(st.session_state.current_question["options"]):
            hint_text = st.session_state.current_question['hints'][i]

            # ヒントの各要素を分解
            hint_parts = hint_text.split(", ")  # カンマ区切りで分割

            # HTML形式でヒントカードを作成
            hint_html = f"""
            <div class="hint-card">
                <div class="hint-title">{option}</div>
                <div class="hint-info">📌 {hint_parts[0]}</div>
                <div class="hint-info">📍 {hint_parts[1]}</div>
                <div class="hint-info">🏫 {hint_parts[2]}</div>
                <div class="hint-info">🧠 {hint_parts[3]}</div>
                <div class="hint-info">🎂 {hint_parts[4]}</div>
            </div>
            """

            # 2列に分けて表示
            if i % 2 == 0:
                with col1:
                    st.markdown(hint_html, unsafe_allow_html=True)
            else:
                with col2:
                    st.markdown(hint_html, unsafe_allow_html=True)

    # 回答を選択する
    col1,col2 = st.columns(2)
    with col1:
        selected_option = st.radio("選択肢を選んでください", st.session_state.current_question["options"], index=None)
        # 回答ボタン
        if st.button("✅ 回答する",disabled=st.session_state.check_answer):
            if selected_option:
                if selected_option == st.session_state.current_question["answer"]: #正解の場合
                    st.session_state.true_or_false = True
                    st.session_state.score += 1 # スコアを加算
                else: #不正解の場合
                    st.session_state.true_or_false = False 
               
                elapsed_time = int(time.time() - st.session_state.start_time) # 経過時間を計算
                st.session_state.check_answer = True
                st.session_state.total_questions += 1
                st.rerun()
            else:
                st.warning("選択肢を選んでください！") # 選択肢が選ばれていない場合のエラーメッセージ
    
        if st.session_state.true_or_false: # 正解か不正解かを表示
            st.markdown("<div class='correct'>✅ 正解！</div>", unsafe_allow_html=True)
        elif st.session_state.true_or_false == False:
            st.markdown(f"<div class='incorrect'>❌ 残念！正解は{st.session_state.current_question['answer']}でした！</div>", unsafe_allow_html=True)
    
    # 回答済みになったら次の問題へ進むボタンを表示
    if st.session_state.check_answer:
        with col2:
            st.markdown(f"<div class='score-container'>🏆 現在のスコア: {st.session_state.score}</div>", unsafe_allow_html=True) # スコアの表示
            cola,colb = st.columns(2)
            with cola:
                # 次の問題へ進むボタン
                if st.button("➡ 次の問題へ進む"): #各項目を初期化して次の問題へ
                    # 次の問題をセット
                    st.session_state.current_question = random.choice(quiz_data)
                    st.session_state.check_answer = False
                    st.session_state.true_or_false = None
                    st.session_state.start_time = time.time()
                    st.rerun()
                st.page_link("pages/result.py", label="結果を確認する", icon="📊")
            with colb:
                time_elapsed = int(time.time() - st.session_state.start_time)
                st.markdown(f"<div class='timer'>⏳ 経過時間: {time_elapsed}秒</div>", unsafe_allow_html=True) # 経過時間の表示

if __name__ == "__main__":
    config.create_sidebar()
    main()
