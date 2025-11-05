class Mascota:

    def __init__(self, name, animal_type, age, energy):
        self.name = name
        self.animal_type = animal_type
        self.age = age
        self.energy = energy

    def play(self):

        if self.energy < 15:
            return f"{self.name} está muy cansado para jugar."

        self.energy -= 15
        return f"{self.name} está jugando feliz."
    
    def feed(self):

        self.energy += 20
        return f"{self.name} ha sido alimentado y ahora tiene {self.energy} de energía."
    
    def check_energy(self):

        if self.energy >= 80:
            return f"{self.name} está lleno de energía."
        elif 50 <= self.energy < 80:
            return f"{self.name} tiene mucha energía"
        elif 25 <= self.energy < 50:
            return f"{self.name} está algo cansado."
        else:
            return f"{self.name} está muy cansado."