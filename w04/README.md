### 第3週の復習 入力検証###

## [w03] 準備 ##

# w03.1 リポジトリのクローン
Terminalを開く（Terminalでの操作は$で示す．$の前はディレクトリを表す）
~$ rm -rf ~/ta_pp2
~$ cd; git clone github:kai-yoshida-2001/ta_pp2.git

# w03.2 演習用ファイルの表示
~$ tree ta_pp2/w03

# w03.3 README.mdの表示
~$ emacs -nw ta_pp2/w03/README.md

## [w03] pyinputplusモジュールの基本操作を理解しよう ##

# w03.4 演習問題（easy）
~/ta_pp2/w03$ cd easy/
~/ta_pp2/w03/easy$ ls
~/ta_pp2/w03/easy$ ./command.sh

# w03.5 command.shの編集
上画面に移動
C-x o
ファイルを開く
C-x C-f ~/ta_pp2/w03/easy/command.sh

#!/bin/bash

source ~/venv/py3.10.12/bin/activate
python3 easy.py
#python3 easy_answer.py

上記の形式に修正したら保存する
C-x C-s
C-x k RET

# w03.6 演習問題の確認
C-x C-f ~/ta_pp2/w03/easy/easy.py

問題一覧
Q1. 選択肢を'はい'か'いいえ'で設定しよう
Q2. 指名入力の制限時間を'5'秒に設定しよう
Q3. 5秒以上経過してしまった場合の処理を設定しよう
Q4. 数値入力を'整数'のみ受け付けるように設定しよう
Q5. 番号付きの選択肢を表示できるように設定しよう

プログラムが書けたら，保存して，実行結果を確認しよう
C-x C-s
C-x o 
~/ta_pp2/w03/easy$ ./command.sh

出力結果が一致したらPythonファイルを閉じる
C-x o
C-x k RET

# w03.7 演習問題（normal）
C-x o
~/ta_pp2/easy$ cd ../normal
~/ta_pp2/normal$ ls
~/ta_pp2/normal$ ./command.sh

# w03.8 command.shの編集
C-x o
C-x C-f ~/ta_pp2/w03/normal/command.sh

#!/bin/bash

source ~/venv/py3.10.12/bin/activate
python3 normal.py
#python3 normal_answer.py

上記の形式に修正したら保存する
C-x C-s
C-x k RET

# w03.9 演習問題の確認
C-x C-f ~/ta_pp2/w03/normal/normal.py

問題一覧
Q1. 番号付きのメニュー表記となるように設定しよう
Q2. 数値入力を整数のみで受け取り，最大値は3，最小値は0で設定しよう
Q3. yesかnoの入力を受け付けるオプションに設定しよう

プログラムが書けたら，保存して，実行結果を確認しよう
C-x C-s
C-x o 
~/ta_pp2/w03/normal$ ./command.sh

出力結果が一致したらPythonファイルを閉じる
C-x o
C-x k RET

# w03.10 演習問題（hard）
C-x o
~/ta_pp2/normal$ cd ../hard
~/ta_pp2/hard$ ls
~/ta_pp2/hard$ ./command.sh

# w03.8 command.shの編集
C-x C-f ~/ta_pp2/w03/hard/command.sh

#!/bin/bash

source ~/venv/py3.10.12/bin/activate
python3 hard.py
#python3 hard_answer.py

上記の形式に修正したら保存する
C-x C-s
C-x k RET

# w03.9 演習問題の確認
C-x C-f ~/ta_pp2/w03/hard/hard.py

問題一覧
Q1. inputフォルダにあるpdfファイルのパスを指定しよう
Q2. PDFファイルを読み込むためのオブジェクトを生成しよう
Q3. PDFファイルのページオブジェクトのリストを作成しよう
Q4. ページから取得したテキストを変数に追加しよう
Q5. 電話番号の正規表現を設定しよう（形式：XXX-XXXX-XXXX）
Q6. Q5で設定したパターンに合う形式を全て見つけよう
Q7. 番号付きのリスト表示となるように設定しよう

プログラムが書けたら，保存して，実行結果を確認しよう
C-x C-s
C-x o 
~/ta_pp2/w03/hard$ ./command.sh

出力結果が一致したらPythonファイルを閉じる
C-x o
C-x k RET
