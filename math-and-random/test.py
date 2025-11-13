import random
import math

# Ejercicio de Random y Math 7
print("========= Ejercicio de Random y Math 7 =========")

possible_numbers = list(range(1, 50))
number_series = ""

for i in range(6):
    choice = random.choice(possible_numbers)
    number_series += " " + str(choice)
    possible_numbers.remove(choice)

print(number_series)