#仮のタイトルページ: 実際には作ってくれたメインページに置き換える
import streamlit as st
import config

def main():
    st.title('内定者クイズ!!')
    st.warning("実際には作ってもらったメインページに置き換える")
    st.page_link("pages/quiz.py", label="クイズに挑戦する", icon="🧠")
if __name__ == "__main__":
    config.create_sidebar()
    main()
