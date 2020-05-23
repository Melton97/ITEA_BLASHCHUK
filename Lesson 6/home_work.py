# 1) Создать консольную программу-парсер, с выводом прогноза погоды. Дать
# возможность пользователю получить прогноз погоды в его локации ( по
# умолчанию) и в выбраной локации, на определенную пользователем дату.
# Можно реализовать, как консольную программу, так и веб страницу.
# Используемые инструменты: requests, beatifulsoup, остальное по желанию.
# На выбор можно спарсить страницу, либо же использовать какой-либо API.

import requests
from bs4 import BeautifulSoup
import pprint
from tabulate import tabulate

URL = 'https://ua.sinoptik.ua/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'}

def get_html(url, params=None):
    
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_ = 'main')
    
    weather = []
    for item in items:
        
        weather.append({
            'day': item.find_all('p', class_ = 'date')[0].get_text(),
            'month': item.find_all('p', class_ = 'month')[0].get_text(),
            'temp_min': item.find_all('div', class_ = 'min')[-1].get_text(),
            'temp_max': item.find_all('div', class_ = 'max')[-1].get_text(),
            'text' : item.find_all('div', class_ = 'weatherIco')[0].get('title')
        })

    print(tabulate(weather))


def parse():
    
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)

    else: 
        print("ЧТо то не так!")

parse()