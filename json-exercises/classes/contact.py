class Contact:

    def __init__(self, nombre, apellidos, telefono, correo):
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.correo = correo

    def __str__(self):
        return f"{self.nombre} {self.apellidos}, con tlf: {self.telefono}, correo: {self.correo}"
    
    def parseToDict(self):
        return {"nombre": self.nombre, "apellidos": self.apellidos, "telefono": self.telefono, "correo": self.correo}