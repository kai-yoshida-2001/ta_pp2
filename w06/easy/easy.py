#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# 1. requests/bs4モジュールによるHTMLの取得と解析
url = 'https://www.cps.akita-pu.ac.jp/'
response = requests.get(url)
# Q1. テキスト情報を取得するために'BeautifulSoup'を指定しよう
soup = ???(response.text, 'lxml')
# Q2. 取得したテキストの中から'title'を取得しよう
title = ???.???.string
print(f'このページのタイトルは：{title}，です')
print('===')

# 2. seleniumモジュールによるブラウザの操作
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Q3. 'driver'に'url'を設定しよう
???.???(url)

driver.save_screenshot('./screenshot.png')
print(f"スクリーンショットを保存しました")
# 3秒間，処理を停止します
time.sleep(3)

# Q4. ブラウザを閉じるように設定しよう
driver.???()

# 3. 画像サイトから所望の画像をダウンロードするプログラム
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
# Q5. 'soup'を使って画像（img）情報を取得しよう
img_url = ???.???('???')['src']
with open('image.jpg', 'wb') as file:
    file.write(requests.get(img_url).content)
