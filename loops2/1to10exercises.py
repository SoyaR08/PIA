# Ejercicio 1

print("============= Ejercicio 1 =============")
for i in range(1, 11):
    print(i)
print()

# Ejercicio 2

print("============= Ejercicio 2 =============")
for i in range(1, 101):
    if i % 2 == 0:
        print(i)
print()

# Ejercicio 3

print("============= Ejercicio 3 =============")
for i in range(6):
    string = ""
    for j in range(i):
        string += "*"
    print(string)
print()

# Ejercicio 4

print("============= Ejercicio 4 =============")
for i in range(6, 0, -1):
    string = ""
    for j in range(i):
        string += "*"
    print(string)
print()

# Ejercicio 5

print("============= Ejercicio 5 =============")
n = int(input("Ingrese un número entero positivo: "))
for i in range(n):
    print(i)
print()

# Ejercicio 6
print("============= Ejercicio 6 =============")

num_fact = 5

for i in range(num_fact - 1, 1, -1):
    num_fact *= i

print(f"El factorial de 5 es: {num_fact}")

# Ejercicio 7
print("============= Ejercicio 7 =============")

num_multiple_table = int(input("Ingrese un número entero positivo: "))

for i in range(1, 11):
    print(f"{num_multiple_table} x {i} = {num_multiple_table * i}")

print()

# Ejercicio 8
print("============= Ejercicio 8 =============")

n_times = 8
odd_times = 0
i = 1
while odd_times < n_times:
    if i % 2 != 0:
        print(i)
        odd_times += 1
    i += 1

print()

# Ejercicio 9
print("============= Ejercicio 9 =============")

def fibonacci(number):

    start = 0
    next = 1

    for _ in range(0, number):
        print(start)

        fibo = start + next
        start = next
        next = fibo


fibonacci(50)
