import streamlit as st

# タイトルを中央上部に配置
st.markdown("<h1 style='text-align: center;'>サイトのタイトル</h1>", unsafe_allow_html=True)

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

# 「はじめる」ボタンを中央に配置するために、列レイアウトを利用
col1, col2, col3 = st.columns(3)
with col2:
    if st.button("はじめる"):
        st.write("はじめ！")
