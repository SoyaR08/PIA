# Ejercicio 21
print("============= Ejercicio 21 =============")

range_start, range_end = 1, 100
sumatory = 0
for i in range(range_start, range_end + 1):
    if i % 2 == 0:
        sumatory += i

print(f"La suma de los números pares entre {range_start} y {range_end} es: {sumatory}")
print()

# Ejercicio 22
print("============= Ejercicio 22 =============")

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)

print()

# Ejercicio 23
print("============= Ejercicio 23 =============")

numbers = input("Introduce una serie de números separados por espacios y luego pulsa enter: ")

number_list = numbers.split(' ')

positive_count = 0
negative_count = 0
zero_count = 0

for number in number_list:

    try:
        num = int(number)
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
        else: 
            zero_count += 1
    except:
        continue

        
print(f"El usuario ha proporcionado {positive_count} números positivos, {negative_count} números negativos y {zero_count} ceros")
print()

# Ejercicio 24
print("============= Ejercicio 24 =============")

integer_list = [0, 1, 34, 2, -13, -9, -8, 12, 4]
sumatory = 0

for number in integer_list:
    if number > 0:
        sumatory += number

print(f"La suma de los enteros de la lista da como resultado: {sumatory}")
print()

# Ejercicio 25
print("============= Ejercicio 25 =============")

text_given = input("Introduce una cadena de texto cualquiera: ")
vowels = "aeiou"
punctuations = "¿?¡!|@#~%&¬/^*+,.º<>=()-_"
vowels_count = 0
consonants_count = 0

for char in text_given:
    if char.lower() in vowels:
        vowels_count += 1
    elif char.lower() not in punctuations:
        consonants_count += 1

print(f"La cadena {text_given}, tiene {vowels_count} vocales y {consonants_count} consonantes")
print()

# Ejercicio 26
print("============= Ejercicio 26 =============")

n_first_primes = int(input("Introduce un número entero: "))
prime_number_appearances = 0
number = 1

while prime_number_appearances < n_first_primes:
    isPrime = True

    if number % 2 == 0 and number != 2:
        isPrime = False

    for i in range(1, number+1):
        if number % i == 0 and (i != 1 and i != number):
            isPrime = False
            break

    if isPrime:
        print(number)
        prime_number_appearances += 1
    
    number += 1


print()

# Ejercicio 27
print("============= Ejercicio 27 =============")

import random

guess_number = random.randint(1, 100)
guessed = False
tries = 1
while not guessed:
    user_input = int(input(f"Introduce un número entre el 1 y el 100 | Intentos: {tries}; "))

    if user_input == guess_number:
        guessed = True

    elif user_input < guess_number:
        print("El número es mayor")

    else:
        print("El número es menor")
    
    tries += 1


print(f"Has advinado el número en {tries} intentos")
print()

# Ejercicio 28
print("============= Ejercicio 28 =============")

zero_given = False
numbers = []
media = 0
while not zero_given:

    try:
        number = int(input("Introduce un número: "))
        
        if number == 0:
            zero_given = True
        else:
            numbers.append(number)
    except:
        continue

media = sum(numbers) / len(numbers)

print(f"La media de la lista '{numbers}' es {media}")
print()

# Ejercicio 29
print("============= Ejercicio 29 =============")

string_given = input("Introduce una cadena: ")
reversed_string = ""

for i in range(len(string_given) -1, -1, -1):
    reversed_string += string_given[i]

print(reversed_string)
print()

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