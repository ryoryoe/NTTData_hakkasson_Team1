# NTTData_hakkasson_Team1

#コードについて
main_temp.py: メインのページの代替コード
quiz.py: クイズの画面を表示するコード
result.py: クイズの正答率などを表示するコード


#ディレクトリについて
static : 画像を保存するディレクトリ。streamlitではstaticディレクトリに入っている画像を./app/staticの形で参照することができる
pages: mainページ以外のページをこのディレクトリに入れておく。各ページへのリンクを作るときは、st.page_link("main_temp.py", label="ホーム", icon="🏠")のように書く
