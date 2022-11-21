import requests
from bs4 import BeautifulSoup
import sys


header = {
    'Accept-Language': 'en-US,en;q=0.5',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'
}


class PriceScraper:
    def __init__(self, url):
        try:
            self.amazon_html = requests.get(url, headers=header).text
        except requests.exceptions.MissingSchema:
            print('Bad Url!')
            sys.exit()
        self.current_price = 0
        self.item_name = ''
        self.url = url

    def get_price(self):
        global soup
        soup = BeautifulSoup(self.amazon_html, features='html.parser')
        whole_amount = soup.find(name='span', class_='a-price-whole').get_text().split('.')[0]
        fraction_amount = soup.find(name='span', class_='a-price-fraction').get_text()
        self.current_price += float(f'{whole_amount}.{fraction_amount}')
        return self.current_price

    def get_item_name(self):
        item_name = soup.find(name='span', id='productTitle').get_text().strip()
        self.item_name += item_name
        return self.item_name