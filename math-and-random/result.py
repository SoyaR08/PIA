import random
import math
from blackjack import blackjack

# Ejercicio de Random y Math 1

print("========= Ejercicio de Random y Math 1 =========")

dice1, dice2 = random.randint(1, 6), random.randint(1, 6)
total = dice1 + dice2
print(f"Dado 1: {dice1}, Dado 2: {dice2}, Suma total: {total}")
print()

# Ejercicio de Random y Math 2

print("========= Ejercicio de Random y Math 2 =========")

roulette = random.randint(0, 36)

if roulette == 0:
    print(f"Gana la casa")
elif roulette % 2 == 0:
    print(f"Número: {roulette}, Color: Rojo")
else:
    print(f"Número: {roulette}, Color: Negro")

print()

# Ejercicio de Random y Math 3
print("========= Ejercicio de Random y Math 3 =========")

values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
strips = ["Corazones", "Diamantes", "Tréboles", "Picas"]
cards = []
for _ in range(5):
    random_value_index = random.randint(0, len(values) - 1)
    random_strip_index = random.randint(0, len(strips) - 1)
    card = f"{values[random_value_index]} de {strips[random_strip_index]}"
    cards.append(card)

print("Cartas seleccionadas: ", cards)
print()

# Ejercicio de Random y Math 5
print("========= Ejercicio de Random y Math 5 =========")
blackjack() # Too much code to copy here so i made an apart archive and call the function
print()

# Ejercicio de Random y Math 6
print("========= Ejercicio de Random y Math 6 =========")

options = ['1', 'X', '2']


for i in range(15):
    choice = random.choice(options)

    match choice:
        case '1':
            print(f"Partida {i+1}. Ha ganado el local")
        case 'X':
            print(f"Partida {i+1}. Empate")
        case '2':
            print(f"Partida {i+1}. Ha ganado el visitante")
print()

# Ejercicio de Random y Math 7
print("========= Ejercicio de Random y Math 7 =========")

possible_numbers = list(range(1, 50))
number_series = ""

for i in range(6):
    choice = random.choice(possible_numbers)
    number_series += " " + str(choice)
    possible_numbers.remove(choice)

complementary = random.choice(possible_numbers)
reinteger = random.randint(0, 9)

number_series = f"{number_series} [{complementary}] [{reinteger}]"

print(number_series)
