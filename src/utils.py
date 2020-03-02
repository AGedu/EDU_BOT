import time
from bs4 import BeautifulSoup
from selenium import webdriver


def get_soup(browser):
    html_source = browser.page_source
    soup=BeautifulSoup(html_source,"html.parser")
    return soup

def scroll(browser, num_volte, num_px):
    for i in range(1,num_volte,1):
        browser.execute_script("window.scrollTo(0, %s);" % (num_px*i))
        time.sleep(2)

def wait(time_to_wait):
    print ('Calm down, i am waiting:', end=' ')
    for i in range(0,time_to_wait,1):
        print (time_to_wait-i, end=',')
        time.sleep(1)
    print ('0')

def start_extraction(driver,url):
    browser = webdriver.Chrome(executable_path = driver)
    browser.maximize_window()
    wait(2)
    browser.get(url)
    soup = get_soup(browser)
    return browser, soup

def scanning_keywords(magic_list, keywords):
    return list(set(magic_list) & set(keywords)) != []
