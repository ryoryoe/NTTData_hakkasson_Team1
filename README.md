# NTTData_hakkasson_Team1

#コードについて
main_temp.py: メインのページの代替コード(削除済み)
home.py: メインページのコード
quiz.py: クイズの画面を表示するコード
result.py: クイズの正答率などを表示するコード
config.py: サイドバーなど共通で使うモジュールを定義。import するだけで使い回せるようになる

#ディレクトリについて
static : 画像を保存するディレクトリ。streamlitではstaticディレクトリに入っている画像を./app/staticの形で参照することができる
pages: mainページ以外のページをこのディレクトリに入れておく。各ページへのリンクを作るときは、st.page_link("main_temp.py", label="ホーム", icon="🏠")のように書く
