from src.utils import start_extraction, wait, scroll, get_soup, scanning_keywords
from datetime import date
import configparser

url = "https://www.repubblica.it"

def extract_keywords(browser, soup):
    try:
        tags_index = browser.find_element_by_name("keywords")
        tags = tags_index.get_attribute("content").split(',')
    except:
        print('No tags found for this article')
        tags = []
    try:
        description_index = browser.find_element_by_name("description")
        description = description_index.get_attribute("content").split(' ')
    except:
        print('No description found for this article')
        description = []
    title = soup.find("title").get_text().split(' ')
    keywords = tags + description + title
    return keywords


def check_day_of_publication(soup):
    today = date.today()
    try:
        article_date = soup.find("time").get("datetime")
    except:
        print('No date found for this article')
        article_date = []
    return article_date == today.strftime("%Y-%m-%d")


def get_news(soup):
    try:
        news = avoid_duplicates([soup.find_all('h2',
                                           class_='entry-title')[n].find('a').get('href') for n in range(4)])
    except:
        print('Cannot find news')
        news = []
    return news


def avoid_duplicates(news):
    cleaned_news = list(set(news))
    return cleaned_news


def larepubblica_main():
    config = configparser.ConfigParser()
    config.read('config/config.cfg')
    path_to_chromedriver = config['WebScraping']['WebBrowser']
    LA_LISTA = config['WebScraping']['LA_LISTA'].split("\n")
    browser, soup = start_extraction(path_to_chromedriver, url)
    news = get_news(soup)
    browser.close()
    articles = []
    for n in news:
        browser, soup = start_extraction(path_to_chromedriver, n)
        if check_day_of_publication(soup):
            keywords = extract_keywords(browser, soup)
            print(keywords)
            if scanning_keywords(LA_LISTA, keywords):
                articles.append((n, keywords))
        browser.close()
    print(articles)
    return articles


if __name__ == '__main__':
    larepubblica_main()
