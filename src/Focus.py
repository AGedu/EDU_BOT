import datetime
from datetime import date
from selenium import webdriver
from bs4 import BeautifulSoup
from utils import start_extraction, wait, scroll, get_soup, scanning_keywords

path_to_chromedriver = "/home/francesco/Downloads/chromedriver"
url = "https://www.focus.it/"
LA_LISTA = ['ai', 'artificial' ,'tecnologia', 'educazione' , 'education',
            'scuola', 'gw', 'warming', 'global', 'warming',
            'digital', 'digitale', 'circolarità', 'sostenibilità', 'sostenibile',
             'edu' , 'energy' , 'energia' , 'rinnovabili', 'coronavirus',
             'corona', 'virus', 'messi']

def check_date_focus(url):
    global path_to_chromedriver
    driver, article_soup = start_extraction(path_to_chromedriver,url)
    data = article_soup.find("div", class_="AFirma")
    stringa = str(data.text).strip()
    driver.close()
    only_date = stringa[:stringa.index("2020")+4]
    data_lista = only_date.split(" ")

    switcher = {
        "gennaio": "01",
        "febbraio": "02",
        "marzo": "03",
        "aprile": "04",
        "maggio": "05",
        "giugno": "06",
        "luglio": "07",
        "agosto": "08",
        "settembre": "09",
        "ottobre": "10",
        "novembre": "11",
        "dicembre": "12"
    }

    stringa_data = data_lista[2] + "-" + switcher.get(data_lista[1]) + "-" + data_lista[0]

    return stringa_data

def scraping():
    #Connessione al sito e tiro giù il codice della pagina
    global path_to_chromedriver, url
    driver, soup = start_extraction(path_to_chromedriver, url)
    articles = []

    for elem in driver.find_elements_by_css_selector("a[class^='EvidImg']"):

        elem_url_link = str(elem.get_attribute("href"))
        today = date.today()
        if today.strftime("%Y-%m-%d") == check_date_focus(elem_url_link):
            #Prende i caratteri dopo l'ultimo "/"
            only_keywords = elem_url_link[elem_url_link.rindex("/")+1:]
            #Split delle parole e inserite in una lista
            lista_parole = only_keywords.split("-")
            print(lista_parole)

            if scanning_keywords(LA_LISTA, lista_parole):
                articles.append((elem_url_link, lista_parole))

    for elem in driver.find_elements_by_css_selector("a[class^='AListImg']"):

        elem_url_link = str(elem.get_attribute("href"))
        today = date.today()
        if today.strftime("%Y-%m-%d") == check_date_focus(elem_url_link):
            #Prende i caratteri dopo l'ultimo "/"
            only_keywords = elem_url_link[elem_url_link.rindex("/")+1:]
            #Split delle parole e inserite in una lista
            lista_parole = only_keywords.split("-")
            print(lista_parole)

            if scanning_keywords(LA_LISTA, lista_parole):
                articles.append((elem_url_link, lista_parole))
    return articles
    #Chiusura finestra chrome
    driver.close()

def focus_main():
    articles = scraping()
    print(articles)
    return articles

if __name__ == "__main__":
    focus_main()
