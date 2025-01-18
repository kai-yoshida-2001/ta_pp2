### 第12週の復習 CSVファイルとJsonデータの操作の復習###

## [w12] 準備 ##

# w12.1 リポジトリのクローン
Terminalを開く（Terminalでの操作は$で示す．$の前はディレクトリを表す）
~$ rm -rf ~/ta_pp2
~$ cd; git clone github:kai-yoshida-2001/ta_pp2.git
~/ta_pp2$ git pull

# w12.2 演習用ファイルの表示
~$ tree ta_pp2/w12

# w12.3 README.mdの表示
~$ emacs -nw ta_pp2/w12/README.md

# w12.4 演習問題（easy）
~/ta_pp2/w12$ cd easy/
~/ta_pp2/w12/easy$ ls
~/ta_pp2/w12/easy$ ./command.sh

# w12.5 command.shの編集
上画面に移動
C-x o
ファイルを開く
C-x C-f ~/ta_pp2/w12/easy/command.sh

#!/bin/bash

source ~/venv/py3.10.12/bin/activate
python3 easy.py
#python3 answer.py

上記の形式に修正したら保存する
C-x C-s
C-x k RET

# w12.6 演習問題の確認
C-x C-f ~/ta_pp2/w12/easy/easy.py

問題一覧
Q1.データを読み取るためのオブジェクトを作成しよう
Q2.データを書き込むためのオブジェクトを作成しよう
Q3.1行ごとにデータを書き込もう
Q4.データを書き込むためのメソッドを呼び出そう
Q5.データの読み取るためのメソッドを呼び出そう
Q6.名前や数字を自分好みに変更して，データの中身が増えることを確認しよう

プログラムが書けたら，保存して，実行結果を確認しよう
C-x C-s
C-x o 
~/ta_pp2/w12/easy$ ./command.sh

出力結果が一致したらPythonファイルを閉じる
C-x o
C-x k RET

# w12.7 演習問題（normal）
C-x o
~/ta_pp2/w12/easy$ cd ../normal
~/ta_pp2/w12/normal$ ls
~/ta_pp2/w12/normal$ ./command.sh

# w12.8 CSVファイルの確認
C-x C-f ~/ta_pp2/w12/normal/input/city_and_code.csv

# w12.9 command.shの編集
C-x o
C-x C-f ~/ta_pp2/w12/normal/command.sh

#!/bin/bash

python3 normal.py
#python3 answer.py

上記の形式に修正したら保存する
C-x C-s
C-x k RET

# w12.10 演習問題の確認
C-x C-f ~/ta_pp2/w12/normal/normal.py

問題一覧
Q1.CSVファイルを保持した変数を指定しよう
Q2.データを読み取るためのオブジェクトを作成しよう
Q3.取得したデータを格納したリストを返そう
Q4.JSONファイルを保持した変数を指定しよう
Q5.データを書き込むためのメソッドを呼び出そう
Q6.新規作成したJSONファイルを返そう
Q7.データを読み取るためのメソッドを呼び出そう
Q8.input/city_and_code.csvに記録さている都市名に変更し，実行結果が変わることを確認しよう

プログラムが書けたら，保存して，実行結果を確認しよう
C-x C-s
C-x o 
~/ta_pp2/w12/normal$ ./command.sh

出力結果が一致したらPythonファイルを閉じる
C-x o
C-x k RET
