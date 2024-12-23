### 第11週の復習 電子メールの操作の復習###

## [w10] 準備 ##

# w11.1 リポジトリのクローン
Terminalを開く（Terminalでの操作は$で示す．$の前はディレクトリを表す）
~$ rm -rf ~/ta_pp2
~$ cd; git clone github:kai-yoshida-2001/ta_pp2.git
~/ta_pp2$ git pull

# w11.2 演習用ファイルの表示
~$ tree ta_pp2/w11

# w11.3 README.mdの表示
~$ emacs -nw ta_pp2/w11/README.md

# w11.4 command.shの実行
~/ta_pp2/w11$ ./command.sh
~/ta_pp2/w11$ ls
'output'ディレクトリを確認後に下記コマンドを実行
~/ta_pp2/w11$ ls output
	client_secret_~.json
	ssid.bak
	ssid.dat
	ssid.dir
	token_drive.pickle
	token_sheets.pickle
	token.json
上記内容のファイルを確認できたら
easyへ進む

# w11.5 演習問題（easy）
~/ta_pp2/w11$ cd easy/
~/ta_pp2/w11/easy$ ls
~/ta_pp2/w11/easy$ ./command.sh

# w11.6 エラーを検出したら
google.auth.exceptions.RefreshError:
というエラーを検出した場合は，下記の手順を踏んでください
1.$ cd ~/pp2/w11/kp3
2.$ ./command.sh
3.$ cd ~/ta_pp2/w11
4.$ ./command.sh

以上の手順を踏むことで
token.jsonが更新され，エラーを解消できるはずです

# w11.7 command.shの編集
上画面に移動
C-x o
ファイルを開く
C-x C-f ~/ta_pp2/w11/easy/command.sh

#!/bin/bash

source ~/venv/py3.10.12/bin/activate
python3 easy.py
#python3 answer.py

上記の形式に修正したら保存する
C-x C-s
C-x k RET

# w11.8 演習問題の確認
C-x C-f ~/ta_pp2/w11/easy/easy.py

問題一覧
Q1.宛先を自分のメールアドレス（学籍番号）に設定しよう
Q2.送信メールに必要な変数を引数に与えよう
Q3.検索するためのメソッドを呼び出そう
Q4.検索対象に指定する情報を定義しよう
Q5.GmailThreadオブジェクトからmessages属性を取得しよう
Q6.件名と差出人名を取得しよう

プログラムが書けたら，保存して，実行結果を確認しよう
C-x C-s
C-x o 
~/ta_pp2/w11/easy$ ./command.sh

出力結果が一致したらPythonファイルを閉じる
C-x o
C-x k RET

# w11.9 演習問題（normal）
C-x o
~/ta_pp2/w11/easy$ cd ../normal
~/ta_pp2/w11/normal$ ls
~/ta_pp2/w11/normal$ ./command.sh

# w11.10 command.shの編集
C-x o
C-x C-f ~/ta_pp2/w11/normal/command.sh

#!/bin/bash

python3 normal.py
#python3 answer.py

上記の形式に修正したら保存する
C-x C-s
C-x k RET

# w11.11 演習問題の確認
C-x C-f ~/ta_pp2/w11/hard/hard.py

問題一覧
Q1.'query'を引数に与えることで，目的のメール情報だけを取得しよう
Q2.すべてのメールメッセージのリストを定義しよう
Q3.メールメッセージの送信者のメールアドレスを取得しよう
Q4.メールメッセージの件名を取得しよう
Q5.メールメッセージの件名を取得しよう
Q6.メールメッセージの送信者のメールアドレスを取得しよう
Q7.メールメッセージの件名を取得しよう

プログラムが書けたら，保存して，実行結果を確認しよう
C-x C-s
C-x o 
~/ta_pp2/w11/hard$ ./command.sh

出力結果が一致したらPythonファイルを閉じる
C-x o
C-x k RET
