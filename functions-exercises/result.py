from functions import *

# Ejercicio Factorial 

print("============= Ejercicio Factorial =============")
number = 5
print(f"El factorial de {number} es {calculate_factorial(number)}")
print()

# Ejercicio Primo 

print("============= Ejercicio Primo =============")
possible_prime = int(input("Introduce un número cualquiera: "))
print(f"¿{possible_prime} es primo? {isPrimeNumber(possible_prime)}")
print()

# Ejercicio Suma de Dígitos 

print("============= Ejercicio Suma de Dígitos =============")
numeric_string = input("Introduce un número cualquiera: ")
print(f"La suma de los dígitos de {numeric_string} es {plus_digits(numeric_string)}")
print()

# Ejercicio Celsius a Fahrenheit 

print("============= Ejercicio Celsius a Fahrenheit =============")
celsius = int(input("Introduce un número cualquiera: "))
print(f"{celsius} grados Celsius son: {parseCelsiusToFahrenheit(celsius)} grados Fahrenheit")
print()

# Ejercicio Sumatorio de números de un array 

print("============= Ejercicio Sumatorio de números de un array =============")
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"La suma de los elementos del array: {array} es: {sumArrayNumbers(array)}")
print()

# Ejercicio Fibonacci 

print("============= Ejercicio Fibonacci =============")
fibo = 5
print(f"Los {fibo} primeros números de la secuencia de Fibonacci son: {fibonacci(fibo)}")
print()

print("============= Ejercicio MCD =============")
n1 = 270
n2 = 192
print(f"El MCD de {n1} y {n2} es: {mcdEuclideAlorithm(n1, n2)}")
print()

# Ejercicio Ordenar un array

print("============= Ejercicio Ordenar un array =============")

numbers = [4, 8, 1, 2, 6, 9, 3, 5, 7, 0, 10]
print(f"Lista original: {numbers}, lista ordenada: {sortArray(numbers)}")
print()

# Ejercicio Calcular Área 

print("============= Ejercicio Calcular Área =============")
radius = 5
print(f"El área de un círculo de radio {5}cm es {calculateCircleArea(radius)} cm^2")
print()

# Ejercicio Transformar horas, minutos y segundos a segundos 

print("============= Ejercicio Transformar horas, minutos y segundos a segundos =============")

hours1, minutes1, seconds1 = 4, 30, 12
print(f"La hora {hours1}:{minutes1}:{seconds1} son {parseToSeconds(hours1, minutes1, seconds1)} segundos")
print()

# Ejercicio Transformar horas, minutos y segundos a segundos 

print("============= Ejercicio Transformar horas, minutos y segundos a segundos =============")

seconds2 = 16212
parseSecondsToDate(seconds2)
print(f"{seconds2} segundos corresponden a las {parseSecondsToDate(seconds2)} horas")
print()

# Ejercicio Pasos a Kilómetros 

print("============= Ejercicio Pasos a Kilómetros =============")

steps = 10000
print(f"{steps} pasos corresponden a {calculateStepsToKm(steps)} km")
print()

# Ejercicio Cuadrado 

print("============= Ejercicio Cuadrado =============")

square_number = 2
print(f"El cuadrado de {square_number} es {squared(square_number)}")
print()

# Ejercicio Suma de dos números 

print("============= Ejercicio Suma de dos números =============")

number1 = 2
number2 = 3
print(f"La suma de {number1} y {number2} es {addition(number1, number2)}")
print()

# Ejercicio Invertir una cadena 

print("============= Ejercicio Invertir una cadena =============")

string = "Amor"
print(f"La cadena {string} al revés es: {revertString(string)}")
print()

# Ejercicio Número mayor 

print("============= Ejercicio Número mayor =============")

number1 = 2
number2 = 3
print(f"El mayor de {number1} y {number2} es {greatherThan(number1, number2)}")
print()

# Ejercicio Filtrar pares 

print("============= Ejercicio Filtrar pares =============")

evenAndOdds = [1, 2, 3, 4, 5, 6, 7, 8]
even = list(filter(lambda a: a % 2 == 0, evenAndOdds))
print(even)
print()

# Ejercicio Palíndromo 

print("============= Ejercicio Palíndromo =============")

string = "Anita lava la tina"
print(f"¿La cadena {string} es un palíndromo? {isPalindrome(string)}")
print()

