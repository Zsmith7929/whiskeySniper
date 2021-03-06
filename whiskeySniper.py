import requests
import MySQLdb
import datetime
from bs4 import BeautifulSoup
from Whiskey import Whiskey

def snipeKLWine():
    # Bourbon new feed
    r = requests.get("https://klwines.com/Products?&filters=sv2_NewProductFeedYN$eq$1$True$ProductFeed$!dflt-stock"
                     "-all!206!4&limit=50&offset=0&orderBy=60%20asc,NewProductFeedDate%20desc&searchText=")
    bourbon_feed = BeautifulSoup(r.text, 'html.parser')
    rows = bourbon_feed.find("table", {"class": "table table-striped table-hover"}).find("tbody").find_all("tr")
    whiskeys = set()
    for row in rows:
        tmp = Whiskey()
        columns = row.find_all("td")
        # Column [2] is vintage; we won't use that
        tmp.date = datetime.datetime.strptime(columns[0].text, '%m/%d/%Y %I:%M %p')
        tmp.sku = columns[1].text.strip()
        tmp.name = columns[3].text.strip()
        tmp.allocated = 1 if row.find("span") else 0
        tmp.price = columns[4].text
        tmp.quantity = 0 if columns[5].text == "Sold Out" else columns[5].text
        whiskeys.add(tmp)

    # Bourbon new/back in stock
    r = requests.get("https://klwines.com/Products?&filters=sv2_90$eq$1$True$ff-90-1--$!206!4&limit=50&offset=0"
                     "&orderBy=60%20asc,search.score()%20desc&searchText=")
    bourbon_feed = BeautifulSoup(r.text, 'html.parser')
    rows = bourbon_feed.find("div", {"class": "results-block clearfix"}).find_all("div",
                                                                                  {"class": "tf-product clearfix"})
    for row in rows:
        tmp = Whiskey()
        tmp.price = row.find("div", {"class": "tf-product-addon"}).find("span", {"class": "global-pop-color"}).text
        tmp.name = row.find("div", {"class": "tf-product-header"}).find("a").text.strip()
        tmp.sku = row.find("div", {"class": "tf-button"}).find("button").get("data-app-insights-track-search-doc-id")
        tmp.date = datetime.datetime.now()
        tmp.allocated = (1 if row.find("div", {"class": "tf-product-addon"}).find("div", {
            "class": "global-serif global-pop-color allocation"}) else 0)
        tmp.quantity = 0
        whiskeys.add(tmp)

    return whiskeys


if __name__ == "__main__":
    whiskeys = snipeKLWine()

    for w in whiskeys:
        print(w)
