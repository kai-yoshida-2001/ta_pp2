### 第6週の復習 Webスクレイピングの復習###

## [w06] 準備 ##

# w06.1 リポジトリのクローン
Terminalを開く（Terminalでの操作は$で示す．$の前はディレクトリを表す）
~$ rm -rf ~/ta_pp2
~$ cd; git clone github:kai-yoshida-2001/ta_pp2.git
~/ta_pp2$ git pull

# w06.2 演習用ファイルの表示
~$ tree ta_pp2/w06

# w06.3 README.mdの表示
~$ emacs -nw ta_pp2/w06/README.md

# w06.4 command.shの実行
~/ta_pp2/w06$ ./command.sh

# w06.5 演習問題（easy）
~/ta_pp2/w06$ cd easy/
~/ta_pp2/w06/easy$ ls
~/ta_pp2/w06/easy$ ./command.sh

# w06.5 command.shの編集
上画面に移動
C-x o
ファイルを開く
C-x C-f ~/ta_pp2/w06/easy/command.sh

#!/bin/bash

source ~/venv/py3.10.12/bin/activate
python3 easy.py
#python3 answer.py

上記の形式に修正したら保存する
C-x C-s
C-x k RET

# w06.6 演習問題の確認
C-x C-f ~/ta_pp2/w06/easy/easy.py

問題一覧
Q1. テキスト情報を取得するために'BeautifulSoup'を指定しよう
Q2. 取得したテキストの中から'title'を取得しよう
Q3. 'driver'に'url'を設定しよう
Q4. ブラウザを閉じるように設定しよう
Q5. 'soup'を使って画像（img）情報を取得しよう

プログラムが書けたら，保存して，実行結果を確認しよう
C-x C-s
C-x o 
~/ta_pp2/w06/easy$ ./command.sh

出力結果が一致したらPythonファイルを閉じる
C-x o
C-x k RET

# w06.7 演習問題（normal）
C-x o
~/ta_pp2/w06/easy$ cd ../normal
~/ta_pp2/w06/normal$ ls
~/ta_pp2/w06/normal$ ./command.sh

# w06.8 command.shの編集
C-x o
C-x C-f ~/ta_pp2/w06/normal/command.sh

#!/bin/bash

source ~/venv/py3.10.12/bin/activate
python3 normal.py
#python3 answer.py

上記の形式に修正したら保存する
C-x C-s
C-x k RET

# w06.9 演習問題の確認
C-x C-f ~/ta_pp2/w06/normal/normal.py

問題一覧
Q1. 'webdriver'に'chrome'ブラウザを設定しよう
Q2. 'driver'に'search_url'を設定しよう
Q3. 'soup'で'select'するタグを'div'に設定しよう


プログラムが書けたら，保存して，実行結果を確認しよう
C-x C-s
C-x o 
~/ta_pp2/w06/normal$ ./command.sh

出力結果が一致したらPythonファイルを閉じる
C-x o
C-x k RET

# w06.10 演習問題（hard）
C-x o
~/ta_pp2/w06/normal$ cd ../hard
~/ta_pp2/w06/hard$ ls
~/ta_pp2/w06/hard$ ./command.sh

# w06.11 command.shの編集
C-x C-f ~/ta_pp2/w06/hard/command.sh

#!/bin/bash

source ~/venv/py3.10.12/bin/activate
python3 hard.py
#python3 answer.py

上記の形式に修正したら保存する
C-x C-s
C-x k RET

# w06.12 演習問題の確認
C-x C-f ~/ta_pp2/w06/hard/hard.py

問題一覧
Q1. 'webdriver'に'chrome'ブラウザを設定しよう
Q2. 'driver'を設定しよう
Q3. 'soup'変数に'BeautifulSoup'の設定を定義しよう
Q4. pyinputplusの'inputStr'メソッドを設定しよう
Q5. 'Exception'クラスを使ってカスタムメッセージを設定しよう

プログラムが書けたら，保存して，実行結果を確認しよう
C-x C-s
C-x o 
~/ta_pp2/w06/hard$ ./command.sh

出力結果が一致したらPythonファイルを閉じる
C-x o
C-x k RET
