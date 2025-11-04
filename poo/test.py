from classes import Restaurante
# Ejercicio 5

print("============= Ejercicio 5 =============")

rest = Restaurante("Billio's", "Any", {"PIZZA EVA": 11.99, "BILLIO'S IBÉRICA": 10.99})

print(rest.addPlate({"PaniAlcide": 13.99}))
rest.showMenu()
print(rest.orderAPlate())
print()