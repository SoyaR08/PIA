def calculate_factorial(n):

    abs_number = abs(n)
    factorial = 1

    if abs_number > 1:
        for i in range(abs_number, 0, -1):
            factorial *= i

    
    return factorial

def isPrimeNumber(n):
    if n % 2 == 0:
        return False
    
    for i in range(1, n, 1):
        if n % i == 0 and i != 1:
            return False
        
    return True

def plus_digits(number):

    result = 0

    if not number.isnumeric() and '-' in number:
        return "Input no válido"
    
    digits_array = list(number)

    for n in digits_array:
        result += int(n)

    return result

def fibonacci(number):

    start = 0
    next = 1

    for i in range(0, number):
        print(start)

        fibo = start + next
        start = next
        next = fibo
