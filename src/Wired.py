import datetime
from datetime import date
from selenium import webdriver
from bs4 import BeautifulSoup
from utils import start_extraction, wait, scroll, get_soup, scanning_keywords

path_to_chromedriver = "/home/francesco/Downloads/chromedriver"
url = "https://www.wired.it/"
LA_LISTA = ['ai', 'artificial' ,'tecnologia', 'educazione' , 'education',
            'scuola', 'gw', 'warming', 'global', 'warming',
            'digital', 'digitale', 'circolarità', 'sostenibilità', 'sostenibile',
             'edu' , 'energy' , 'energia' , 'rinnovabili', 'coronavirus',
             'corona', 'virus', 'messi', '2020']

def check_date_wired(url):
    try:
        only_date = url[url.index("2020"):url.index("2020")+10]
        good_date = only_date.replace("/","-")
        today = date.today()
        return today.strftime("%Y-%m-%d") == good_date
    except:
        return None

def scraping():
    #Connessione al sito e tiro giù il codice della pagina
    global path_to_chromedriver, url
    driver, soup = start_extraction(path_to_chromedriver, url)
    articles = []

    #Estrazione elementi
    for elem in soup.find_all("h3", class_="article-title"):
        url = ""

        try:
            url = elem.a["href"]
            print(url)
        except:
            continue

        if check_date_wired(url):
            keywords = str(elem.find("a").text.lower().strip()).split(" ")

            if scanning_keywords(LA_LISTA, keywords):
                articles.append((url, keywords))

    for elem in soup.find_all("p", class_="article-title"):
        url = ""

        try:
            url = elem.a["href"]
            print(url)
        except:
            continue

        if check_date_wired(url):
            keywords = str(elem.find("a").text.lower().strip()).split(" ")

            if scanning_keywords(LA_LISTA, keywords):
                articles.append((url, keywords))
    driver.close()
    return articles

def wired_main():
    articles = scraping()
    print(articles)
    return articles
    
if __name__ == "__main__":
    wired_main()
