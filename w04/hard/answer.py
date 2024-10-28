#!/usr/bin/env python3

import os, re
import pyinputplus as pyip
from pathlib import Path

# Q1. pyinputplusモジュールで，ファイルパスを受け取る関数を設定しよう
input_dir = pyip.inputFilepath("操作するディレクトリパスを入力してください：")
dir_path = Path(input_dir)

# Q2. Eメールの正規表現を使ってRegexオブジェクトを生成しよう
email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')

os.mkdir('output')
# Q3. 抽出したEメールを保存するためのPathオブジェクトを生成しよう
output_file = Path("./output/extracted_emails.txt")

extracted_emails = []
for text_file in dir_path.glob("*.txt"):
    # Q4. 対象のファイルを読み込めるように設定しよう
    with open(text_file, 'r') as f:
        for line in f:
            # Q5. 設定したパターンとマッチするものを1つずつ取得しよう
            match = email_pattern.search(line)
            if match:
                extracted_emails.append(match.group())

if extracted_emails:
    # Q6. 新規テキストファイルを作成し，抽出したテキストを書き込もう
    with open(output_file, 'w') as f:
        f.write('\n'.join(extracted_emails))
    print(f"{len(extracted_emails)}件のメールアドレスが{output_file}に保存されました．")

else:
    print("メールアドレスを含む行が見つかりませんでした")
