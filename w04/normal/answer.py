#!/usr/bin/env python3

from pathlib import Path
import pyperclip
import os

def combine_and_copy(dir_path):
    all_text = ""
    for file in os.listdir(dir_path):
        # Q1. Pathオブジェクトを生成しよう
        file_path = Path(dir_path, file)
        if file_path.is_file and file_path.suffix == '.txt':
            # Q2. 読み込みモードを使ってテキスト情報を取得しよう
            with open(file_path, 'r', encoding='utf-8') as f:
                all_text += f.read() + '\n'
    # Q3. クリップボードにテキスト情報を記憶させよう
    pyperclip.copy(all_text)
    print("テキストをクリップボードにコピーしました．\nテキストファイルやChromeを立ち上げてペーストしてみましょう．")

dir_path = './input'
combine_and_copy(dir_path)
