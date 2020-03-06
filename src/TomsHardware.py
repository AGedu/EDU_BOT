import datetime
from datetime import date
from selenium import webdriver
from bs4 import BeautifulSoup
from src.utils import start_extraction, wait, scroll, get_soup, scanning_keywords
import configparser
import configparser

url = "https://www.tomshw.it/"


def scraping(path_to_chromedriver, LA_LISTA):
    global url
    driver, soup = start_extraction(path_to_chromedriver, url)
    row = 0
    articles = []

    for elem in soup.find_all("div", class_="item_short_desc"):
        today = date.today()

        try:
            article_date = elem.meta['content']
        except:
            article_date = "YYYY-mm-dd"

        row += 1
        if today.strftime("%Y-%m-%d") == article_date and row <= 10:
            keywords = []
            keywords = str(elem.find("a", class_="_force_url").text).lower().split(" ")
            print(keywords)
            if scanning_keywords(LA_LISTA, keywords):
                articles.append((elem.h3.a["href"], keywords))

    driver.close()
    return articles

def tomshw_main():
    config = configparser.ConfigParser()
    config.read('config/config.cfg')
    path_to_chromedriver = config['WebScraping']['WebBrowser']
    LA_LISTA = config['WebScraping']['LA_LISTA'].split("\n")
    articles = scraping(path_to_chromedriver, LA_LISTA)
    print(articles)
    return articles

if __name__ == "__main__":
    tomshw_main()
