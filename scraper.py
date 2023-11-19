import os
import sys

import requests
from bs4 import BeautifulSoup
from exceptions import LinkNotValid, WrongCode
import functions
import articlewriter


def check_link_name(link: 'str'):
    try:
        parts = link.split('/')

        if 'articles' not in parts or 'nature.com' not in str(parts):
            raise LinkNotValid

    except LinkNotValid:
        print("Invalid page!")
        sys.exit(1)


def check_status_code(code):
    try:
        if code != 200:
            raise WrongCode
    except WrongCode:
        print(f"The URL returned {code}")
        sys.exit(1)


def get_all_proper_articles(number_of_pages, article_genre):
    for page in range(1, number_of_pages + 1):
        try:
            os.mkdir("Page_" + str(page))
            url = "https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=" + str(page)
            response = requests.get(url)
            check_status_code(response.status_code)
            content = response.content
            soup = BeautifulSoup(content, 'html.parser')
            article_links = functions.get_links(soup, article_genre)
            articlewriter.save_articles(article_links, page)

        except requests.exceptions.HTTPError as e:
            print("Invalid page!")


page_numbers = int(input('input pages numbers '))
article_type = input('please enter article type ')
get_all_proper_articles(page_numbers, article_type)
print('Saved all articles.')
