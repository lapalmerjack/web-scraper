import requests
from bs4 import BeautifulSoup


def save_articles(article_links: dict, page_number):
    titles = []
    for title, link in article_links.items():
        content = get_article(link)
        if content is not None:
            titles.append(title)
            parse_to_file(title, content, page_number)


def get_article(url: str):
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    article_teaser = soup.find('p', {'class': 'article__teaser'})
    if article_teaser:
        return article_teaser.get_text()
    else:
        return None


def parse_to_file(title, content, page_number):
    correct_directory = "Page_" + str(page_number) + "/" + title
    with open(correct_directory, "wb+") as c:
        c.write(content.encode())
    c.close()

