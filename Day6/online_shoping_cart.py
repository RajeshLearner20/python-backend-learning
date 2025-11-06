class product:

    def __init__(self,name,price):
        self.name = name
        self.price = price

class Cart:

    def __init__(self):
        self.__items = []

    def add_item(self,product):
        self.__items.append(product)

    def total(self):
        return sum(item.price for item in self.__items)

p1 = product("Mouse",300)
p2 = product("Key board",200)

cart = Cart()
cart.add_item(p1)
cart.add_item(p2)

print(f"Total: {cart.total()}")
        
