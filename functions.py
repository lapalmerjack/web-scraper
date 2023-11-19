import re


def get_links(soup, article_type):
    articles_and_links = {}
    for article in soup.find_all('article'):
        if get_proper_links(article, article_type):
            link = article.find('a', {'data-track-action': 'view article'})
            article_link = format_links(link['href'])
            title = format_string(link.get_text())
            articles_and_links[title] = article_link

    return articles_and_links


def get_proper_links(article, article_type):
    right_article = article.find('span', {'data-test': 'article.type'})
    return right_article.get_text() == article_type


def format_string(article_string: str):
    no_blanks = article_string.replace(" ", "_")
    symbols_removed = re.sub(r'[^a-zA-Z0-9\'_]', '', no_blanks)

    return symbols_removed + ".txt"


def format_links(link):
    return "https://www.nature.com" + link


