class Vehiculo:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

class Coche(Vehiculo):

    def accelerate(self):
        return "El coche está acelerando."

    def brake(self):
        return "El coche está frenando."
    
    def claxon(self):
        return "¡PIIIIIIIIIIIIIII!"
    
class Motocicleta(Vehiculo):

    def accelerate(self):
        return "La moto está acelerando."

    def brake(self):
        return "La moto está frenando."
    
    def claxon(self):
        return "¡PIIIIIIIIIIIIIII!"
    
class Bicicleta(Vehiculo):

    def accelerate(self):
        return "La bici está acelerando."

    def brake(self):
        return "La bici está frenando."
    
    def claxon(self):
        return "¡clink, clink!"
    
    def pedalear(self):
        return "Pedaleando la bicicleta."
    
