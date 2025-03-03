import gspread
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials
import streamlit as st

# Google Sheets APIへの認証
def authenticate_gspread():
    # サービスアカウントの認証情報を使ってAPIにアクセス
    creds = Credentials.from_service_account_file(
        'credentials.json',  # ここに認証情報のファイルを指定
        scopes=["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    )
    # トークンが無効な場合、再認証する
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
    
    # gspreadクライアントの作成
    client = gspread.authorize(creds)
    return client

# スプレッドシートにデータを追加する関数
def save_result_to_sheet(player_name, correct_answers, total_questions, accuracy):
    # Google Sheetsにアクセス
    client = authenticate_gspread()
    
    # スプレッドシートのIDとワークシートを指定
    spreadsheet_id = '1pD1AXXJqOFc6kD1pkTZutWHcP_65CkygDaOsNJt9ofI'  # スプレッドシートのIDを指定
    sheet = client.open_by_key(spreadsheet_id).worksheet('sheet1')  # 1番目のシートにアクセス
    
    # プレイヤーの結果を行として追加
    new_row = [player_name, correct_answers, total_questions, accuracy]
    sheet.append_row(new_row)

# サンプルデータ
total_questions = 10
correct_answers = 7
accuracy = (correct_answers / total_questions) * 100
player_name = "プレイヤーA"  # ここは実際のプレイヤー名を取得してください

# 結果をスプレッドシートに保存
save_result_to_sheet(player_name, correct_answers, total_questions, accuracy)

# ストリームリットで表示
st.title("🎉 リザルト画面 🎉")
st.markdown(f"### ✅ 正解数: {correct_answers} / {total_questions}")
st.markdown(f"### 📊 正答率: {accuracy:.2f}%")
