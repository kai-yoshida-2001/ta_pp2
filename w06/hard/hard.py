#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pyinputplus as pyip

def fetch_news_results(keyword):
    options = Options()
    options.add_argument("--headless")
    # Q1. 'webdriver'に'chrome'ブラウザを設定しよう
    driver = ???.???(service=Service(ChromeDriverManager().install()), options=options)

    try:
        # Q2. 'driver'を設定しよう
        ???.get(f"https://www.google.com/search?q={keyword}+news")
        html = driver.page_source
    except Exception as e:
        print(f"Error during Selenium operation: {e}")
        return None
    finally:
        driver.quit()

    return html

def parse_news_results(html):
    # Q3. 'soup'変数に'BeautifulSoup'の設定を定義しよう
    soup = ???(html, "lxml")
    results = soup.select("div.tF2Cxc")
    if not results:
        raise ValueError("検索結果が見つかりませんでした。")

    extracted_results = []
    for result in results[:5]:
        title = result.select_one("h3").text
        link = result.select_one("a")["href"]
        extracted_results.append((title, link))
    return extracted_results

if __name__ == "__main__":
    # Q4. pyinputplusの'inputStr'メソッドを設定しよう
    keyword = pyip.???(prompt="検索したいニュースキーワードを入力してください: ")
    try:
        html = fetch_news_results(keyword)
        if html is None:
            # Q5. 'Exception'クラスを使ってカスタムメッセージを設定しよう
            raise ???("検索結果を取得できませんでした。")
        
        news_results = parse_news_results(html)
        print("\n--- 検索結果 ---")
        for i, (title, link) in enumerate(news_results, start=1):
            print(f"{i}. {title}\n   {link}")
            print('===')
    except Exception as e:
        print(f"エラー: {e}")
