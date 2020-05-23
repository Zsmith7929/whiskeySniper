import requests
import time
import MySQLdb
from bs4 import BeautifulSoup

class Whiskey(object):
    def __init__(self, date="", sku=0, name="", allocated=False, quantity=0):
        self.date = date
        self.sku = sku
        self.name = name
        self.allocated = allocated
        self.quantity = quantity

def snipeKLWine(list: white_list):

    # Bourbon new feed
    r = requests.get("https://klwines.com/Products?&filters=sv2_NewProductFeedYN$eq$1$True$ProductFeed$!dflt-stock-all!206!4&limit=50&offset=0&orderBy=60%20asc,NewProductFeedDate%20desc&searchText=")
    bourbon_feed = BeautifulSoup(r.text, 'html.parser')
    rows = bourbon_feed.find("table", {"class": "table table-striped table-hover"}).find("tbody").find_all("tr")
    for row in rows:
        tmp = Whiskey()
        columns = row.find_all("td")
        tmp.date =





