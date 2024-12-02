#!/usr/bin/env python3

import os,  zipfile
from datetime import datetime
from pathlib import Path

def create_snapshot(dir_input):
    dir_output = './output'
    # Q1.'Path'オブジェクトを生成し，引数に'dir_output'を指定しよう
    output_path = ???(???)
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    snapshot_name = f'snapshot_{timestamp}.zip'

    # Q2.'output_path'と'snapshot'を結合したパスを設定しよう
    snapshot_path = ??? / ???

    # Q3.'ZipFile'引数に，スナップショットのパスを指定しよう
    with zipfile.???(???, 'w') as f:
        for root, _, files in os.walk(dir_input):
            for file in files:
                # Q4.'Path'オブジェクトを生成し，引数には'root'を指定しよう
                file_path = ???(???) / file
                f.write(file_path)

    print(f'スナップショットを作成しました：{snapshot_path}')

    snapshots = sorted(output_path.glob('snapshot_*.zip'))
    if len(snapshots) > 2:
        oldest_snapshot = snapshots[0]
        oldest_snapshot.unlink()
        print(f'古いスナップショットを削除しました：{oldest_snapshot}')

if __name__ == '__main__':
    dir_input = './input/'
    create_snapshot(dir_input)
