class ShoppingCart(object):
    def __init__(self):
        self.total = 0
        self.items = {}

    def add_item(self, item_name, quantity, price):
        self.total += quantity * price
        if type(item_name) == str and quantity > 0:
            self.items.update({item_name: quantity})

    def remove_item(self, item_name, quantity, price):
        if quantity >= self.items[item_name] and quantity >= 1:
            items_cost = price * self.items[item_name]
            self.total -= items_cost
            del self.items[item_name]
        else:
            self.total -= quantity * price
            self.items[item_name] -= quantity

    def checkout(self, cash_paid):
        balance = 0
        if cash_paid < self.total:
            return "Cash paid not enough"
        balance = cash_paid - self.total
        return balance


class Shop(ShoppingCart):
    def __init__(self):
        self.quantity = 100

    def remove_item(self):
        self.quantity -= 1
