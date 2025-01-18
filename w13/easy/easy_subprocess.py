#!/usr/bin/env python3

import subprocess

def py_a():
    # Q1.subprocessを実行させよう
    process_a = ???.???(
        [
            'python', 'answer_datetime.py'
        ]
    )

    print('answer_datetime.pyをsubprocessで実行しました')
    print('-' * 5)

def py_b():
    # Q2.subprocessを実行させよう
    process_a = ???.???(
        [
            'python', 'answer_threading.py'
        ]
    )

    print('answer_threading.pyをsubprocessで実行しました')
    print('-' * 5)
    
if __name__ == '__main__':
    py_a()
    py_b()
