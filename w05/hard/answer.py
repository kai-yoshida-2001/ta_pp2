#!/usr/bin/env python3

import pyinputplus as pyip
import re
import logging

logging.basicConfig(level=logging.INFO)

def get_phone_number():
    try:
        # Q1. pyinputplusを使ってStr型で受け付けるように設定しよう
        phone_number = pyip.inputStr("電話番号をXXX-XXXX-XXXXの形式で入力してください: ")

        # Q2. 正規表現を使って電話番号形式を設定しよう
        pattern = r"^\d{3}-\d{4}-\d{4}$"
        
        if not re.match(pattern, phone_number):
            raise ValueError("電話番号が指定された形式と一致しません")

        # Q3. 正しい形式で入力された場合のログを記録しよう
        logging.info(f"正しい形式の電話番号が入力されました: {phone_number}")
        return phone_number

    # Q4. 例外処理でValueErrorを設定しよう
    except ValueError as e:
        logging.error(f"入力エラー: {e}")
        return None

if __name__ == "__main__":
    logging.info("プログラムが開始されました")
    phone_number = get_phone_number()
    if phone_number:
        print(f"入力された電話番号: {phone_number}")
    else:
        print("適切な電話番号が入力されませんでした")
    logging.info("プログラムが終了しました")
