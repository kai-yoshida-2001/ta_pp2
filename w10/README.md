### 第10週の復習 Google Sheetsの操作の復習###

## [w10] 準備 ##

# w10.1 リポジトリのクローン
Terminalを開く（Terminalでの操作は$で示す．$の前はディレクトリを表す）
~$ rm -rf ~/ta_pp2
~$ cd; git clone github:kai-yoshida-2001/ta_pp2.git
~/ta_pp2$ git pull

# w10.2 演習用ファイルの表示
~$ tree ta_pp2/w10

# w10.3 README.mdの表示
~$ emacs -nw ta_pp2/w10/README.md

# w10.4 command.shの実行
~/ta_pp2/w10$ ./command.sh
~/ta_pp2/w10$ ls
'output'ディレクトリを確認後に下記コマンドを実行
~/ta_pp2/w10$ ls output
	client_secret_~.json
	ssid.bak
	ssid.dat
	ssid.dir
	token_drive.pickle
	token_sheets.pickle
上記内容のファイルを確認できたら
easyへ進む

# w10.5 演習問題（easy）
~/ta_pp2/w10$ cd easy/
~/ta_pp2/w10/easy$ ls
~/ta_pp2/w10/easy$ ./command.sh

# w10.6 command.shの編集
上画面に移動
C-x o
ファイルを開く
C-x C-f ~/ta_pp2/w10/easy/command.sh

#!/bin/bash

source ~/venv/py3.10.12/bin/activate
python3 easy.py
#python3 answer.py

上記の形式に修正したら保存する
C-x C-s
C-x k RET

# w10.7 演習問題の確認
C-x C-f ~/ta_pp2/w10/easy/easy.py

問題一覧
Q1.スプレッドシートを新規作成しよう
Q2.'title'に'spreadsheet_name'を設定しよう
Q3.'spreadsheet'の'id'を取得して出力しよう
Q4.最初のシートを指定しよう
Q5.各行にデータを書き込もう（更新しよう）


プログラムが書けたら，保存して，実行結果を確認しよう
C-x C-s
C-x o 
~/ta_pp2/w10/easy$ ./command.sh

出力結果が一致したらPythonファイルを閉じる
C-x o
C-x k RET

# w10.8 演習問題（hard）
C-x o
~/ta_pp2/w10/easy$ cd ../hard
~/ta_pp2/w10/hard$ ls
~/ta_pp2/w10/hard$ ./command.sh

# w10.9 command.shの編集
C-x o
C-x C-f ~/ta_pp2/w10/hard/command.sh

#!/bin/bash

python3 hard.py
#python3 answer.py

上記の形式に修正したら保存する
C-x C-s
C-x k RET

# w10.10 演習問題の確認
C-x C-f ~/ta_pp2/w10/hard/hard.py

問題一覧
Q1.既存のスプレッドシートを読み込もう
Q2.'Excel'拡張子でダウンロードしよう
Q3. 自分のDriveに'upload'しよう
Q4.'title'と'id'を取得しよう
Q5.シートを新規作成しよう
Q6~Q8.行にデータを書き込もう


プログラムが書けたら，保存して，実行結果を確認しよう
C-x C-s
C-x o 
~/ta_pp2/w10/hard$ ./command.sh

出力結果が一致したらPythonファイルを閉じる
C-x o
C-x k RET
