class Persona:
    def __init__(self, name, age, gender, height):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height

    def __str__(self):
        return f"{self.name}, de {self.age} años, {self.gender} con altura de {self.height}"

    def saludar(self, other_name):
        return f"¡Hola, {other_name}!"
    
    def ageInFiveYears(self):
        return self.age + 5
    
    def isAdult(self):
        return self.age >= 18