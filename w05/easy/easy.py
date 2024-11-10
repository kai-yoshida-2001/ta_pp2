#!/usr/bin/env python3

import logging

logging.basicConfig(level=logging.INFO)

print('=====')
# Q1. プログラムの開始をログに記録しよう
logging.???('プログラムが開始されました')
print('=====')

try:
    a = int(input('正の整数を入力してください'))
    b = int(input('正の整数を入力してください'))

    print('=====')
    result = a / b
    print(f'入力された数値の積は，{result}です')

# Q2. 正の整数以外が入力された場合の例外処理を記述しよう
except ???:
    print('=====')
    print("0で割ることはできません")

logging.info('例外処理が終わりました')

# Q3. assert文を使い，aとbが正の数でない場合に発生するエラーを設定しよう
def add_positive_assert(a, b):
    ???
    return a + b

# Q4. raise文を使い，aとbが正の数でない場合に発生するエラーを設定しよう
def add_positive_raise(a, b):
    ???
    ???
    return  a + b

print('=====')
print(f'assert文によるエラーチェックはクリアしました\n{add_positive_assert(a, b)}')
print(f'raise文によるエラーチェックはクリアしました\n{add_positive_raise(a, b)}')

print('==========')

# Q5. 全ての処理が終わったことを記録しよう
logging.???('プログラム終了しました')
