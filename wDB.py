#Whiskey Database Connector
import MySQLdb
import datetime
from Whiskey import Whiskey
import pickle

class DBC(object):
    def __init__(self):
        # load pickled credentials
        creds = pickle.load(open("k.p", "rb"))
        self.db = MySQLdb.connect(host=creds["host"],
                         user=creds["user"],
                         passwd=creds["passwd"],
                         db=creds["db"])
        self.cursor = db.cursor()

    def putWhiskey(self, w: Whiskey):
        return self.cursor.execute("INSERT INTO whiskey (sku, name, price, quantity, allocation, date) VALUES ({sku}, {name}, {price}, {quantity}, {allocation}, {date}) ON DUPLICATE KEY UPDATE date={newDate}".format(
            sku=w.sku,
            name=w.name,
            price=w.price,
            quantity=w.quantity,
            allocation=w.allocation,
            date=w.date,
            newDate=datetime.datetime.now()
        ))

    def commit(self):
        self.db.commit()


if __name__ == "__main__":
    pass



