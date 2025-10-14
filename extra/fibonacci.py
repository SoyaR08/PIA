"""
Función de FIbonacci
Programa que imprima los primeros 50 números de la serie Fibonacci.
orden: 0, 1, 1, 2, 3, 5, 8, 13,...
"""

def fibonacci(number):

    start = 0
    next = 1

    for i in range(0, number):
        print(start)

        fibo = start + next
        start = next
        next = fibo


fibonacci(50)
