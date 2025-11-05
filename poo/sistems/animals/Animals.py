class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        return "Grr..."
    
class Perro(Animal):

    def make_sound(self):
        return "Guau Guau"
    
class Gato(Animal):
    def make_sound(self):
        return "Miau Miau"
    
class Pajaro(Animal):
    def make_sound(self):
        return "Pío Pío"