### 第14週の復習 GUIの操作の復習###

## [w14] 準備 ##

# w14.1 リポジトリのクローン
Terminalを開く（Terminalでの操作は$で示す．$の前はディレクトリを表す）
~$ rm -rf ~/ta_pp2
~$ cd; git clone github:kai-yoshida-2001/ta_pp2.git
~/ta_pp2$ git pull

# w14.2 演習用ファイルの表示
~$ tree ta_pp2/w14

# w14.3 README.mdの表示
~$ emacs -nw ta_pp2/w14/README.md

# w14.4 演習問題（easy）
~/ta_pp2/w14$ cd easy/
~/ta_pp2/w14/easy$ ls
~/ta_pp2/w14/easy$ ./command.sh

# w14.5 command.shの編集
上画面に移動
C-x o
ファイルを開く
C-x C-f ~/ta_pp2/w14/easy/command.sh

#!/bin/bash

source ~/venv/py3.10.12/bin/activate
python3 easy.py
#python3 answer.py

上記の形式に修正したら保存する
C-x C-s
C-x k RET

# w14.6 演習問題の確認
C-x C-f ~/ta_pp2/w14/easy/easy.py

問題一覧
Q1.マウス（カーソル）を画面の（100, 100）の位置に移動させよう
Q2.クリックさせよう
Q3.マウス（カーソル）の現在地を取得しよう
Q4.ドラッグ動作をさせてみよう

プログラムが書けたら，保存して，実行結果を確認しよう
C-x C-s
C-x o 
~/ta_pp2/w14/easy$ ./command.sh

出力結果が一致したらPythonファイルを閉じる
C-x o
C-x k RET

# w14.7 演習問題（normal）
C-x o
~/ta_pp2/w14/easy$ cd ../normal
~/ta_pp2/w14/normal$ ls
~/ta_pp2/w14/normal$ ./command.sh

# w14.8 command.shの編集
C-x o
C-x C-f ~/ta_pp2/w14/normal/command.sh

#!/bin/bash

python3 normal.py
#python3 answer.py

上記の形式に修正したら保存する
C-x C-s
C-x k RET

# w14.9 演習問題の確認
C-x C-f ~/ta_pp2/w14/normal/normal.py

問題一覧
Q1.Terminal上に指定のテキストを書き込めるようにしよう
Q2.Enterキーを押すように設定しよう
Q3.Terminal上に指定のテキストを書き込めるようにしよう
   *カレントディレクトリが'~/pp2'に変化していることを確認しよう
Q4.Enterキーを押すように設定しよう

プログラムが書けたら，保存して，実行結果を確認しよう
C-x C-s
C-x o 
~/ta_pp2/w14/normal$ ./command.sh

出力結果が一致したらPythonファイルを閉じる
C-x o
C-x k RET
