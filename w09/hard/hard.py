#!/usr/bin/env python3

import openpyxl, os
from pathlib import Path

# Q1.Pathオブジェクトを生成しよう
input_path = ???('./input/hard_example.xlsx')
output_path = ???('./output/output_example.xlsx')
os.makedirs(output_path.parent, exist_ok=True)

# Q2.対象のExcelファイルを読み込もう
wb = ???.???(???)
sheet1 = wb['Sheet1']

scores = []
for row in sheet1.iter_rows(min_row=2, max_col=2, values_only=True):
    name, score = row
    if score is not None:
        scores.append(score)

total = sum(scores)
average = total / len(scores)

distribution = {
    '70点未満': len([s for s in scores if s < 70]),
    '70以上80点未満': len([s for s in scores if 70 <= s < 80]),
    '80点以上90点未満': len([s for s in scores if 80 <= s < 90]),
    '90点以上': len([s for s in scores if s >= 90]),
}

# Q3.計算結果を入力するためのシートを新規作成しよう
sheet2 = ???.???('Sheet2')
sheet2.append(['合計点', total])
sheet2.append(['平均点', round(average, 2)])

sheet2.append(['点数分布'])
for category, count in distribution.items():
    sheet2.append([category, count])

# Q4.'output'ディレクトリに保存しよう
???.???(???)
print(f'計算結果を{output_path}に保存しました')
