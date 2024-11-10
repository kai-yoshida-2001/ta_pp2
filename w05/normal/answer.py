#!/usr/bin/env python3

import logging

logging.basicConfig(level=logging.INFO)

# Q1. プログラムの開始をログに記録しよう
logging.info("プログラムが開始されました")

def get_positive_integer():
    try:
        value = int(input("正の整数を入力してください: "))
        
        if value <= 0:
            # Q2. raise文を使い，valueが正の整数でない場合のエラーを設定しよう
            raise ValueError("入力値は正の整数でなければなりません")
        
        logging.info(f"入力された正の整数: {value}")
        return value

    # Q3. 例外処理を実行する場合にエラーログを記録する設定しよう
    except ValueError as e:
        logging.error(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    get_positive_integer()
    # Q4. 全工程が終了したことを記録しよう
    logging.info("プログラムが終了しました")
