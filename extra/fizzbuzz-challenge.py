"""Fizz-Buzz
Programa que muestra por consola (print) los números del 1 al 100 (inclusive) sustituyendo:
- Los múltiplos de 3 por la palabra "Fizz".
- Los múltiplos de 5 por la palabra "Buzz".
- Los múltiplos de 3 y de 5 por la palabra "FizzBuzz".

"""
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