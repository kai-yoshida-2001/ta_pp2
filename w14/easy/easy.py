#!/usr/bin/env python3

import pyautogui

def auto_mouse():
    # Q1.マウス（カーソル）を画面の（100, 100）の位置に移動させよう
    pyautogui.???(100, 100, duration=2)

    # Q2.クリックさせよう
    pyautogui.???()

    # Q3.マウス（カーソル）の現在地を取得しよう
    current_position = pyautogui.???()
    print(f'現在のマウス位置：{current_position}')

    # Q4.ドラッグ動作をさせてみよう
    pyautogui.???(200, 200, duration=2)

if __name__ == '__main__':
    auto_mouse()
