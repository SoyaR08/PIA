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