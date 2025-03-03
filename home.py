import streamlit as st
import config
import pandas as pd
import os
from datetime import datetime

# プレイヤー名を保存するファイルのパス
PLAYER_FILE = "players.csv"

def save_player_name(name):
    """プレイヤー名をCSVファイルに保存（重複防止）"""
    if not name.strip():
        return  # 空の名前は無視

    # CSVファイルが存在しない場合は新規作成
    if not os.path.exists(PLAYER_FILE):
        df = pd.DataFrame(columns=["名前", "登録日時"])
        df.to_csv(PLAYER_FILE, index=False, encoding="utf-8")

    # 既存データを読み込み
    df = pd.read_csv(PLAYER_FILE, encoding="utf-8")

    # すでに登録されているかチェック
    if name in df["名前"].values:
        return  # すでに登録されている場合は何もしない

    # 新しいプレイヤーを追加
    new_entry = pd.DataFrame({"名前": [name], "登録日時": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]})
    df = pd.concat([df, new_entry], ignore_index=True)

    # CSVファイルに保存
    df.to_csv(PLAYER_FILE, index=False, encoding="utf-8")

def main():
    st.markdown("<h1 style='text-align: center;'>サイトのタイトル</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>現在のあなたの順位: 2位</h2>", unsafe_allow_html=True)

    # トップ3ユーザーの表示
    st.markdown("<h3 style='text-align: center;'>トップ3ユーザー</h3>", unsafe_allow_html=True)
    top_users = [
        {"rank": 1, "name": "ユーザーA", "points": 1500},
        {"rank": 2, "name": "ユーザーB", "points": 1400},
        {"rank": 3, "name": "ユーザーC", "points": 1300}
    ]

    for user in top_users:
        st.markdown(
            f"<p style='text-align: center;'>{user['rank']}位: {user['name']} - {user['points']}ポイント</p>",
            unsafe_allow_html=True
        )

    st.divider()

    # **プレイヤー名の入力**
    st.markdown("<h3 style='text-align: center;'>プレイヤー名を入力してください</h3>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col2:
        player_name = st.text_input("プレイヤー名", placeholder="あなたの名前を入力")
        if st.button("登録"):
            save_player_name(player_name)
            st.success(f"プレイヤー名「{player_name}」を登録しました！")

    st.divider()

    # **クイズ挑戦ボタン**
    col1, col2, col3 = st.columns(3)
    with col2:
        st.page_link("pages/quiz.py", label="クイズに挑戦する", icon="🧠")

if __name__ == "__main__":
    config.create_sidebar()
    main()
