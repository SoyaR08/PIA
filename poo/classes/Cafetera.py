class Cafetera:

    def __init__(self, brand, max_capacity, coffee_level):
        self.brand = brand
        self.max_capacity = max_capacity
        self.coffee_level = coffee_level

    def fill_coffee(self):
        self.coffee_level = self.max_capacity
        return f"La cafetera está llena"

    def serve_coffee(self, quantity):
        if quantity > self.coffee_level:
            self.coffee_level = 0
            return f"Se ha vaciado la cafetera, por favor rellenar"

        self.coffee_level -= quantity
        return f"Quedan {self.coffee_level} litros de café"
    
    def check_coffee(self):
        return f"Quedan {self.coffee_level} litros de café" if self.coffee_level > 0 else f"Está vacía"
        
