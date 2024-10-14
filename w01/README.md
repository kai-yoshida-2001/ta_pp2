### 第1週の復習 PDFとWord文書の操作###

## [w01] 準備 ##

# w01.1 リポジトリのクローン
Terminalを開く（Terminalでの操作は$で示す．$の前はディレクトリを表す）
~$ rm -rf ~/ta_pp2
~$ cd; git clone github:kai-yoshida-2001/ta_pp2.git

# w01.2 演習用ファイルの表示
~$ tree ta_pp2/w01

# w01.3 README.mdの表示
~$ emacs -nw ta_pp2/w01/README.md

[Emacsのショートカット]
C-n で下へ移動
C-p で上へ移動
C-f で右へ移動
C-b で左へ移動
C-a で行頭へ移動
C-x C-c で終了

[Terminalのショートカット]
C-p で前のコマンドを表示
C-n で次のコマンドを表示

~$ emacs -nw ta_pp2/w01/README.md

# w01.4 ライブラリのインストール
[Emacsのショートカット]
C-x 2 でバッファを分割
C-x o で次のバッファへ移動
C-x a でバッファ内でTerminalを起動

~/ta_pp2/w01$ ./command.sh

## [w01] PyPDF2 モジュールの基本操作を理解しよう ##

# w01.5 入力ファイルの確認
FilesでHome -> ta_pp2 -> w01 -> pypdf -> input -> meetingminutes.pdfの内容を確認する

# w01.6 プログラムの実行
~/ta_pp2/w01$ cd pypdf
~/ta_pp2/w01/pypdf$ ls
~/ta_pp2/w01/pypdf$ ./command.sh
division.pdfのウィンドウを閉じる（右上のx印をクリック）

# w01.7 出力ファイルの確認
~/ta_pp2/w01/pypdf$ ls
~/ta_pp2/w01/pypdf$ ls output
~/ta_pp2/w01/pypdf$ evince output/division.pdf
FilesでHome -> ta_pp2 -> w01 -> pypdf -> output -> division.pdfの内容を確認する

# w01.8 プログラムの確認
C-x C-f ~/ta_pp2/w01/pypdf/basic_operation.py
C-x k RET

# w01.9 出力ファイルの削除
~/ta_pp2/w01/pypdf$ ls
~/ta_pp2/w01/pypdf$ ./clean.sh
~/ta_pp2/w01/pypdf$ ls

## [w01] docx モジュールの基本操作を理解しよう ##
# w01.10 プログラムの確認
~/ta_pp2/w01/pypdf$ cd ../docx
~/ta_pp2/w01/docx$ ls
C-x C-f ~/ta_pp2/w01/docx/basic_operation.py
C-x k RET

# w01.11 プログラムの実行
~/ta_pp2/w01/docx$ ./command.sh

# w01.12 出力ファイルの確認
~/ta_pp2/w01/docx$ ls
~/ta_pp2/w01/docx$ ls output
~/ta_pp2/w01/docx$ libreoffice --nologo --writer output/new.docx
FilesでHome -> ta_pp2 -> w01 -> docx -> output ->new.docxの内容を確認する

# w01.13 出力ファイルの削除
~/ta_pp2/w01/docx$ ls
~/ta_pp2/w01/docx$ ./clean.sh
~/ta_pp2/w01/docx$ ls

## [w01] question.pyの'???'を埋めて招待状を作成するプログラムを完成させよう ##

# w01.14 ディレクトリの移動
~/ta_pp2/w01/docx$ cd ../practice
~/ta_pp2/w01/practice$ ls

# w01.15 問題
Q1. inputフォルダの中にある ’.txt’ ファイルを指定しよう（ヒント：$ ls input/）
Q2. '敬具'を右寄せに指定しよう（ヒント：ta_pp2/w01/docx/basic_operation.py）
Q3. ’記’を中央寄せに指定しよう（ヒント：Q2. と同じ）
Q4. '以上'を右寄せに指定しよう（ヒント：Q2. と同じ）

# w01.16 プログラムの確認
C-x C-f ~/ta_pp2/w01/practice/question.py
C-x k RET

# w01.17 プログラムの実行
~/ta_pp2/w01/practice$ ./command.sh

# w01.18 出力ファイルの確認
~/ta_pp2/w01/practice$ ls
~/ta_pp2/w01/practice$ ls output
~/ta_pp2/w01/practice$ libreoffice --nologo --writer output/invitations.docx
FilesでHome -> ta_pp2 -> w01 -> practice -> output -> invitations.docxの内容を確認する

# w01.19 入力ファイルの編集（時間がある人は）
C-x C-f ~/ta_pp2/w01/practice/input/guests.txt
C-f を2回押してカーソルを右へ2つ移動する
C-k でカーソル以降を削除する
Shift + Space を押して日本語入力モードにする
花子と入力する
Shift + Space を押して英語入力モードに戻す
C-x C-s で保存する
C-x k RET でバッファを削除する

# w01.20 入力ファイルの確認
~/ta_pp2/w01/practice$ cat input/guests.txt

# w01.21 プログラムの再実行
~/ta_pp2/w01/practice$ ./command.sh

# w01.22 出力ファイルの削除
~/ta_pp2/w01/practice$ ls
~/ta_pp2/w01/practice$ ./clean.sh
~/ta_pp2/w01/practice$ ls
