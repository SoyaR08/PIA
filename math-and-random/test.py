import random
import math
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