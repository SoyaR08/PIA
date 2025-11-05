from datetime import date

class Producto:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Ropa(Producto):

    def __init__(self, name, price, quantity, size):
        super().__init__(name, price, quantity)
        self.size = size

    def calculate_amount(self, discount):
        total = self.price * self.quantity
        discount_amount = total * (discount / 100)
        return total - discount_amount

class Alimento(Producto):
    def __init__(self, name, price, quantity, expiration_date):
        super().__init__(name, price, quantity)
        self.expiration_date = expiration_date

    def calculate_amount(self):
        today = date.today()
        exp_date = date.fromisoformat(self.expiration_date)
        total = self.price * self.quantity
        if exp_date < today:
            return 0
        elif (exp_date - today).days <= 5:
            discount_amount = total * 0.2
            return total - discount_amount
        else:
            return total

class Electrodomestico(Producto):

    def __init__(self, name, price, quantity, energic_waste):
        super().__init__(name, price, quantity)
        self.energic_waste = energic_waste

    def calculate_amount(self):
        total = self.price * self.quantity
        if self.energic_waste:
            tax = total * 0.05
            return total + tax
        else:
            return total