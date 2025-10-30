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

# Ejercicio 16
print("============= Ejercicio 16 =============")

score = 70

if score > 80 and score <= 100:
    print("A")
elif score > 60 and score <= 80:
    print("B")
elif score > 40 and score <= 60:
    print("C")
elif score > 20 and score <= 40:
    print("D")
elif score >= 0 and score <= 20:
    print("F")
print()

# Ejercicio 17
print("============= Ejercicio 17 =============")

possible_vowel = input("Introduce una letra: ").lower()

if possible_vowel in ['a', 'e', 'i', 'o', 'u']:
    print(f"La letra '{possible_vowel}' es una vocal.")
else:
    print(f"La letra '{possible_vowel}' no es una vocal.")
print()

# Ejercicio 18
print("============= Ejercicio 18 =============")

range_given = [1, 100]
number_to_check = int(input("Introduce un número entero: "))

if range_given[0] <= number_to_check <= range_given[1]:
    print(f"El número {number_to_check} está en el rango.")
else:
    print(f"El número {number_to_check} no está en el rango.")
print()

# Ejercicio 19
print("============= Ejercicio 19 =============")

def calculator(number1, number2, operation):
    match operation:
        case "+":
            return number1 + number2
        case "-":
            return number1 - number2
        case "*":
            return number1 * number2
        case "/":
            if number2 != 0:
                return number1 / number2
            else:
                return "Error: División por cero."
        case _:
            return "Operación no válida."

number_given1, number_given2, operation_given = float(input("Introduce el primer número: ")), float(input("Introduce el segundo número: ")), input("Introduce la operación (+, -, *, /): ")
print(f"El resultado de la operación es: {calculator(number_given1, number_given2, operation_given)}")
print()

# Ejercicio 20
print("============= Ejercicio 20 =============")

number = int(input("Introduce un número: "))

def isPrimeNumber(n):
    if n % 2 == 0:
        return False
    
    for i in range(1, n, 1):
        if n % i == 0 and i != 1:
            return False
        
    return True

print(f"¿Es primo?: {isPrimeNumber(number)}")
print()