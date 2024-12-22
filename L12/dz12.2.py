class Item:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"{self.name}, price: {self.price}, description: {self.description}, dimensions: {self.dimensions}"


class User:
    def __init__(self, name, surname, phone_number):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number

    def __str__(self):
        return f"{self.name} {self.surname}, phone: {self.phone_number}"


class Purchase:
    def __init__(self, user):
        self.user = user
        self.products = {}

    def add_item (self, item, quantity):
        if item in self.products:
            self.products[item] += quantity
        else:
            self.products[item] = quantity

    def get_total(self):
        total = sum(item.price * quantity for item, quantity in self.products.items())
        return total

    def __str__(self):
        items_str = "\n".join(f"{item.name}: {quantity} pcs." for item, quantity in self.products.items())
        return f"User: {self.user}\nItems:\n{items_str}\nTotal: {self.get_total()}"

lemon = Item('lemon', 5, "yellow", "small", )
apple = Item('apple', 2, "red", "middle", )
print(lemon)  # lemon, price: 5

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)  # Ivan Ivanov

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 20 pcs.
"""
assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
assert cart.get_total() == 60, 'Повинно залишатися 60!'

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 10)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 10 pcs.
"""

assert cart.get_total() == 40