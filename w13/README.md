### 第13週の復習 時間管理，タスクのスケジューリング，プログラム起動の復習###

## [w13] 準備 ##

# w13.1 リポジトリのクローン
Terminalを開く（Terminalでの操作は$で示す．$の前はディレクトリを表す）
~$ rm -rf ~/ta_pp2
~$ cd; git clone github:kai-yoshida-2001/ta_pp2.git
~/ta_pp2$ git pull

# w13.2 演習用ファイルの表示
~$ tree ta_pp2/w13

# w13.3 README.mdの表示
~$ emacs -nw ta_pp2/w13/README.md

# w13.4 演習問題（easy）
~/ta_pp2/w13$ cd easy/
~/ta_pp2/w13/easy$ ls
~/ta_pp2/w13/easy$ ./command.sh

# w13.5 command.shの編集
上画面に移動
C-x o
ファイルを開く
C-x C-f ~/ta_pp2/w13/easy/command.sh

#!/bin/bash

rm -rf *~
source ~/venv/py3.10.12/bin/activate
python3 easy_datetime.py
#python3 easy_threading.py
#python3 easy_subprocess.py
#python3 easy_multiprocessing.py
#python3 answer_datetime.py
#python3 answer_threading.py
#python3 answer_subprocess.py
#python3 answer_multiprocessing.py

上記の形式に修正したら保存する
C-x C-s
C-x k RET

* 上記の編集作業を，問題数分繰り返す

# w13.6 演習問題の確認(easy_datetime.py)
C-x C-f ~/ta_pp2/w13/easy/easy_datetime.py

問題一覧
Q1.今の日時情報を取得しよう
Q2.年の情報だけを取得して表示させよう
Q3.月の情報だけを取得して表示させよう
Q4.日の情報だけを取得して表示させよう
Q5.曜日の情報だけを取得して表示させよう
Q6.今日から10日後の日付を計算しよう
Q7.10日後の月と日付の情報を出力させよう
Q8.今日から1週間前の日付を計算しよう
Q9.1週間前の月と日付の情報を出力させよう

プログラムが書けたら，保存して，実行結果を確認しよう
C-x C-s
C-x o 
~/ta_pp2/w12/easy$ ./command.sh

# w13.7 演習問題の確認(easy_threading.py)
C-x C-f ~/ta_pp2/w13/easy/easy_threading.py

問題一覧
Q1.平行処理のためのスレッドを作成しよう
Q2.作成したスレッドを開始させよう
Q3.スレッドの終了を待機しよう

プログラムが書けたら，保存して，実行結果を確認しよう
C-x C-s
C-x o 
~/ta_pp2/w12/easy$ ./command.sh

出力結果が一致したらPythonファイルを閉じる
C-x o
C-x k RET

# w13.8 演習問題の確認(easy_subprocess.py)
C-x C-f ~/ta_pp2/w13/easy/easy_subprocess.py

問題一覧
Q1.subprocessを実行させよう
Q2.subprocessを実行させよう

プログラムが書けたら，保存して，実行結果を確認しよう
C-x C-s
C-x o 
~/ta_pp2/w12/easy$ ./command.sh

出力結果が一致したらPythonファイルを閉じる
C-x o
C-x k RET

# w13.9 演習問題の確認(easy_multiprocessing.py)
C-x C-f ~/ta_pp2/w13/easy/easy_multiprocessing.py

問題一覧
Q1.並列で実行するプロセスを作成しよう
Q2.プロセスを開始させよう
Q3.プロセスの終了を待機させよう

プログラムが書けたら，保存して，実行結果を確認しよう
C-x C-s
C-x o 
~/ta_pp2/w12/easy$ ./command.sh

出力結果が一致したらPythonファイルを閉じる
C-x o
C-x k RET

# w13.10 演習問題（normal）
C-x o
~/ta_pp2/w12/easy$ cd ../normal
~/ta_pp2/w12/normal$ ls
~/ta_pp2/w12/normal$ ./command.sh

# w13.11 command.shの編集
C-x o
C-x C-f ~/ta_pp2/w13/normal/command.sh

#!/bin/bash

python3 normal.py
#python3 answer.py

上記の形式に修正したら保存する
C-x C-s
C-x k RET

# w13.12 演習問題の確認
C-x C-f ~/ta_pp2/w13/normal/normal.py

問題一覧
Q1.システムの開始時点での日時を取得しよう
Q2.サブプロセスを実行させよう
Q3.システムの終了時点での日時を取得しよう
Q4.スレッドを作成しよう
Q5.作成したスレッドを開始しよう
Q6.スレッドの終了を待機しよう

プログラムが書けたら，保存して，実行結果を確認しよう
C-x C-s
C-x o 
~/ta_pp2/w12/normal$ ./command.sh

出力結果が一致したらPythonファイルを閉じる
C-x o
C-x k RET
