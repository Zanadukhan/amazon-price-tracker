from price_scraper import PriceScraper
from mail import SendMail
import schedule
import time


url = input('Please copy and paste desired item link here: ')
info_scraper = PriceScraper(url)

item_name = info_scraper.get_item_name()
target_price = float(input("What's the lowest price that you're willing to pay for this item? $"))
send_mail = SendMail()

def discount_check():
    item_price = info_scraper.get_price()
    if item_price <= target_price:
        send_mail.send_new_mail(item_name, item_price, url)
        print('email sent')

schedule.every().day.at('20:30').do(discount_check)

while True:
    schedule.run_pending()
    time.sleep(60)

discount_check()



