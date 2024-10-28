### 第4週の復習 ファイルの読み書き###

## [w04] 準備 ##

# w04.1 リポジトリのクローン
Terminalを開く（Terminalでの操作は$で示す．$の前はディレクトリを表す）
~$ rm -rf ~/ta_pp2
~$ cd; git clone github:kai-yoshida-2001/ta_pp2.git

# w04.2 演習用ファイルの表示
~$ tree ta_pp2/w03

# w04.3 README.mdの表示
~$ emacs -nw ta_pp2/w04/README.md

# w04.4 演習問題（easy）
~/ta_pp2/w04$ cd easy/
~/ta_pp2/w04/easy$ ls
~/ta_pp2/w04/easy$ ./command.sh

# w04.5 command.shの編集
上画面に移動
C-x o
ファイルを開く
C-x C-f ~/ta_pp2/w04/easy/command.sh

#!/bin/bash

source ~/venv/py3.10.12/bin/activate
python3 easy.py
#python3 easy_answer.py

上記の形式に修正したら保存する
C-x C-s
C-x k RET

# w04.6 演習問題の確認
C-x C-f ~/ta_pp2/w04/easy/easy.py

問題一覧
Q1. inputとoutputのPathオブジェクトを生成しよう
Q2. 生成したPathオブジェクトを使ってファイルをコピーしよう
Q3. 読み込みモードでsample.txtのテキスト情報を取得しよう
Q4. 新規テキストファイルを作成してテキストを書き込もう
Q5. text変数の情報をクリップボードに記憶させよう

プログラムが書けたら，保存して，実行結果を確認しよう
C-x C-s
C-x o 
~/ta_pp2/w04/easy$ ./command.sh

出力結果が一致したらPythonファイルを閉じる
C-x o
C-x k RET

# w04.7 演習問題（normal）
C-x o
~/ta_pp2/w04/easy$ cd ../normal
~/ta_pp2/w04/normal$ ls
~/ta_pp2/w04/normal$ ./command.sh

# w04.8 command.shの編集
C-x o
C-x C-f ~/ta_pp2/w04/normal/command.sh

#!/bin/bash

source ~/venv/py3.10.12/bin/activate
python3 normal.py
#python3 normal_answer.py

上記の形式に修正したら保存する
C-x C-s
C-x k RET

# w04.9 演習問題の確認
C-x C-f ~/ta_pp2/w04/normal/normal.py

問題一覧
Q1. Pathオブジェクトを生成しよう
Q2. 読み込みモードを使ってテキスト情報を取得しよう
Q3. クリップボードにテキスト情報を記憶させよう

プログラムが書けたら，保存して，実行結果を確認しよう
C-x C-s
C-x o 
~/ta_pp2/w04/normal$ ./command.sh

出力結果が一致したらPythonファイルを閉じる
C-x o
C-x k RET

# w04.10 演習問題（hard）
C-x o
~/ta_pp2/w04/normal$ cd ../hard
~/ta_pp2/w04/hard$ ls
~/ta_pp2/w04/hard$ ./command.sh

# w04.8 command.shの編集
C-x C-f ~/ta_pp2/w04/hard/command.sh

#!/bin/bash

source ~/venv/py3.10.12/bin/activate
python3 hard.py
#python3 hard_answer.py

上記の形式に修正したら保存する
C-x C-s
C-x k RET

# w04.9 演習問題の確認
C-x C-f ~/ta_pp2/w04/hard/hard.py

問題一覧
Q1. pyinputplusモジュールで，ファイルパスを受け取る関数を設定しよう
Q2. Eメールの正規表現を使ってRegexオブジェクトを生成しよう
Q3. 抽出したEメールを保存するためのPathオブジェクトを生成しよう
Q4. 対象のファイルを読み込めるように設定しよう
Q5. 設定したパターンとマッチするものを1つずつ取得しよう
Q6. 新規テキストファイルを作成し，抽出したテキストを書き込もう
Q7. 

プログラムが書けたら，保存して，実行結果を確認しよう
C-x C-s
C-x o 
~/ta_pp2/w04/hard$ ./command.sh

出力結果が一致したらPythonファイルを閉じる
C-x o
C-x k RET
