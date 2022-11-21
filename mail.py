import smtplib, ssl
from price_scraper import PriceScraper
EMAIL = YOUR_EMAIL_HERE
PASSWORD = YOUR_EMAIL_PASSWORD_HERE
SMTP_SERVER = 'smtp-mail.outlook.com'
PORT = 587
header = """Subject: Amazon Item on sale!!
"""


class SendMail:
    def __init__(self):
        self.context = ssl.create_default_context()

    def send_new_mail(self, item_name, price, url):
        message = header + '\n' + f'{item_name} are now ${price}\n\n' \
                                  f'{url}!!!!'
        with smtplib.SMTP(SMTP_SERVER, PORT) as server:
            server.starttls(context=self.context)
            server.login(EMAIL, PASSWORD)
            server.sendmail(EMAIL, EMAIL, message)


