#!/usr/bin/env python3

import pyautogui, time

def auto_keyboard():
    time.sleep(3)
    # Q1.Terminal上に指定のテキストを書き込めるようにしよう
    pyautogui.???('echo Hello, World!', interval=0.1)
    # Q2.Enterキーを押すように設定しよう
    pyautogui.???('enter')

    # Q3.Terminal上に指定のテキストを書き込めるようにしよう
    # *カレントディレクトリが'~/pp2'に変化していることを確認しよう
    pyautogui.???('cd ~/pp2/', interval=0.1)
    # Q4.Enterキーを押すように設定しよう
    pyautogui.???('enter')
    
if __name__ == '__main__':
    auto_keyboard()
