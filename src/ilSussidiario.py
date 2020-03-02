from datetime import date
from utils import start_extraction, wait, scroll, get_soup, scanning_keywords
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import json
import datetime
from datetime import date
import time

path_to_chromedriver = "/home/francesco/Downloads/chromedriver"
url = "https://www.ilsussidiario.net"
LA_LISTA = ['ai', 'artificial' ,'tecnologia', 'educazione' , 'education',
            'scuola', 'gw', 'warming', 'global', 'warming',
            'digital', 'digitale', 'circolarità', 'sostenibilità', 'sostenibile',
             'edu' , 'energy' , 'energia' , 'rinnovabili', 'coronavirus',
             'corona', 'virus', 'messi']

def ilsussidiario_extract_keywords(url):
    step1 = url.lstrip('https://www.ilsussidiario.net/news/')
    step2 = ''.join(i for i in step1 if not i.isdigit())
    step3 = step2.rstrip('/').rstrip('amp').rstrip('//')
    keywords = step3.split('-')
    return keywords

def ilsussidiario_check_day(url):
    today = date.today()
    art_date = url.find('span',class_='date').get_text()
    print(art_date)
    return art_date == today.strftime("%d.%m.%Y")

def main():
    browser, soup = start_extraction(path_to_chromedriver, url)
    articles = []
    main_news = soup.find('div', class_='column flex article-content')

    if ilsussidiario_check_day(main_news):
        try:
            main_news_url = main_news.find('h3',class_="title flex").find('a').get('href')
            k1 = ilsussidiario_extract_keywords(main_news_url)
            if scanning_keywords(k1, LA_LISTA):
                print(k1)
                articles.append((main_news_url, k1))
        except:
            print('Notizia primaria non trovata')


    sec_news = soup.find('div', {"id":"home-page-section-4"}).find_all('div',class_='container flexbox column flex')
    print(sec_news)
    for n in sec_news:
        if ilsussidiario_check_day(n):
            try:
                url_sec = n.find('h3',class_="title flex").find('a').get('href')
                k2 = ilsussidiario_extract_keywords(url_sec)
                if scanning_keywords(k2, LA_LISTA):
                    print(k2)
                    articles.append((url_sec, k2))
            except:
                print('Notizia secondaria non trovata')

    other_news = soup.find('div', {"id":"home-page-section-6"}).find_all('div',class_='container flexbox column flex')
    print(other_news)
    for n in other_news:
        if ilsussidiario_check_day(n):
            try:
                url_oth = n.find('h3',class_="title flex").find('a').get('href')
                k3 = ilsussidiario_extract_keywords(url_oth)
                if scanning_keywords(k3, LA_LISTA):
                    print(k3)
                    articles.append((url_oth, k3))
            except:
                print('Notizia terziaria non trovata')
        else:
            print('Articolo non del giorno corrente')


    return articles

if __name__ == '__main__':
    articles = main()
    print(articles)
