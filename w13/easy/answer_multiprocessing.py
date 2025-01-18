#!/usr/bin/env python3

from multiprocessing import Process
import time

def task_a(num_a):
    for i in range(num_a):
        print(f'タスクAを実行中：{i + 1}')
        time.sleep(1)

    print('-' * 5)
    print('タスクAが終了しました')
    print('-' * 5)

def task_b(num_b):
    for i in range(num_b):
        print(f'タスクBを実行中：{i + 1}')
        time.sleep(1.5)

    print('-' * 5)
    print('タスクBが終了しました')
    print('-' * 5)

if __name__ == '__main__':
    num_a = 7
    num_b = 8

    # Q1.並列で実行するプロセスを作成しよう
    process_a = Process(target=task_a(num_a))
    process_b = Process(target=task_b(num_b))

    # Q2.プロセスを開始させよう
    process_a.start()
    process_b.start()

    # Q3.プロセスの終了を待機させよう
    process_a.join()
    process_b.join()

    print('すべてのタスクが完了しました')
