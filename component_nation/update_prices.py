#for scraping price from amazon
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
import locale
import logging


locale.setlocale(locale.LC_MONETARY, 'en_IN')



def init_selenium():
    CHROME_PATH = '/usr/bin/google-chrome-stable'
    CHROMEDRIVER_PATH = '/usr/bin/chromedriver'
    WINDOW_SIZE = "1920,1080"
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
    chrome_options.binary_location = CHROME_PATH
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,chrome_options=chrome_options)
    return driver


def fetch_prices(data):
    
    urls=[]
    prices=[]
    # for item in data:
    #     urls.append(item.url)
    print("abcdefgh")
    for item in data:
        url=item.url
        print(url)
        driver=init_selenium()
        driver.get(url)

        soup = BeautifulSoup(driver.page_source, "html.parser")

        try:
            price_row = soup.find(id="priceblock_ourprice_row")
            if(price_row==None):
                price_row = soup.find(id="priceblock_dealprice_row")
                prices.append(price_row.find(class_="a-size-medium a-color-price priceBlockDealPriceString").get_text())
            else:
                prices.append(price_row.find(class_="a-size-medium a-color-price priceBlockBuyingPriceString").get_text())
        except:
            prices.append(item.price)
            print("price not updated")
            logging.exception(IndexError)
            


        driver.close()

    return prices

def total(data):
    total=0
    for item in data:
        if(item.product=="Adata XPG D30 16GB 3000Mhz DDR4 (Qt.2)"):
            total = total + int(re.sub("[^0-9]","",item.price))
            total = total + int(re.sub("[^0-9]","",item.price))
        else:
            total = total + int(re.sub("[^0-9]","",item.price))
    # total="{:,}".format(total)
    total=locale.currency(total, grouping=True)

    return total
