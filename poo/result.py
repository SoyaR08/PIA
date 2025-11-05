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

# Ejercicio 6

print("============= Ejercicio 6 =============")

std = Estudiante("Juan", "IAyBD", [8, 2, 5], 0)
print(std.add_grade(7))
print(std.calculate_average())
print(f"¿Está aprobado? {'Sí' if std.isApproved() else 'No'}")
print()

# Ejercicio 7

print("============= Ejercicio 7 =============")

ball = Pelota("Fútbol", "5", 2.3)

print(ball.inflate(0.5))
print(ball.check_pressure())
print(ball.deflate())

print()

# Ejercicio 8

print("============= Ejercicio 8 =============")

smrtphn = Smartphone("Samsung", "Galaxy S21", 128, 4000, 80)

print(smrtphn.call_contact())
print(smrtphn.charge(10))
print(smrtphn.check_battery())

print()

# Ejercicio 9

print("============= Ejercicio 9 =============")

pet = Mascota("Firulais", "Perro", 4, 60)

print(pet.feed())
print(pet.play())
print(pet.play())
print(pet.check_energy())

print()

# Ejercicio 10

print("============= Ejercicio 10 =============")

reloj = Reloj(10, 61, 120)
print(reloj.show_time())
print(reloj.advance_time('m'))
print(reloj.show_time())
print()