#!/usr/bin/env python3

import docx
from docx.shared import Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
import os

# テキストを取得したいdocxファイルを定義
file_name = './input/demo.docx'
docx_file = docx.Document(file_name)

# テキストを取得して出力
for paragraph in docx_file.paragraphs:
    print(paragraph.text)

# 新しいドキュメントファイルを作成
new_docx = docx.Document()
# ファイル内に貼り付ける画像のパスを指定
image = './input/cat.png'

# 新規ドキュメントファイルにテキストを書き込み
new_docx.add_paragraph('Pythonを使ってドキュメントファイルを作成')
new_docx.add_paragraph('このファイルは，docxモジュールを使って作成しました')

# 新規ドキュメントファイルに画像を貼り付け
new_docx.add_picture(image, width=Inches(2))
new_docx.add_paragraph('可愛い猫ですね')

# 書き込むテキストを中央揃えや右寄せする
new_docx.add_paragraph('この行は，中央揃えにしています').alignment = WD_ALIGN_PARAGRAPH.CENTER
new_docx.add_paragraph('この行は，右寄せしています').alignment = WD_ALIGN_PARAGRAPH.RIGHT

# 書き込みや貼り付けが終わった新規ファイルを保存
os.mkdir('output')
new_docx.save('./output/new.docx')
print('outputフォルダに新規ファイルを保存しました')
