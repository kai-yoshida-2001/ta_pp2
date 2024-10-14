#!/usr/bin/env python3

from PyPDF2 import PdfReader, PdfWriter
import os

# 対象のpdfファイルを定義
os.mkdir('output')
input_file = './input/meetingminutes.pdf'
output_file = './output/division.pdf'

with open(input_file, 'rb') as file:
    reader = PdfReader(file)

    # 総ページ数を取得して変数に定義
    total_pages = len(reader.pages)

    print('##########')
    print(f'総ページ数：{total_pages}')

    # テキストを取得したいページ数を定義
    page_number = 0

    page = reader.pages[page_number]

    # テキストを取得
    text = page.extract_text()

    print('##########')
    print('取得したテキスト：', '\n', text)

    writer = PdfWriter()

    # 取得した全ページ数を取得して，最初の5ページを新しいpdfファイルに追加する
    for page_num in range(5):
        writer.add_page(reader.pages[page_num])

    with open(output_file, 'wb') as pages:
        writer.write(pages)

    print('##########')
    print(f'{output_file}を保存しました')
