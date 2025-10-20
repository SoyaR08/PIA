# 11. Contador decreciente con while
# a. Escribe un programa que imprima los números del 10 al 1 utilizando un bucle while.
# 12. Mínimo común múltiplo (MCM) con while
# a. Escribe un programa que encuentre el MCM de dos números utilizando un bucle while.
# 13. Palabras que empiezan con una letra con for
# a. Escribe un programa que recorra una lista de palabras y cuente cuántas empiezan con 
# una letra específica utilizando un bucle for.
# 14. Buscar máximo en una lista con for
# a. Escribe un programa que busque el número más grande en una lista utilizando un bucle 
# for.
# 15. Suma de números en un rango con for
# a. Escribe un programa que sume todos los números en un rango dado utilizando un bucle 
# for.
# 16. Tablas de multiplicar con for
# a. Escribe un programa que imprima la tabla de multiplicar del 1 al 10 utilizando un bucle 
# for.
# 17. Potencia de un número con for
# a. Escribe un programa que calcule la potencia de un número dado utilizando un bucle 
# for
# 18. Calcular promedio con for
# Escribe un programa que calcule el promedio de una lista de números utilizando un bucle 
# for.
# 19. Contar letras y dígitos con for
# Escribe un programa que cuente cuántas letras y cuántos dígitos hay en una cadena 
# utilizando un bucle for.
# 20. Comparación de listas con for
# Escribe un programa que compare dos listas y cuente cuántos elementos coinciden utilizando 
# un bucle for.

# Ejercicio 11
print("============= Ejercicio 11 =============")
count = 10
while count >= 1:
    print(count)
    count -= 1
print()

# Ejercicio 12
print("============= Ejercicio 12 =============")
num1 = 4
num2 = 6

def findDivisors(n):
    divisors = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)

    return divisors

print("Divisores de ", num1, ": ", findDivisors(num1))
print("Divisores de ", num2, ": ", findDivisors(num2))
print()