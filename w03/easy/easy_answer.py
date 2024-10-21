#!/usr/bin/env python3

import pyinputplus as pyip

# Q1. 選択肢を'はい'か'いいえ'で設定しよう
text = '人を何時間も忙しくさせておく方法を知りたいですか？\n'
answer = pyip.inputYesNo(text, yesVal='はい', noVal='いいえ')
if answer == 'はい':
    print('答えはまたの機会に...')
    print('===============')

# Q2. 指名入力の制限時間を'5'秒に設定しよう
text = '5秒以内に氏名を入力してください：'
try:
    name = pyip.inputStr(text, timeout=5)
    print(f'{name}さん，こんにちは')
    print('===============')
except pyip.TimeoutException:
    print('5秒以上経過してしまいました...')
    print('===============')

# Q3. 数値入力を'整数'のみ受け付けるように設定しよう
text = '1~9の中で，好きな数字を入力してください：\n'
num1 = pyip.inputInt(text)
num2 = pyip.inputInt(text)
print(f'好きな数字の合計値は，{num1 + num2}です')
print('===============')

# Q4. 番号付きの選択肢を表示できるように設定しよう
breakfast = pyip.inputMenu(('お米', 'パン', '麺類'),
                           prompt = '朝食に食べたいものを選んでください\n ',
                           numbered=True)
print(f'朝食は{breakfast}に合うものをご用意しますね')
print('===============')
