#!/usr/bin/env python3

import ezsheets, os

os.chdir('../output')

spreadsheet_name = "ta_pp2_easy"

# Q1.スプレッドシートを新規作成しよう
# Q2.'title'に'spreadsheet_name'を設定しよう
spreadsheet = ezsheets.createSpreadsheet(title=spreadsheet_name)

# Q3.'spreadsheet'の'id'を取得して出力しよう
print(f"スプレッドシート '{spreadsheet_name}' が作成されました。ID: {spreadsheet.id}")

# Q4.最初のシートを指定しよう
sheet = spreadsheet[0]

# Q5.各行にデータを書き込もう（更新しよう）
sheet.updateRow(1, ['名前', '点数', '結果'])
sheet.updateRow(2, ['山田', 85, '合格'])
sheet.updateRow(3, ['田中', 60, '合格'])
sheet.updateRow(4, ['佐藤', 40, '不合格'])

print(f'新規作成したスプレッドシートにデータを書き込みました')
