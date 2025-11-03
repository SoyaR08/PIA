# Ejercicio 40
print("============= Ejercicio 40 =============")

number_to_parse = 13
q = 1
binary_number = ""

while q > 0:
    q = number_to_parse // 2
    rest = number_to_parse % 2
    binary_number = str(rest) + binary_number
    number_to_parse = q


print(binary_number)
print()