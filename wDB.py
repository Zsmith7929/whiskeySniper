#Whiskey Database Connector
import MySQLdb
import datetime
import pickle

class DBC(object):
    def __init__(self):
        self.db = MySQLdb.connect(host="smith7929.mysql.pythonanywhere-services.com",
                         user="smith7929",
                         passwd="I@mthe1whoknocks",
                         db="smith7929$whiskey")
        self.cursor = db.cursor()

    def putWhiskey(self, w):
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



