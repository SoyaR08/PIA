# Ejercicio 30
print("============= Ejercicio 30 =============")
import random
user_number = input("Introduce un número entre 1 y 10: ")

while not user_number.isdigit():
    user_number = input("Eso no es un número, introduce otro entre 1 y 10: ")


user_number = int(user_number)

tries = 1
number_selected = random.randint(1, 10)
got_it = False
range_to_choose = [1,2,3,4,5,6,7,8,9,10]

while not got_it:
    if user_number == number_selected:
        got_it = True

    else:
        range_to_choose.remove(number_selected)
        number_selected = random.choice(range_to_choose)
        tries += 1
    print("Pensando...")

print(f"La máquina ha necesitado {tries} intentos para adivinar el número {user_number}")
print()