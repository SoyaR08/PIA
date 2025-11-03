# Ejercicio 31
print("============= Ejercicio 31 =============")

posible_palindrome = "Anita lava la tina"

def isPalindrome(string):

    reversed_palindrome = ""
    cleaned_string = string.replace(" ", "").lower()

    for i in range(len(cleaned_string) - 1, -1, -1):
        reversed_palindrome+=cleaned_string[i]

    return True if cleaned_string == reversed_palindrome else False

print(f"La cadena {posible_palindrome}, ¿es palindromo?: {isPalindrome(posible_palindrome)}")
print()

# Ejercicio 32
print("============= Ejercicio 32 =============")

array = [8, 3, 9, 10, 2, 1, 4, 5, 7, 6]
max_number = array[0]

for number in array:
    if number > max_number:
        max_number = number

print(f"El número mayor de la lista {array} es: {max_number}")
print()

# Ejercicio 33
print("============= Ejercicio 33 =============")

def isPrimeNumber(n):
    if n % 2 == 0:
        return False
    
    for i in range(1, n, 1):
        if n % i == 0 and i != 1:
            return False
        
    return True

given_range = range(1, 10)
prime_count = 0
primes = []

for i in given_range:
    prime = isPrimeNumber(i)

    if prime:
        primes.append(i)
        prime_count += 1

print(f"Hay {prime_count} primos entre {given_range.start} y {given_range.stop} siendo: {primes}")
print()

# Ejercicio 34
print("============= Ejercicio 34 =============")

# array = [2, 1, 3, 4, 5, 6, 9, 8, 7, 10]
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
unordered = False
i = 0
step = 1
limit = len(array)

while not unordered and step < limit:

    if array[i] > array[step]:
            unordered = True

    else:
        i += 1
        step += 1

        
print(f"¿La lista {array}, está ordenada ascendentemente?: {not unordered}")
print()

# Ejercicio 35
print("============= Ejercicio 35 =============")

def findDivisors(n):
    divisors = []
    
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)

    return divisors

def isPerfectNumber(n):

    num_divisors = findDivisors(n)

    result = sum(num_divisors)

    return result == n

given_range2 = range(1, 1001)

perfect_numbers = []

for i in given_range2:
    if isPerfectNumber(i):
        perfect_numbers.append(i)

print(f"Los números perfectos correspondidos entre 1 y 1000 son: {perfect_numbers}")
print()

# Ejercicio 36
print("============= Ejercicio 36 =============")

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz()
print()

# Ejercicio 37
print("============= Ejercicio 37 =============")
import random

detected_zero = False
numbers = []
while not detected_zero:
    random_num = random.randint(0, 10)

    if random_num == 0:
        detected_zero = True
    
    numbers.append(random_num)

print(f"Números obtenidos: {numbers}")
print()

# Ejercicio 38
print("============= Ejercicio 38 =============")

numbers_list = [5, 7, 4, 2, 10, 1, 9, 3, 8, 6]
mx_number = numbers_list[0]
second_mx_number = numbers_list[0]

for n in numbers_list:
    if n > mx_number:
        if mx_number > second_mx_number:
            second_mx_number = mx_number
        mx_number = n

    if second_mx_number < n and n < mx_number:
        second_mx_number = n

print(f"En la lista {numbers_list} el 2º número mayor es: {second_mx_number}, y el primero es: {mx_number}")
print()

# Ejercicio 39
print("============= Ejercicio 39 =============")

numbers_list = [5, 7, 4, 2, 10, 1, 9, 3, 8, 6]
evens = []
odds = []

for n in numbers_list:
    if n % 2 == 0:
        evens.append(n)
    else:
        odds.append(n)

print(f"Pares: {evens}. Impares: {odds}")
print()

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