class Restaurante:


    # name: str, kitchen_type: str, menu: dict[str : int]
    def __init__(self, name, kitchen_type, menu):
        self.name = name
        self.kitchen_type = kitchen_type
        self.menu = menu

    def addPlate(self, newPlate):

        if not isinstance(newPlate, dict):
            return f"Dato inválido, no se ha podido añadir el plato"

        self.menu.update(newPlate)

        return f"Plato {newPlate} añadido"
    
    def showMenu(self):
        print(f"============ Menú de {self.name} ============")
        for plate, price in self.menu.items():
            print(f"{plate} | {price}")
        print()

    def orderAPlate(self):
        self.showMenu()
        plateName = input("Escoja un plato: ").strip().upper()

        if plateName not in self.menu:
            return "Plato no reconocido"
        
        chosen_plate = f"Ha escogido: {plateName} | {self.menu.get(plateName)}"

        return chosen_plate