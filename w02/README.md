### 第2週の復習 パターンマッチ###

## [w02] 準備 ##

# w02.1 リポジトリのクローン
Terminalを開く（Terminalでの操作は$で示す．$の前はディレクトリを表す）
~$ rm -rf ~/ta_pp2
~$ cd; git clone github:kai-yoshida-2001/ta_pp2.git

# w02.2 演習用ファイルの表示
~$ tree ta_pp2/w02

# w02.3 README.mdの表示
~$ emacs -nw ta_pp2/w02/README.md

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

~$ emacs -nw ta_pp2/w02/README.md

# w02.4 ライブラリのインストール
[Emacsのショートカット]
C-x 2 でバッファを分割
C-x o で次のバッファへ移動
C-x a でバッファ内でTerminalを起動

~/ta_pp2/w02$ ./command.sh

## [w02] reモジュールの基本操作を理解しよう ##

# w02.5 プログラムの実行
~/ta_pp2/w02$ ls
~/ta_pp2/w02$ ./command.sh

# w02.6 プログラムの確認
C-x C-f ~/ta_pp2/w02/basic_operation.py
C-x k RET

## [w02] question.pyの'???'を埋めて携帯電話番号に対応した正規表現プログラムを完成させよう ##

# w02.7 ディレクトリの移動
~/ta_pp2/w02$ cd practice
~/ta_pp2/w02/practice$ ls

# w02.8 問題
Q1. 携帯電話番号形式の正規表現を設定しよう
Q2. textの中で，正規表現が適用される最初の部分を見つけよう
Q3. textの中で，正規表現が適用される部分を"全て"見つけよう
Q4. 正規表現と一致する文字列を，’###-####-####’に置換しよう
Q5. 置換前と置換後の文字列を出力して，違いを確かめよう

# w02.9 ヒント
’ta_pp2/w02/basic_operation.py’を見てみよう

# w02.10 プログラムの確認
C-x C-f ~/ta_pp2/w02/practice/question.py
C-x k RET

# w02.11 プログラムの実行
~/ta_pp2/w02/practice$ ./command.sh

# w02.12 答え合わせ
C-x C-f ~/ta_pp2/w02/practice/answer.py
