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