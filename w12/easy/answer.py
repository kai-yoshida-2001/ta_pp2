#!/usr/bin/env python3

import csv, json, os
from pathlib import Path

# CSVファイルの操作（読み取りと書き込み）
def read_csv(csv_file):
    data = []
    with open(csv_file, mode='r', encoding='utf-8') as file:
        # Q1.データを読み取るためのオブジェクトを作成しよう
        reader = csv.reader(file)
        print(f'{csv_file}の内容:')
        for row in reader:
            data.append(row)
            print(row)
    return data

def write_csv(csv_file, data):
    with open(csv_file, mode='a', encoding='utf-8', newline='') as file:
        # Q2.データを書き込むためのオブジェクトを作成しよう
        writer = csv.writer(file)
        # Q3.1行ごとにデータを書き込もう
        writer.writerow(data)
    print(f'{csv_file}へデータを書き込みました')

###########################################################

# JSONファイルの操作（書き込みと読み取り）
def write_json(csv_file, json_file):
    csv_data = read_csv(csv_file)
    with open(json_file, mode='w', encoding='utf-8') as file:
        # Q4.データを書き込むためのメソッドを呼び出そう
        json.dump(csv_data, file, ensure_ascii=False, indent=4)
    print(f'{csv_file}のデータを{json_file}に複製しました')

def read_json(json_file):
    with open(json_file, mode='r', encoding='utf-8') as file:
        # Q5.データの読み取るためのメソッドを呼び出そう
        data = json.load(file)
    print(f'{json_file}の内容：')
    for item in data:
        print(item)
    return data

if __name__ == '__main__':
    os.makedirs('./output', exist_ok=True)
    csv_file = Path('./input/sample.csv')
    json_file = Path('./output/sample.json')
    # Q6.名前や数字を自分好みに変更して，データの中身が増えることを確認しよう
    insert_data = ['吉田', 50, 50, 50]
    read_csv(csv_file)
    write_csv(csv_file, insert_data)
    write_json(csv_file, json_file)
    read_json(json_file)
