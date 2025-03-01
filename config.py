#各ページで共通して使うサイドバーなどを定義
import streamlit as st

def create_sidebar():
    with st.sidebar:
         st.page_link("home.py", label="ホーム", icon="🏠")
         st.page_link("pages/quiz.py", label="クイズに挑戦する", icon="🧠")
         st.page_link("pages/result.py", label="結果を確認する", icon="📊")
         
