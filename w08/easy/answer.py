#!/usr/bin/env python3

import os, shutil, zipfile, sys

source = './input'
output = './output'
unnecessary = './empty'

os.makedirs(output)
os.makedirs(unnecessary)
print('=====')

# 1.'shutil'モジュールによるファイルの操作
# ファイルのコピー
original = f'{source}/catnames.txt'
copy = f'{output}/cat_name_list.txt'

# Q1.'copy'メソッドを呼び出して，コピー元とコピー先を引数に指定しよう
shutil.copy(original, copy)
print(f'{original}を{copy}へ複製しました')
print('=====')

# ファイルの移動
here = f'{source}/spam.txt'
destination = f'{output}/spam.txt'

# Q2.'move'メソッドを呼び出して，移動元と移動先を引数に指定しよう
shutil.move(here, destination)
print(f'{here}から{destination}へ移動しました')
print('=====')

# Q3.'move'メソッドを呼び出して，Q2の移動元と移動先を逆に指定してみよう
shutil.move(destination, here)
print(f'{destination}から{here}へ戻しました')
print('=====')

# ディレクトリの削除
# Q4.'rmtree'メソッドを呼び出して，'unnecessary'を削除しよう
shutil.rmtree(unnecessary)
print(f'{unnecessary}を削除しました')
print('=====')

# 2.'zipfile'モジュールによるファイルの圧縮
zip_file_name = 'output/snapshot.zip'

# Q5.'ZipFile'メソッドを呼び出して，'zip_file_name'を引数に指定しよう
with zipfile.ZipFile(zip_file_name, 'w') as f:
    for root, dirs, files in os.walk(source):
        for file in files:
            file_path = f'{source}/{file}'
            f.write(file_path)
print(f'{zip_file_name}を作成しました')
print('=====')
