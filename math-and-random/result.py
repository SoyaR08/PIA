import random
import math

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