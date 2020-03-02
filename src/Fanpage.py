import datetime
from datetime import date
from selenium import webdriver
from bs4 import BeautifulSoup
from utils import start_extraction, wait, scroll, get_soup, scanning_keywords

path_to_chromedriver = "/home/francesco/Downloads/chromedriver"
url = "https://www.fanpage.it/"
LA_LISTA = ['ai', 'artificial' ,'tecnologia', 'educazione' , 'education',
            'scuola', 'gw', 'warming', 'global', 'warming',
            'digital', 'digitale', 'circolarità', 'sostenibilità', 'sostenibile',
             'edu' , 'energy' , 'energia' , 'rinnovabili', 'coronavirus',
             'corona', 'virus', 'messi']


def check_date_fp(url):
    try:
        driver, article_soup = start_extraction(path_to_chromedriver,url)
        good_date = article_soup.find("time")["datetime"][:10]
        today = date.today()
        driver.close()
        return today.strftime("%Y-%m-%d") == good_date
    except:
        return None

def scraping():
    #Connessione al sito e tiro gù il codice della pagina
    global path_to_chromedriver, url
    driver, soup = start_extraction(path_to_chromedriver, url)
    row = 0
    articles = []

    #Estrazione_elementi
    for elem in soup.find_all("div", class_="classh1 title-storyBox"):
        row += 1
        url = ""
        if row <= 10:
            try:
                url = elem.a["href"]
            except:
                continue

            if check_date_fp(url):
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
                continue

            if check_date_fp(url):
                keywords = str(elem.find("a").text.lower().strip()).split(" ")
                print(keywords)
                if scanning_keywords(LA_LISTA, keywords):
                    articles.append((url, keywords))
    return articles
    #Chiusura finestra chrome
    driver.close()

def fanpage_main():
    articles = scraping()
    print(articles)
    return articles

if __name__ == "__main__":
    fanpage_main()
