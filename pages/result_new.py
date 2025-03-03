#result.pyと同じ内容なのでresult.pyを使用

import streamlit as st

# サンプルデータ
total_questions = 10
correct_answers = 7

# 正答率計算
accuracy = (correct_answers / total_questions) * 100

# リザルト画面
st.title("🎉 リザルト画面 🎉")

st.markdown(f"### ✅ 正解数: {correct_answers} / {total_questions}")
st.markdown(f"### 📊 正答率: {accuracy:.2f}%")

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

# 再挑戦ボタン
if st.button("🔄 もう一度挑戦"):
    st.experimental_rerun()

# ホーム画面に戻るボタン
if st.button("🏠 ホームに戻る"):
    st.write("ホーム画面に戻ります...")  # ホーム画面への遷移処理を追加予定

#2025/02/21 いい感じなのでは？
