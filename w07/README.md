### 第7週の復習 画像の操作の復習###

## [w07] 準備 ##

# w07.1 リポジトリのクローン
Terminalを開く（Terminalでの操作は$で示す．$の前はディレクトリを表す）
~$ rm -rf ~/ta_pp2
~$ cd; git clone github:kai-yoshida-2001/ta_pp2.git
~/ta_pp2$ git pull

# w07.2 演習用ファイルの表示
~$ tree ta_pp2/w07

# w07.3 README.mdの表示
~$ emacs -nw ta_pp2/w07/README.md

# w07.4 演習問題（easy）
~/ta_pp2/w07$ cd easy/
~/ta_pp2/w07/easy$ ls
~/ta_pp2/w07/easy$ ./command.sh

# w07.5 command.shの編集
上画面に移動
C-x o
ファイルを開く
C-x C-f ~/ta_pp2/w07/easy/command.sh

#!/bin/bash

./clean.sh
source ~/venv/py3.10.12/bin/activate
python3 easy.py
#python3 answer.py

上記の形式に修正したら保存する
C-x C-s
C-x k RET

# w07.6 演習問題の確認
C-x C-f ~/ta_pp2/w07/easy/easy.py

問題一覧
Q1. 'input'ディレクトリにある'example.png'を'open'メソッドを使って設定しよう
Q2. 台紙となる画像を'new'メソッドを使って新規作成しよう
Q3. 'img_1'のサイズを'resize'しよう
Q4. 'img_2'に'new_img_1'を'paste'（貼り付け）しよう
Q5. 'Draw'オブジェクトを生成し，引数に'img_2'を設定しよう

プログラムが書けたら，保存して，実行結果を確認しよう
C-x C-s
C-x o 
~/ta_pp2/w07/easy$ ./command.sh

出力結果が一致したらPythonファイルを閉じる
C-x o
C-x k RET

# w07.7 演習問題（normal）
C-x o
~/ta_pp2/w07/easy$ cd ../normal
~/ta_pp2/w07/normal$ ls
~/ta_pp2/w07/normal$ ./command.sh

# w07.8 command.shの編集
C-x o
C-x C-f ~/ta_pp2/w07/normal/command.sh

#!/bin/bash

./clean.sh
source ~/venv/py3.10.12/bin/activate
python3 normal.py
#python3 answer.py

上記の形式に修正したら保存する
C-x C-s
C-x k RET

# w07.9 演習問題の確認
C-x C-f ~/ta_pp2/w07/normal/normal.py

問題一覧
Q1. 台紙となる画像を'new'メソッドを使って新規作成しよう
Q2. 'input'ディレクトリにある'flower.png'を'open'メソッドを使って設定しよう
Q3. 'im_base'に'im_flower'を'paste'（貼り付け）しよう
Q4. 'Draw'オブジェクトを生成し，引数に'im_base'を設定しよう


プログラムが書けたら，保存して，実行結果を確認しよう
C-x C-s
C-x o 
~/ta_pp2/w07/normal$ ./command.sh

出力結果が一致したらPythonファイルを閉じる
C-x o
C-x k RET

# w07.10 演習問題（hard）
C-x o
~/ta_pp2/w07/normal$ cd ../hard
~/ta_pp2/w07/hard$ ls
~/ta_pp2/w07/hard$ ./command.sh

# w07.11 command.shの編集
C-x C-f ~/ta_pp2/w07/hard/command.sh

#!/bin/bash

./clean.sh
source ~/venv/py3.10.12/bin/activate
python3 hard.py
#python3 answer.py

上記の形式に修正したら保存する
C-x C-s
C-x k RET

# w07.12 演習問題の確認
C-x C-f ~/ta_pp2/w07/hard/hard.py

問題一覧
Q1. 台紙となる画像を新規作成しよう
Q2. 'flower.png'を設定しよう
Q3. 台紙に'im_flower'を貼り付けよう
Q4. Drawオブジェクトを生成して引数を設定しよう
Q5. 'pyinputplus'を使って，Str型で入力を受け付けるように設定しよう
Q6. 'pyinputplus'を使って，整数（Int）型で入力を受け付けるように設定しよう

プログラムが書けたら，保存して，実行結果を確認しよう
C-x C-s
C-x o 
~/ta_pp2/w07/hard$ ./command.sh

出力結果が一致したらPythonファイルを閉じる
C-x o
C-x k RET
