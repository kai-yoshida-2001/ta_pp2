#!/usr/bin/env python3

import re

# 電話番号形式の正規表現
pattern = re.compile(r'\d{3}-\d{4}')

# search()メソッドを使い，一致する最初の部分を見つける
match = pattern.search('連絡先は123-4567です．')
print('==========')
if match:
    print("searchメソッド()を使って見つけた番号：", '\n', match.group())

# findall()メソッドを使い，テキスト全体から一致するパターンを見つける
all_matches = pattern.findall('連絡先は123-4567か234-5678です．')
print('==========')
print("findall()メソッドを使って見つけた番号：", '\n', all_matches)

# sub()メソッドを使い，一致するパターンを別の文字列に置換する
new_text = pattern.sub('***-****', '連絡先は123-4567か234-5678です．')
print('==========')
print('sub()メソッドを使って置換（マスク）した文章：','\n', new_text)
