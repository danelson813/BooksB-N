# BooksB&N/helpers/helpers.py

from bs4 import BeautifulSoup as bs
from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service


def get_soup(url):
    service = Service()
    options = Options()
    options.add_argument('--incognito')
    options.add_argument('start-maximized')
    options.add_argument('--headless')
    driver = webdriver.Firefox(service=service, options=options)
    time.sleep(5)
    driver.get(url)
    # driver.save_screenshot("first_ss.png")
    time.sleep(3)
    soup = bs(driver.page_source, 'html.parser')
    time.sleep(2)
    driver.close()
    return soup


def parse_books(books, finished_list):
    for book in books:
        base = "https://www.barnesandnoble.com"
        results = {}
        results['title'] = book.find('h3', class_='product-info-title').text.strip()
        results['author'] = book.find('div', class_='product-shelf-author').text
        results['price'] = book.find("span", class_='current').text
        results['format'] = book.find('td', class_='format').text
        results['link'] = base + book.find('h3', class_='product-info-title').find('a').get('href')
        finished_list.append(results)
    return finished_list