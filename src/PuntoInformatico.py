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
url = "https://www.punto-informatico.it"
LA_LISTA = ['ai', 'artificial' ,'tecnologia', 'educazione' , 'education',
            'scuola', 'gw', 'warming', 'global', 'warming',
            'digital', 'digitale', 'circolarità', 'sostenibilità', 'sostenibile',
             'edu' , 'energy' , 'energia' , 'rinnovabili', 'coronavirus',
             'corona', 'virus', 'messi']

def puntoinformatico_get_news(soup):
    news = []
    all_sections = soup.find_all('section', class_='section-news-list')
    for n in range(len(all_sections)):
        splitted_sections = all_sections[n].find_all('a')
        for m in range(len(splitted_sections)):
            if not splitted_sections[m].get('href').find('https://www.punto-informatico.it/'):
                news.append(splitted_sections[m].get('href'))
    return news


def puntoinformatico_check_day(soup):
    today = date.today()
    article_date = soup.find("span", class_='time').get('date-postdate').split(' ')
    return article_date[0] == today.strftime("%Y-%m-%d")


def puntoinformatico_extract_keywords(browser, soup):
    keywords_soup = soup.find('script', class_="yoast-schema-graph yoast-schema-graph--main").get_text()
    res = json.loads(keywords_soup)
    # k1 = res['@graph'][4]['keywords'].split(',')
    k2 = res['@graph'][3]['url'].lstrip('https://www.punto-informatico.it/').rstrip('/').split('-')
    lw = res['@graph'][3]['name'].replace(':', '').split(' ')
    k3 = [lw[w].lower() for w in range(len(lw)) if list(lw[w])[0].isupper()]
    keywords = k2 + k3
    return keywords


def puntoinformatico_main():
    browser, soup = start_extraction(path_to_chromedriver, url)
    news = puntoinformatico_get_news(soup)
    browser.close()
    articles = []
    for n in news:
        browser, soup = start_extraction(path_to_chromedriver, n)
        if puntoinformatico_check_day(soup):
            keywords = puntoinformatico_extract_keywords(browser, soup)
            if scanning_keywords(LA_LISTA, keywords):
                articles.append((n, keywords))
        browser.close()
    print(articles)
    return(articles)


if __name__ == '__main__':
    puntoinformatico_main()
