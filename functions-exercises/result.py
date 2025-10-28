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