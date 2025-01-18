#!/usr/bin/env python3

import threading, time

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
        time.sleep(2)

    print('-' * 5)
    print('タスクBが終了しました')
    print('-' * 5)
    
if __name__ == '__main__':
    num_a = 5
    num_b = 7

    # Q1.平行処理のためのスレッドを作成しよう
    thread_a = threading.???(target=???(num_a))
    thread_b = threading.???(target=???(num_b))

    # Q2.作成したスレッドを開始させよう
    thread_a.???()
    thread_b.???()

    # Q3.スレッドの終了を待機しよう
    thread_a.???()
    thread_b.???()

    print('全てのタスクが完了しました')
