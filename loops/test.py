# Ejercicio 27
print("============= Ejercicio 27 =============")
import random

head_streak = 0
head_counter = 0
cross_counter = 0
history = []

while head_streak < 3:
    choice = random.randint(0, 1)

    match choice:
        case 0:
            head_counter += 1
            head_streak += 1
            history.append("Cara")
        case 1:
            cross_counter += 1
            head_streak = 0
            history.append("Cruz")

print(f"Han salido {head_counter} caras y {cross_counter} cruces hasta obtener 3 caras seguidas.")
print(f"Historial de lanzamientos: {history}")
print()