import streamlit as st
import config

def main():
    #このページが最初に表示された時のために初期化を定義しておく
    if "score" not in st.session_state:
        st.session_state.score = 0 # スコアの初期化
    if "total_questions" not in st.session_state: # 総問題数を数える変数
        st.session_state.total_questions = 0
    # サンプルデータ
    total_questions = 10
    correct_answers = 7
    
    # 正答率計算
    accuracy = (correct_answers / total_questions) * 100
    
    # リザルト画面
    st.title("🎉 リザルト画面 🎉")
    
    col1,col2 = st.columns(2)
    with col1:
        st.markdown(f"### ✅ 正解数: {st.session_state.score} / {st.session_state.total_questions}")
        #st.markdown(f"### ✅ 正解数: {correct_answers} / {total_questions}")
    with col2:
        #st.markdown(f"### 📊 正答率: {accuracy:.2f}%")
        if st.session_state.total_questions == 0: #quiz.pyとstateを共有しておく
            accuracy = 0
        else:
            accuracy = st.session_state.score/st.session_state.total_questions*100
        st.markdown(f"### 📊 正答率: {accuracy:.1f}%")
    
    # フィードバック表示
    if accuracy == 100:
        st.success("完璧！全問正解！🎊")
    elif accuracy >= 70:
        st.info("いい感じ！もう少しで満点！💪")
    elif accuracy >= 50:
        st.warning("もう少し頑張ろう！😅")
    else:
        st.error("次はもっと頑張ろう！💡")
    
    # 現在のユーザー順位を中央に表示（例として「あなたの順位: 2位」と表示）
    st.markdown("<h2 style='text-align: center;'>現在のあなたの順位: 2位</h2>", unsafe_allow_html=True)
    
    # トップ3ユーザーを表示
    st.markdown("<h3 style='text-align: center;'>トップ3ユーザー</h3>", unsafe_allow_html=True)
    
    # トップ3ユーザーの情報（ほんとはデータベース参照とかしたりして大変？？）
    top_users = [
        {"rank": 1, "name": "ユーザーA", "points": 1500},
        {"rank": 2, "name": "ユーザーB", "points": 1400},
        {"rank": 3, "name": "ユーザーC", "points": 1300}
    ]
    
    # 各ユーザー情報を中央揃えで表示
    for user in top_users:
        st.markdown(
            f"<p style='text-align: center;'>{user['rank']}位: {user['name']} - {user['points']}ポイント</p>", 
            unsafe_allow_html=True
        )
    col1,col2 = st.columns(2)
    with col1:
        # 再挑戦ボタン
        #if st.button("🔄 もう一度挑戦"):
        #    st.experimental_rerun()
        st.page_link("pages/quiz.py", label="もう一度挑戦する", icon="🔄")
    with col2:
        # ホーム画面に戻るボタン
        #if st.button("🏠 ホームに戻る"):
        #    st.write("ホーム画面に戻ります...")  # ホーム画面への遷移処理を追加予定
        st.page_link("main_temp.py", label="ホームに戻る", icon="🏠")
    
    #2025/02/21 いい感じなのでは？
    #2025/02/27 いい感じやな

if __name__ == "__main__":
    config.create_sidebar()
    main()
