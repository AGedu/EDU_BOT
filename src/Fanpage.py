import datetime
from datetime import date
from selenium import webdriver
from bs4 import BeautifulSoup
from src.utils import start_extraction, wait, scroll, get_soup, scanning_keywords
import configparser

url = "https://www.fanpage.it/"

def check_date_fp(path_to_chromedriver, url):
    try:
        driver, article_soup = start_extraction(path_to_chromedriver, url)
        good_date = article_soup.find("time")["datetime"][:10]
        today = date.today()
        driver.close()
        return today.strftime("%Y-%m-%d") == good_date
    except:
        return None

def scraping(path_to_chromedriver, LA_LISTA):
    global url
    driver, soup = start_extraction(path_to_chromedriver, url)
    row = 0
    articles = []

    for elem in soup.find_all("div", class_="classh1 title-storyBox"):
        row += 1
        url = ""
        if row <= 10:
            try:
                url = elem.a["href"]
            except:
                pass

            if check_date_fp(path_to_chromedriver, url):
                keywords = str(elem.find("a").text.lower().strip()).split(" ")
                print(keywords)
                if scanning_keywords(LA_LISTA, keywords):
                    articles.append((url, keywords))

    for elem in soup.find_all("div", class_="classh2 title-storyBox"):
        row += 1
        url = ""
        if row <= 10:
            try:
                url = elem.a["href"]
            except:
                pass

            if check_date_fp(path_to_chromedriver, url):
                keywords = str(elem.find("a").text.lower().strip()).split(" ")
                print(keywords)
                if scanning_keywords(LA_LISTA, keywords):
                    articles.append((url, keywords))
    return articles
    driver.close()

def fanpage_main():
    config = configparser.ConfigParser()
    config.read('config/config.cfg')
    path_to_chromedriver = config['WebScraping']['WebBrowser']
    LA_LISTA = config["WebScraping"]["LA_LISTA"].split("\n")
    articles = scraping(path_to_chromedriver, LA_LISTA)
    print(articles)
    return articles

if __name__ == "__main__":
    fanpage_main()
