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


def fibonacci(number):

    start = 0
    next = 1

    for i in range(0, number):
        print(start)

        fibo = start + next
        start = next
        next = fibo
