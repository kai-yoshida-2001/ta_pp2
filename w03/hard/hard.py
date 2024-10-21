#!/usr/bin/env python3

import PyPDF2
import re
import pyinputplus as pyip

# Q1. inputフォルダにあるpdfファイルのパスを指定しよう
pdf_file = './input/???'
with open(pdf_file, 'rb') as file:

    # Q2. PDFファイルを読み込むためのオブジェクトを生成しよう
    reader = PyPDF2.Pdf???(file)
    text = ''

    # Q3. PDFファイルのページオブジェクトのリストを作成しよう
    for page in reader.???:
        # Q4. ページから取得したテキストを変数に追加しよう
        text += page.???()

# Q5. 電話番号の正規表現を設定しよう（形式：XXX-XXXX-XXXX）
phone_pattern = re.(r'\d{?}-\d{?}-\d{?}')
# Q6. Q5で設定したパターンに合う形式を全て見つけよう
phone_numbers = phone_pattern.???(text)

if phone_numbers:
    print("以下の電話番号が見つかりました")
    for i, num in enumerate(phone_numbers, start=1):
        print(f"{i}.{num}")
    print("===============")
    
    # Q7. 番号付きのリスト表示となるように設定しよう
    chose_phone = pyip.input???(phone_numbers,
                                 ??? = True,
                                 prompt = "お好きな電話番号を選んでください\n"
                                 )
    print(f"選択された電話番号：{chose_phone}")
else:
    print("電話番号が見つかりませんでした")
