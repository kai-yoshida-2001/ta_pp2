#!/usr/bin/env python3

import ezsheets, statistics, os

os.chdir('../output')

org_ss_id = '19jJbWx5zU_uh_5LAgWYxjHCEVr9VG3sl8wBKeLms4BM'
# Q1.既存のスプレッドシートを読み込もう
org_ss = ezsheets.Spreadsheet(org_ss_id)

file_name = 'ta_pp2_hard.xlsx'
# Q2.'Excel'拡張子でダウンロードしよう
org_ss.downloadAsExcel(file_name)
# Q3. 自分のDriveに'upload'しよう
new_ss = ezsheets.upload(file_name)
os.remove(file_name)
# Q4.'title'と'id'を取得しよう
print(f'{new_ss.title}を複製しました．\nID：{new_ss.id}')

sheet = new_ss[0]
names = [name for name in sheet.getColumn(1)[1:] if name.strip()]
score_raw = [score for score in sheet.getColumn(2)[1:] if score.strip()]

scores = [int(score) if score.replace('.', '', 1).isdigit() else 0 for score in score_raw]

if len(names) != len(scores):
    raise ValueError('名簿とデータ数が一致しません')

total = sum(scores)
average = total / len(scores) if len(scores) > 0 else 0
std_dev = statistics.stdev(scores) if len(scores) > 1 else 0
deviation_scores = [(score - average) / std_dev * 10 + 50 if std_dev > 0 else 50 for score in scores]

# Q5.シートを新規作成しよう
result_s = new_ss.createSheet(title='集計結果')
# Q6.行にデータを書き込もう
result_s.updateRow(1, ['名簿', '点数', '偏差値'])
for i, (name, score, deviation_score) in enumerate(zip(names, scores, deviation_scores), start=2):
    # Q7.行にデータを書き込もう
    result_s.updateRow(i, [name, score, round(deviation_score, 2)])

final_row = len(names) + 3
# Q8.行にデータを書き込もう
result_s.updateRow(final_row, ['合計値', total])
result_s.updateRow(final_row + 1, ['平均', round(average, 2)])
result_s.updateRow(final_row + 2, ['標準偏差', round(std_dev, 2)])

print('集計結果をシートに書き込みました')
