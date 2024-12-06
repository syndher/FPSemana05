class Produto:
        def __init__(self, name, price, quantity):
            self.name = name
            self.price = price
            self.quantity = quantity

        def addstock(self, quantity):
            if quantity > 0:
                self.quantity+=quantity
                print(1)
            else:
                print(0)

        def sell(self, quantity):
            if quantity<= self.quantity:
                self.quantity-= quantity
                print(1)
            else:
                print(0)
        def inform(self):
             print(f"{self.name} {self.price} {self.quantity}")

item = Produto("Vaso", 19.99, 100)
item.addstock(-20)
item.addstock(20)
item.sell(50)
item.sell(100)
item.inform()

