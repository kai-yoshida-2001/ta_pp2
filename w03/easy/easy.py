#!/usr/bin/env python3

import pyinputplus as pyip

# Q1. 選択肢を'はい'か'いいえ'で設定しよう
text = '人を何時間も忙しくさせておく方法を知りたいですか？\n'
answer = pyip.input???(text, ???='はい', ???='いいえ')
if answer == 'はい':
    print('答えはまたの機会に...')
    print('===============')

# Q2. 指名入力の制限時間を'5'秒に設定しよう
text = '5秒以内に氏名を入力してください：'
try:
    name = pyip.inputStr(text, ???=5)
    print(f'{name}さん，こんにちは')
    print('===============')
# Q3. 5秒以上経過してしまった場合の処理を設定しよう
except pyip.???:
    print('5秒以上経過してしまいました...')
    print('===============')

# Q4. 数値入力を'整数'のみ受け付けるように設定しよう
text = '1~9の中で，好きな数字を入力してください：\n'
num1 = pyip.input???(text)
num2 = pyip.input???(text)
print(f'好きな数字の合計値は，{num1 + num2}です')
print('===============')

# Q5. 番号付きの選択肢を表示できるように設定しよう
breakfast = pyip.input???(('お米', 'パン', '麺類'),
                           prompt = '朝食に食べたいものを選んでください\n ',
                           ???=True)
print(f'朝食は{breakfast}に合うものをご用意しますね')
print('===============')
