#! /usr/bin/env python3

import re

text = "お問い合わせは010-2030-4050か，020-6070-8090まで．"

# Q1. 携帯電話番号形式の正規表現を設定しよう
phone_pattern = re.compile(r'\d{3}-\d{4}-\d{4}')

# Q2. textの中で，正規表現が適用される最初の部分を見つけよう
match = phone_pattern.search(text)
print("==========")
if match:
    print("見つかった番号：", match.group())

# Q3. textの中で，正規表現が適用される部分を全て見つけよう
all_matches = phone_pattern.findall(text)
print("==========")
print("見つかった全ての番号：", all_matches)

# Q4. 正規表現と一致する文字列を'###-####-####'に置換しよう
new_text = phone_pattern.sub('###-####-####', text)

# Q5. 置換前と置換後の文字列を出力して，違いを確かめよう
print("==========")
print('置換前の文章：', text)
print('置換後の文章：', new_text)
