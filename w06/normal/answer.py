#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import requests

def google_search_scraper(keyword, num_results=5):
    # キーワードでGoogle検索（Seleniumを使用）
    search_url = f'https://www.google.com/search?q={keyword}'
    options = Options()
    options.add_argument('--headless')
    service = Service(ChromeDriverManager().install())
    # Q1. 'webdriver'に'chrome'ブラウザを設定しよう
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        # Q2. 'driver'に'search_url'を設定しよう
        driver.get(search_url)
        html = driver.page_source
    finally:
        driver.quit()

    # BeautifulSoupでHTML解析
    soup = BeautifulSoup(html, 'lxml')
    # Q3. 'soup'で'select'するタグを'div'に設定しよう
    search_results = soup.select('div.tF2Cxc')

    # 結果を保存
    results = []
    for result in search_results[:num_results]:
        title = result.select_one('h3').text if result.select_one('h3') else 'No Title'
        link = result.select_one('a')['href'] if result.select_one('a') else 'No Link'
        results.append({'title': title, 'link': link})

    return results

# 実行例
if __name__ == '__main__':
    # 'keyword'変数に格納する単語を変更して，実行結果が変わることを確認しよう
    keyword = 'Python Web Scraping'
    results = google_search_scraper(keyword)

    print('Google検索結果:')
    for i, result in enumerate(results, start=1):
        print('===')
        print(f"{i}. {result['title']} ({result['link']})")
