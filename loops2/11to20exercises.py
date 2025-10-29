# Ejercicio 11
print("============= Ejercicio 11 =============")

num = int(input("Introduce un número entero: "))

if num % 2 == 0:
    print(f"El número {num} es par.")
else:
    print(f"El número {num} es impar.")

print()

# Ejercicio 12
print("============= Ejercicio 12 =============")

number_given = int(input("Introduce un número entero: "))

if number_given > 0:
    print(f"El número {number_given} es positivo.")
elif number_given < 0:
    print(f"El número {number_given} es negativo.")
else:
    print("El número es cero.")


print()

# Ejercicio 13
print("============= Ejercicio 13 =============")

n1, n2 = int(input("Introduce un número entero: ")), int(input("Introduce otro número entero: "))

if n1 > n2:
    print(f"El número {n1} es mayor que {n2}.")
elif n1 < n2:
    print(f"El número {n2} es mayor que {n1}.")
else:
    print("Ambos números son iguales.")

print()

# Ejercicio 14
print("============= Ejercicio 14 =============")

num1, num2, num3 = int(input("Introduce un número entero: ")), int(input("Introduce otro número entero: ")), int(input("Introduce otro número entero: "))

if num1 >= num2 and num1 >= num3:
    print(f"El número mayor es {num1}.")
elif num2 >= num1 and num2 >= num3:
    print(f"El número mayor es {num2}.")
else:
    print(f"El número mayor es {num3}.")

print()

# Ejercicio 15
print("============= Ejercicio 15 =============")

year = 2024

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f"El año {year} es bisiesto.")

print()