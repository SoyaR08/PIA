# Ejercicio 30
print("============= Ejercicio 30 =============")

isANumber = False
digits_sum = 0
while not isANumber:
    n = input("Introduce un número: ")

    try:
        n_int = int(n)
        isANumber = True
    except:
        continue
        
for digit in n:
    digits_sum += int(digit)

print(f"La suma de los dígitos de {n} es {digits_sum}")
print()