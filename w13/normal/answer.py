#!/usr/bin/env python3

import datetime, threading, subprocess

def run_task(command, task_id):
    print(f"Task-{task_id}: Starting '{command}'")

    # Q1.システムの開始時点での日時を取得しよう
    start_time = datetime.datetime.now()

    # Q2.サブプロセスを実行させよう
    subprocess.run(command, shell=True)

    # Q3.システムの終了時点での日時を取得しよう
    end_time = datetime.datetime.now()

    duration = (end_time - start_time).total_seconds()
    print(f'Task-{task_id}: Finished in {duration:.2f} seconds')

if __name__ == '__main__':
    commands = [
        "echo 'Hello, World!'",
        "sleep 2",
        "echo 'Python is fun!'"
    ]

    threads = []
    for i, command in enumerate(commands):
        # Q4.スレッドを作成しよう
        thread = threading.Thread(target=run_task, args=(commands, i))
        threads.append(thread)
        # Q5.作成したスレッドを開始しよう
        thread.start()

    for thread in threads:
        # Q6.スレッドの終了を待機しよう
        thread.join()

    print('All tasks completed')
