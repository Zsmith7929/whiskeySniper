class Whiskey(object):
    def __init__(self, date="", sku=0, name="", allocated=False, quantity=0, price="0.00"):
        self.date = date
        self.sku = sku
        self.name = name
        self.allocated = allocated
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return "Date: {date}, SKU: {sku}, Name: {name}, Allocated: {allocated}, Price: {price}, Quantity: {quantity}".format(
            date=self.date,
            sku=self.sku,
            name=self.name,
            allocated=self.allocated,
            price=self.price,
            quantity=self.quantity)

    def __hash__(self):
        return self.sku

    def __eq__(self, other):
        return self.sku == other.sku