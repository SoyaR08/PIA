class Persona:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"Nombre: {self.name}, edad: {self.age}, género: {self.gender}"
    
class Estudiante(Persona):

    def __init__(self, name, age, gender, grade):
        super().__init__(name, age, gender)
        self.grade = grade

    def study(self, subject):
        return f"{self.name} está estudiando {subject}."
    
    def __str__(self):
        return super().__str__() + f", grado: {self.grade}"
    
class Profesor(Persona):

    def __init__(self, name, age, gender, subject_teached):
        super().__init__(name, age, gender)
        self.subject_teached = subject_teached

    def teach(self):
        return f"{self.name} está enseñando {self.subject_teached}."
    
    def __str__(self):
        return super().__str__() + f", materia que imparte: {self.subject_teached}"
    
class Director(Persona):

    def __init__(self, name, age, gender, years_in_charge):
        super().__init__(name, age, gender)
        self.years_in_charge = years_in_charge

    def manage(self):
        return f"{self.name} tiene {self.years_in_charge} años en el cargo."
    
    def __str__(self):
        return super().__str__() + f", y lleva: {self.years_in_charge} años en el cargo."