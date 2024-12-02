#!/usr/bin/env python3

import os, re, shutil
from pathlib import Path
from zipfile import ZipFile

def files_sort(input_dir, dir_output):
    # Q1.'Path'オブジェクトを生成して，それぞれのディレクトリを引数に指定しよう
    input_path = ???(???)
    output_path = ???(???)

    output_path.mkdir(exist_ok=True)

    for file in input_path.iterdir():
        if file.is_file():
            # Q2.'re'モジュールの'search'メソッドを呼び出そう
            match = ???.???(r'\.(\w+)$', file.name)
            if match:
                ext = match.group(1)
                ext_dir = output_path / ext
                ext_dir.mkdir(exist_ok=True)
                # Q3.'shutil'モジュールの'copy'メソッドを呼び出そう
                ???.???(file, ext_dir / file.name)
                print(f'===\nCopied {file.name} to {ext_dir}')

    for ext_dir in output_path.iterdir():
        if ext_dir.is_dir():
            zip_file = output_path / f'{ext_dir.name}.zip'
            # Q4.'ZipFile'メソッドを呼び出して，'zip_file'を引数に指定しよう
            with ???(???, 'w') as f:
                for file in ext_dir.iterdir():
                    f.write(file, arcname=file.name)

            print(f'===\nCompressed {ext_dir} into {zip_file}')

if __name__ == '__main__':
    input_dir = './input'
    output_dir = './output'

    files_sort(input_dir, output_dir)
