# Version 1

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
try:
    def get_headlines(rss_url):
        driver.get(url = rss_url)
        # time.sleep(1)
        lst = []
        try:
            i = 2
            while True:
                title = driver.find_element(By.CSS_SELECTOR, f'#folder{i} > div.opened > div:nth-child(1) > span:nth-child(2)').text
                lst.append(title)
                i+=1
        except:
            print(f"There are {len(lst)} news")
        finally:
            driver.close()
            driver.quit()
        return lst
except Exception as ex:
    print(f"Error {ex}")
google_news_url = "https://news.google.com/rss"
headlines = get_headlines(google_news_url)
print(headlines)

# Version 2

import requests
from bs4 import BeautifulSoup

google_news_url="https://news.google.com/news/rss"


def get_headlines(rss_url):
    response = requests.get(url=rss_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find_all('title')
    title = list(title)
    title = [str(i)[7:-8] for i in title]
    return title
print(get_headlines(google_news_url))