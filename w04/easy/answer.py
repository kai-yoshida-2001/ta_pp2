#!/usr/bin/env python3

import os, re, shutil, pyperclip
from pathlib import Path

os.mkdir('output')
image_file = 'sample.png'
input_dir = './input'
output_dir = './output'

# Q1. inputとoutputのPathオブジェクトを生成しよう 
input_path = Path(input_dir, image_file)
output_path = Path(output_dir, image_file)
print(f'file:{input_path}, {input_path.name}, {input_path.stem}, {input_path.suffix}')
# Q2. 生成したPathオブジェクトを使ってファイルをコピーしよう
shutil.copy(input_path, output_path)

# Q3. 読み込みモードでsample.txtのテキスト情報を取得しよう
text_file = './input/sample.txt'
with open(text_file, 'r') as file:
    get_text = file.read()
    print(f'取得したテキスト情報：\n{get_text}')

# Q4. 新規テキストファイルを作成してテキストを書き込もう
with open(text_file, 'w') as file:
    file.write('これはPythonで作成したテキストファイルです．')

# Q5. text変数の情報をクリップボードに記憶させよう
text = "これは，クリップボードにコピーしたテキストです．"
pyperclip.copy(text)
print('テキストファイルやChromeを立ち上げて，ペーストしてみよう')
