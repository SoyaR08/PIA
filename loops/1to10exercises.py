# 1. Números pares con for. Escribe un programa que imprima todos los números pares entre 1 y 100 utilizando un bucle for. Utiliza una condición if para verificar si el número es par.
# 2. Factorial con while. Escribe un programa que calcule el factorial de un número dado utilizando un bucle while.
# 3. Números primos con for. Escribe un programa que determine si un número es primo utilizando un bucle for con una condición if.
# 4. Buscar en lista con else en un for Escribe un programa que busque un número en una lista utilizando un bucle for, y si no lo encuentra, muestra un mensaje en el bloque else.
# 5. Palíndromo con while Escribe un programa que verifique si una palabra es un palíndromo utilizando un bucle while.
# 6. Sumar dígitos de un número con while Escribe un programa que sume los dígitos de un número utilizando un bucle while.
# 7. Adivinar el número con while Crea un juego en el que el usuario intente adivinar un número secreto. El programa deberá seguir solicitando al usuario que adivine hasta que lo haga correctamente.
# 8. Conversión de temperaturas con for Escribe un programa que convierta un rango de temperaturas de Celsius a Fahrenheit utilizando un bucle for.
# 9. Serie de Fibonacci con for Escribe un programa que genere los primeros N números de la serie de Fibonacci utilizando un bucle for.
# 10. Conteo de vocales con for a. Escribe un programa que cuente cuántas vocales hay en una palabra dada utilizando un bucle for y una condición if.

import random

# Ejercicio 1 

print("============= Ejercicio 1 =============")
for num in range(1, 101):
    if num % 2 == 0:
        print(num)
print()

# Ejercicio 2
print("============= Ejercicio 2 =============")
number_given = 10
fact = 1
while (number_given > 1):
    fact *= number_given
    number_given -= 1
print(fact)
print() 

# Ejercicio 3
print("============= Ejercicio 3 =============")
def isPrime(n):
    isPrime = True

    if n % 2 == 0 and n != 2:
        isPrime = False
        return isPrime
        
    for i in range(1, n+1):
        if n % i == 0 and i != 1 and i != n:
            isPrime = False
            return isPrime
    
    return isPrime


prime_number = 27
print("El nº ",prime_number, " es primo? ", isPrime(prime_number))
print()

# Ejercicio 4
print("============= Ejercicio 4 =============")
numbers_list = [1, 3, 5, 7, 9]
number_to_find = 9
for num in numbers_list:
    if num == number_to_find:
        print("Número encontrado:", number_to_find)
        break

else:
    print("Número no encontrado:", number_to_find)
print()

# Ejercicio 5
print("============= Ejercicio 5 =============")
palindrome = "Roma amor"
isPalindrome = False
count = len(palindrome) - 1
reversed_palindrome = ""
while (count >= 0):
    reversed_palindrome += palindrome[count]
    count -= 1

if palindrome.lower().replace(" ", "") == reversed_palindrome.lower().replace(" ", ""):
    isPalindrome = True

print("La palabra ", palindrome, " es palíndromo? ", isPalindrome)
print()

# Ejercicio 6
print("============= Ejercicio 6 =============")
number = str(44)
sum_digits = 0
i = len(number) - 1
while i >= 0:
    sum_digits += int(number[i])
    i-=1

print("La suma de los dígitos de ", number, " es: ", sum_digits)
print()

# Ejercicio 7
# Is commented due to input request
print("============= Ejercicio 7 =============")
secret = random.randint(1, 10)
user_try = int(input("Adivina el número secreto entre 1 y 10: "))
while secret != user_try:

    if user_try < secret:
        print("El número secreto es mayor. Inténtalo de nuevo.")

    else:
        print("El número secreto es menor. Inténtalo de nuevo.")

    user_try = int(input("Adivina el número secreto entre 1 y 10: "))

print("¡Felicidades! Has adivinado el número secreto:", secret)
print()

# Ejercicio 8
print("============= Ejercicio 8 =============")

temperatures_celsius = range(0, 101, 10)
parsed_temperatures = []
def celsius_to_fahrenheit(celsius):
    return (celsius * 9)/5 + 32

for celsius in temperatures_celsius:
    fahrenheit = celsius_to_fahrenheit(celsius)
    parsed_temperatures.append(fahrenheit)

print("Temperaturas en Celsius:", list(temperatures_celsius))
print("Temperaturas en Fahrenheit:", parsed_temperatures)
print()

# Ejercicio 9
print("============= Ejercicio 9 =============")
def fibonacci(number):

    start = 0
    next = 1

    for i in range(0, number):
        print(start)

        fibo = start + next
        start = next
        next = fibo


fibonacci(8)
print()

# Ejercicio 10
print("============= Ejercicio 10 =============")
vowels = "aeiou"
word = "Hello world"
vowels_found = 0
for char in word.lower():
    if char in vowels:
        vowels_found += 1

print("Número de vocales en la palabra '", word, "': ", vowels_found)
print()