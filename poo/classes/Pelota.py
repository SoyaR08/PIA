class Pelota:

    def __init__(self, sport_type, size, air_pressure):
        self.sport_type = sport_type
        self.size = size
        self.air_pressure = air_pressure

    def inflate(self, pressure):
        if pressure > 0:
            self.air_pressure += pressure
            return f"Pelota inflada. Presión actual: {self.air_pressure}"
        else:
            return "La presión a añadir debe ser positiva."
        
    def deflate(self):
        self.air_pressure = 0
        return "Pelota desinflada."
    
    def check_pressure(self):

        if self.air_pressure > 2.5:
            return "La presión de la pelota es alta."
        elif self.air_pressure < 2:
            return "La presión de la pelota es baja."
        else:
            return "La presión de la pelota es adecuada."
