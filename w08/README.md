### 第8週の復習 ファイルの復習###

## [w08] 準備 ##

# w08.1 リポジトリのクローン
Terminalを開く（Terminalでの操作は$で示す．$の前はディレクトリを表す）
~$ rm -rf ~/ta_pp2
~$ cd; git clone github:kai-yoshida-2001/ta_pp2.git
~/ta_pp2$ git pull

# w08.2 演習用ファイルの表示
~$ tree ta_pp2/w08

# w08.3 README.mdの表示
~$ emacs -nw ta_pp2/w08/README.md

# w08.4 演習問題（easy）
~/ta_pp2/w08$ cd easy/
~/ta_pp2/w08/easy$ ls
~/ta_pp2/w08/easy$ ./command.sh

# w08.5 command.shの編集
上画面に移動
C-x o
ファイルを開く
C-x C-f ~/ta_pp2/w08/easy/command.sh

#!/bin/bash

./clean.sh
touch input/unnecessary.txt
source ~/venv/py3.10.12/bin/activate
python3 easy.py
#python3 answer.py

上記の形式に修正したら保存する
C-x C-s
C-x k RET

# w08.6 演習問題の確認
C-x C-f ~/ta_pp2/w08/easy/easy.py

問題一覧
Q1.'copy'メソッドを呼び出して，コピー元とコピー先を引数に指定しよう
Q2.'move'メソッドを呼び出して，移動元と移動先を引数に指定しよう
Q3.'move'メソッドを呼び出して，Q2の移動元と移動先を逆に指定してみよう
Q4.'rmtree'メソッドを呼び出して，'unnecessary'を削除しよう
Q5.'ZipFile'メソッドを呼び出して，'zip_file_name'を引数に指定しよう

プログラムが書けたら，保存して，実行結果を確認しよう
C-x C-s
C-x o 
~/ta_pp2/w08/easy$ ./command.sh

出力結果が一致したらPythonファイルを閉じる
C-x o
C-x k RET

# w08.7 演習問題（normal）
C-x o
~/ta_pp2/w08/easy$ cd ../normal
~/ta_pp2/w08/normal$ ls
~/ta_pp2/w08/normal$ ./command.sh

# w08.8 command.shの編集
C-x o
C-x C-f ~/ta_pp2/w08/normal/command.sh

#!/bin/bash

./clean.sh
mkdir output
touch output/snapshot_20241015_153010.zip
touch output/snapshot_20241020_203520.zip
touch output/snapshot_20241120_123430.zip
source ~/venv/py3.10.12/bin/activate
python3 normal.py
#python3 answer.py

上記の形式に修正したら保存する
C-x C-s
C-x k RET

# w08.9 演習問題の確認
C-x C-f ~/ta_pp2/w08/normal/normal.py

問題一覧
Q1.'Path'オブジェクトを生成し，引数に'dir_output'を指定しよう
Q2.'output_path'と'snapshot'を結合したパスを設定しよう
Q3.'ZipFile'引数に，スナップショットのパスを指定しよう
Q4.'Path'オブジェクトを生成し，引数には'root'を指定しよう

プログラムが書けたら，保存して，実行結果を確認しよう
C-x C-s
C-x o 
~/ta_pp2/w08/normal$ ./command.sh

出力結果が一致したらPythonファイルを閉じる
C-x o
C-x k RET

# w08.10 演習問題（hard）
C-x o
~/ta_pp2/w08/normal$ cd ../hard
~/ta_pp2/w08/hard$ ls
~/ta_pp2/w08/hard$ ./command.sh

# w08.11 command.shの編集
C-x C-f ~/ta_pp2/w08/hard/command.sh

#!/bin/bash

./clean.sh
source ~/venv/py3.10.12/bin/activate
python3 hard.py
#python3 answer.py

上記の形式に修正したら保存する
C-x C-s
C-x k RET

# w08.12 演習問題の確認
C-x C-f ~/ta_pp2/w08/hard/hard.py

問題一覧
Q1.'Path'オブジェクトを生成して，それぞれのディレクトリを引数に指定しよう
Q2.'re'モジュールの'search'メソッドを呼び出そう
Q3.'shutil'モジュールの'copy'メソッドを呼び出そう
Q4.'ZipFile'メソッドを呼び出して，'zip_file'を引数に指定しよう

プログラムが書けたら，保存して，実行結果を確認しよう
C-x C-s
C-x o 
~/ta_pp2/w08/hard$ ./command.sh

出力結果が一致したらPythonファイルを閉じる
C-x o
C-x k RET
