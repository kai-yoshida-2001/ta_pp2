### 第5週の復習 デバックの復習###

## [w05] 準備 ##

# w05.1 リポジトリのクローン
Terminalを開く（Terminalでの操作は$で示す．$の前はディレクトリを表す）
~$ rm -rf ~/ta_pp2
~$ cd; git clone github:kai-yoshida-2001/ta_pp2.git
~/ta_pp2$ git pull

# w05.2 演習用ファイルの表示
~$ tree ta_pp2/w05

# w05.3 README.mdの表示
~$ emacs -nw ta_pp2/w05/README.md

# w05.4 演習問題（easy）
~/ta_pp2/w05$ cd easy/
~/ta_pp2/w05/easy$ ls
~/ta_pp2/w05/easy$ ./command.sh

# w05.5 command.shの編集
上画面に移動
C-x o
ファイルを開く
C-x C-f ~/ta_pp2/w05/easy/command.sh

#!/bin/bash

source ~/venv/py3.10.12/bin/activate
python3 easy.py
#python3 easy_answer.py

上記の形式に修正したら保存する
C-x C-s
C-x k RET

# w05.6 演習問題の確認
C-x C-f ~/ta_pp2/w05/easy/easy.py

問題一覧
Q1. プログラムの開始をログに記録しよう
Q2. 正の整数以外が入力された場合の例外処理を記述しよう
Q3. assert文を使い，aとbが正の数でない場合に発生するエラーを設定しよう
Q4. raise文を使い，aとbが正の数でない場合に発生するエラーを設定しよう
Q5. 全ての処理が終わったことを記録しよう

プログラムが書けたら，保存して，実行結果を確認しよう
C-x C-s
C-x o 
~/ta_pp2/w05/easy$ ./command.sh

出力結果が一致したらPythonファイルを閉じる
C-x o
C-x k RET

# w05.7 演習問題（normal）
C-x o
~/ta_pp2/w05/easy$ cd ../normal
~/ta_pp2/w05/normal$ ls
~/ta_pp2/w05/normal$ ./command.sh

# w05.8 command.shの編集
C-x o
C-x C-f ~/ta_pp2/w05/normal/command.sh

#!/bin/bash

source ~/venv/py3.10.12/bin/activate
python3 normal.py
#python3 normal_answer.py

上記の形式に修正したら保存する
C-x C-s
C-x k RET

# w05.9 演習問題の確認
C-x C-f ~/ta_pp2/w05/normal/normal.py

問題一覧
Q1. プログラムの開始をログに記録しよう
Q2. raise文を使い，valueが正の整数でない場合のエラーを設定しよう
Q3. 例外処理を実行する場合にエラーログを記録する設定しよう
Q4. 全工程が終了したことを記録しよう

プログラムが書けたら，保存して，実行結果を確認しよう
C-x C-s
C-x o 
~/ta_pp2/w05/normal$ ./command.sh

出力結果が一致したらPythonファイルを閉じる
C-x o
C-x k RET

# w05.10 演習問題（hard）
C-x o
~/ta_pp2/w05/normal$ cd ../hard
~/ta_pp2/w05/hard$ ls
~/ta_pp2/w05/hard$ ./command.sh

# w05.8 command.shの編集
C-x C-f ~/ta_pp2/w05/hard/command.sh

#!/bin/bash

source ~/venv/py3.10.12/bin/activate
python3 hard.py
#python3 hard_answer.py

上記の形式に修正したら保存する
C-x C-s
C-x k RET

# w05.9 演習問題の確認
C-x C-f ~/ta_pp2/w05/hard/hard.py

問題一覧
Q1. pyinputplusを使ってStr型で受け付けるように設定しよう
Q2. 正規表現を使って電話番号形式を設定しよう
Q3. 正しい形式で入力された場合のログを記録しよう
Q4. 例外処理でValueErrorを設定しよう

プログラムが書けたら，保存して，実行結果を確認しよう
C-x C-s
C-x o 
~/ta_pp2/w05/hard$ ./command.sh

出力結果が一致したらPythonファイルを閉じる
C-x o
C-x k RET
