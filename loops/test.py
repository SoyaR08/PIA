# Ejercicio 24
print("============= Ejercicio 24 =============")

number_list = [9, 10, 8, 3, 2, -7, 5, 6, 4, 1]
max_number = number_list[0]
min_number = number_list[0]

for number in number_list:
    if number > max_number:
        max_number = number
    elif number < min_number:
        min_number = number

print(f"El número mayor de la lista es: {max_number} y el menor es: {min_number}")