from bs4 import BeautifulSoup
import urllib.request
import json
import requests

url = 'https://news.yahoo.co.jp/topics'
ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) '\
    'AppleWebKit/537.36 (KHTML, like Gecko) '\
    'Chrome/77.0.3865.90 Safari/537.36 '

def getNews(word):
    req = urllib.request.Request(url, headers={'User-Agent': ua})
    html = urllib.request.urlopen(req)
    soup = BeautifulSoup(html, "html.parser")
    main = soup.find('div', attrs={'class': 'topicsMod'})
    topics = main.select("li > a")

    count = 0
    list = []

    for topic in topics:
        if topic.contents[0].find(word) > -1:
            list.append(topic.contents[0])
            list.append(topic.get('href'))
            count += 1
    if count == 0:
        list.append("記事が見つかりませんでした")

    result = '\n'.join(list)
    return result
