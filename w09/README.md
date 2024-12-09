### 第9週の復習 Excelスプレッドシート操作の復習###

## [w09] 準備 ##

# w09.1 リポジトリのクローン
Terminalを開く（Terminalでの操作は$で示す．$の前はディレクトリを表す）
~$ rm -rf ~/ta_pp2
~$ cd; git clone github:kai-yoshida-2001/ta_pp2.git
~/ta_pp2$ git pull

# w09.2 演習用ファイルの表示
~$ tree ta_pp2/w09

# w09.3 README.mdの表示
~$ emacs -nw ta_pp2/w09/README.md

# w09.4 演習問題（easy）
~/ta_pp2/w09$ cd easy/
~/ta_pp2/w09/easy$ ls
~/ta_pp2/w09/easy$ ./command.sh

# w09.5 command.shの編集
上画面に移動
C-x o
ファイルを開く
C-x C-f ~/ta_pp2/w09/easy/command.sh

#!/bin/bash

./clean.sh
source ~/venv/py3.10.12/bin/activate
python3 easy.py
#python3 answer.py
libreoffice --nologo --writer ./output/easy_example.xlsx

上記の形式に修正したら保存する
C-x C-s
C-x k RET

# w09.6 演習問題の確認
C-x C-f ~/ta_pp2/w09/easy/easy.py

問題一覧
Q1.'load_workbook'メソッドを呼び出して，Excelファイルを読み込もう
Q2.'sheetnames'メソッドを呼び出して，'workbook'のシート情報を取得しよう
Q3.'workbook'のシート名'Sheet1'を指定しよう（'workbook'に注意しよう）
Q4.'title'メソッドを呼び出して，指定したシートのタイトルを取得しよう
Q5.'value'メソッドを使い，指定したシート内のセル情報を取得しよう
Q6.指定したシート内のセルにテキストを書き込もう
Q7.'save'メソッドを使い，'output'ディレクトリにファイルを保存しよう

プログラムが書けたら，保存して，実行結果を確認しよう
C-x C-s
C-x o 
~/ta_pp2/w09/easy$ ./command.sh

出力結果が一致したらPythonファイルを閉じる
C-x o
C-x k RET

# w09.7 演習問題（normal）
C-x o
~/ta_pp2/w09/easy$ cd ../normal
~/ta_pp2/w09/normal$ ls
~/ta_pp2/w09/normal$ ./command.sh

# w09.8 command.shの編集
C-x o
C-x C-f ~/ta_pp2/w09/normal/command.sh

#!/bin/bash

./clean.sh
python3 normal.py
#python3 answer.py
libreoffice --nologo --writer ./output/normal_example.xlsx

上記の形式に修正したら保存する
C-x C-s
C-x k RET

# w09.9 演習問題の確認
C-x C-f ~/ta_pp2/w09/normal/normal.py

問題一覧
Q1.'Workbook'モジュールで新規ファイルを作成しよう
Q2.'title'メソッドを使い，シート名を定義しよう
Q3.'create_sheet'メソッドを使い，2つ目のシートを'swap_rows_and_cols'という名前で作成しよう
Q4.'save'メソッドを使い，'output'ディレクトリに保存しよう
Q5.4問目と同じパスを，{}内に記述しよう

プログラムが書けたら，保存して，実行結果を確認しよう
C-x C-s
C-x o 
~/ta_pp2/w09/normal$ ./command.sh

出力結果が一致したらPythonファイルを閉じる
C-x o
C-x k RET

# w09.10 演習問題（hard）
C-x o
~/ta_pp2/w09/normal$ cd ../hard
~/ta_pp2/w09/hard$ ls
~/ta_pp2/w09/hard$ ./command.sh

# w09.11 command.shの編集
C-x C-f ~/ta_pp2/w09/hard/command.sh

#!/bin/bash

./clean.sh
source ~/venv/py3.10.12/bin/activate
python3 hard.py
#python3 answer.py
libreoffice --nologo --writer ./output/hard_example.xlsx

上記の形式に修正したら保存する
C-x C-s
C-x k RET

# w09.12 演習問題の確認
C-x C-f ~/ta_pp2/w09/hard/hard.py

問題一覧
Q1.Pathオブジェクトを生成しよう
Q2.対象のExcelファイルを読み込もう
Q3.計算結果を入力するためのシートを新規作成しよう
Q4.'output'ディレクトリに保存しよう

プログラムが書けたら，保存して，実行結果を確認しよう
C-x C-s
C-x o 
~/ta_pp2/w09/hard$ ./command.sh

出力結果が一致したらPythonファイルを閉じる
C-x o
C-x k RET
