#!/usr/bin/env python3

import csv, json, os, requests, time
from pathlib import Path

def read_csv(csv_file):
    city_and_code = []
    # Q1.CSVファイルを保持した変数を指定しよう
    with open(???, mode='r', encoding='utf-8') as file:
        # Q2.データを読み取るためのオブジェクトを作成しよう
        reader = csv.???(file)
        print(f'{csv_file}の内容：')
        for row in reader:
            city_and_code.append(row)
            print(row)
    # Q3.取得したデータを格納したリストを返そう
    return ???

def get_weather(city_and_code, city):
    for i in range(len(city_and_code)):
        if city_and_code[i][0] == city:
            code = city_and_code[i][1]
            print(code)
    url = f'https://weather.tsukumijima.net/api/forecast?city={code}'
    response = requests.get(url)
    response.raise_for_status()    
    time.sleep(1)
    return response.json()

def save_json(json_data, city):
    json_file = f'./output/sample_{city}.json'
    # Q4.JSONファイルを保持した変数を指定しよう
    with open(???, mode='w', encoding='utf-8') as file:
        # Q5.データを書き込むためのメソッドを呼び出そう
        json.???(json_data, file, ensure_ascii=False, indent=4)

    print(f'取得した天気情報を{json_file}として保存しました')
    # Q6.新規作成したJSONファイルを返そう
    return ???

def read_json(json_file):
    with open(json_file, mode='r', encoding='utf-8') as file:
        # Q7.データを読み取るためのメソッドを呼び出そう
        data = json.???(file)
    print(f'{json_file}の内容：')
    print(f'{data["forecasts"][0]["date"]}の{data["title"]}をお知らせします．')
    print(f'天気：{data["forecasts"][0]["telop"]}')
    print(f'天気概況文：\n{data["description"]["text"]}')
    return data

if __name__ == '__main__':
    os.makedirs('./output', exist_ok=True)
    # Q8.input/city_and_code.csvに記録さている都市名に変更し，実行結果が変わることを確認しよう
    city = '秋田'
    csv_file = Path('./input/city_and_code.csv')
    city_and_code = read_csv(csv_file)
    json_data = get_weather(city_and_code, city)
    json_file = save_json(json_data, city)
    read_json(json_file)
