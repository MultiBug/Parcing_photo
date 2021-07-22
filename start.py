from urllib.request import *
from bs4 import BeautifulSoup

url = 'https://micropic.ru'


def get_html(url):
    req = Request(url)
    html = urlopen(req).read()
    return html


def main():
    opener = build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
    install_opener(opener)
    html = get_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    list = soup.find_all(class_='rekl_block big_block')
    print(list)


main()
