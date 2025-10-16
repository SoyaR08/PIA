# 41. Crea una lista con los precios de productos y calcula el promedio.
# 42. Crea una lista de temperaturas y convierte todas las temperaturas de Celsius a Fahrenheit.
# 43. Encuentra los números pares en una lista de 10 números enteros.
# 44. Crea una lista de palabras y usa map() para convertirlas a mayúsculas.
# 45. Simula una cola utilizando listas, añadiendo elementos con append() y removiéndolos con pop(0).
# 46. Crea una lista de nombres y usa filter() para obtener solo los nombres que comienzan con una vocal.
# 47. Encuentra los duplicados en una lista de números y elimina las repeticiones.
# 48. Crea una lista de nombres y ordénalos por la longitud de cada nombre.
# 49. Divide una lista de estudiantes en dos grupos de forma alterna (uno para cada grupo).
# 50. Crea una lista de enteros y usa reduce() para obtener el producto de todos los elementos

from functools import reduce

# Ejercicio 41
print("====================Ejercicio 41====================")
prices = [10.5, 20.75, 30.0, 15.25, 50.0]
total = 0
for price in prices:   
    total += price

average = total / len(prices)
print("Precio promedio:", average)
print()

# Ejercicio 42
print("====================Ejercicio 42====================")
celsius_temps = [0, 20, 37, 100]

def calculate_fahrenheit(celsius):
    return (celsius * 9)/5 + 32

fahrenheit_temps = list(map(calculate_fahrenheit, celsius_temps))

print("Temperaturas en Fahrenheit:", fahrenheit_temps)
print()

# Ejercicio 43
print("====================Ejercicio 43====================")
numbers = range(1, 11)
even = list(filter(lambda x: x % 2 == 0, numbers))
print("Numeros pares:", even)
print()

# Ejercicio 44
print("====================Ejercicio 44====================")
min_words = ["hola", "mundo", "python", "es", "genial"]
upper_words = list(map(lambda x: x.upper(), min_words))
print("Palabras en mayúsculas:", upper_words)
print()

# Ejercicio 45
print("====================Ejercicio 45====================")
queue = [0]
for i in range(1, 11):
    queue.append(i)
    print("Cola", queue)
    queue.pop(0)
print()

# Ejercicio 46
print("====================Ejercicio 46====================")
names = ["Rafa", "Álvaro", "Enrique", "Mario", "Jennifer", "Óscar"]
vowels = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]
print("Nombres que empiezan por vocal:", list(filter(lambda x: x[0].lower() in vowels, names)))
print()

# Ejercicio 47
print("====================Ejercicio 47====================")
numbers_duplicated = [1, 2, 3, 4, 4, 2, 9, 4, 6, 7, 8, 1, 3]
print("Lista con duplicados:", numbers_duplicated)
dictionary_duplications = {}
numbers_non_duplicated = []

for i in range(0, len(numbers_duplicated)):
    for j in range(i, len(numbers_duplicated)):
        duplicated = False
        if numbers_duplicated[i] == numbers_duplicated[j] and i != j:
            if numbers_duplicated[i] not in dictionary_duplications:
                dictionary_duplications[numbers_duplicated[i]] = [j]
            else:
                if j not in dictionary_duplications[numbers_duplicated[i]]:
                    dictionary_duplications[numbers_duplicated[i]].append(j)

for position in dictionary_duplications.values():
    numbers_duplicated[position[0]] = ""

numbers_non_duplicated = list(filter(lambda x: x != "", numbers_duplicated))

print("Lista sin duplicados:", numbers_non_duplicated)
print()

# Ejercicio 48
print("====================Ejercicio 48====================")
print("Nombres ordenados por longitud:", list(sorted(names, key=(lambda x: len(x)))))
print()

# Ejercicio 49
print("====================Ejercicio 49====================")
students = ["Rafa", "Álvaro", "Enrique", "Mario", "Jennifer", "Óscar"]
group1 = []
group2 = []

for i in range(0, len(students)):
    if i % 2 == 0:
        group1.append(students[i])
    else:
        group2.append(students[i])

print("Grupo 1:", group1, "Grupo 2:", group2)
print()

# Ejercicio 50
print("====================Ejercicio 50====================")
product_list = range(1, 6)
print("Producto de todos los elementos:", reduce((lambda x, y: x * y), product_list))
print()