class Smartphone:

    def __init__(self, brand, model, storage, max_battery, current_battery):
        self.brand = brand
        self.model = model
        self.storage = storage  
        self.max_battery = max_battery  
        if current_battery < 0 or current_battery > 100:
            self.current_battery = 50
        else:
            self.current_battery = current_battery # Batería en porcentaje

    def charge(self, amount):

        if amount < 0:
            return "La cantidad a cargar no puede ser negativa."
        
        if self.current_battery + amount > 100:
            self.current_battery = 100
            return f"El teléfono está completamente cargado. Batería actual: {self.current_battery} %."
        
        self.current_battery += amount
        return f"Cargando... Batería actual: {self.current_battery} %."
    
    def call_contact(self):

        self.current_battery -= 5  # No se cuanto puede gastar una llamada, voy a suponer que un 5%
        return f"Llamando a contacto... Batería restante: {self.current_battery} %."
    
    def check_battery(self):
        return f"Batería actual: {self.current_battery} %."
