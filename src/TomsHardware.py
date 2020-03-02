import datetime
from datetime import date
from selenium import webdriver
from bs4 import BeautifulSoup
from utils import start_extraction, wait, scroll, get_soup, scanning_keywords

path_to_chromedriver = "/home/francesco/Downloads/chromedriver"
url = "https://www.tomshw.it/"
LA_LISTA = ['ai', 'artificial' ,'tecnologia', 'educazione' , 'education',
            'scuola', 'gw', 'warming', 'global', 'warming',
            'digital', 'digitale', 'circolarità', 'sostenibilità', 'sostenibile',
             'edu' , 'energy' , 'energia' , 'rinnovabili', 'coronavirus',
             'corona', 'virus', 'messi', '2020']

def scraping():
    #Connessione al sito e tiro giù il codice della pagina
    global path_to_chromedriver, url
    driver, soup = start_extraction(path_to_chromedriver, url)
    row = 0
    articles = []

    #Estrazione elementi
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

    #Chiusura finestra chrome
    driver.close()
    return articles

def tomshw_main():
    articles = scraping()
    print(articles)
    return articles

if __name__ == "__main__":
    tomshw_main()
