from classes import *

# Ejercicio 1

print("============= Ejercicio 1 =============")

book = Libro("El Quijote", "Miguel de Cervantes", 1469, 1605)
print(book)
print(book.isLarge())
print()

# Ejercicio 2

print("============= Ejercicio 2 =============")

persona = Persona("Juan", 30, "Masculino", 1.75)
print(persona)
print(persona.saludar("Pedro"))
print(f"Edad en 5 años: {persona.ageInFiveYears()}")
print(f"¿Es adulto? {'Sí' if persona.isAdult() else 'No'}")

print()

print("============= Ejercicio 3 =============")

account = CuentaBancaria("Ana Pérez", 1000, Type.AHORROS)

print(account.deposit_money(500))
print(account.show_info())
print(account.withdraw_money(1700))
print(account.show_info())
print(account.withdraw_money(1400))
print()

# Ejercicio 4

print("============= Ejercicio 4 =============")

coffe_machine = Cafetera("Nescafé", 3, 1.5)
print(coffe_machine.serve_coffee(0.225))
print(coffe_machine.fill_coffee())
print(coffe_machine.check_coffee())
print()

# Ejercicio 5

print("============= Ejercicio 5 =============")

rest = Restaurante("Billio's", "Any", {"PIZZA EVA": 11.99, "BILLIO'S IBÉRICA": 10.99})

print(rest.addPlate({"PaniAlcide": 13.99}))
rest.showMenu()
print(rest.orderAPlate())