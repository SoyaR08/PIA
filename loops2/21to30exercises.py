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