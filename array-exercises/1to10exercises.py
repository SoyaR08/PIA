# 1. Crear una lista con los primeros 5 números enteros. Accede al tercer número de la lista.
# 2. Crea una lista vacía y añade los números del 1 al 10 uno por uno usando append().
# 3. Crea una lista con los nombres de 5 países. Cambia el segundo país por otro.
# 4. Crea una lista con 4 colores y usa insert() para añadir un nuevo color en la posición 2.
# 5. Elimina el primer elemento de una lista de frutas usando pop() sin argumentos.
# 6. Elimina una lista de 4 números utilizando remove() para borrar un número específico.
# 7. Crea una lista con 6 números y usa reverse() para invertir el orden de los elementos.
# 8. Usa sort() para ordenar una lista de 6 números en orden ascendente.
# 9. Crea una lista de nombres y utiliza count() para contar cuántas veces aparece un nombre específico.
# 10. Usa el operador in para verificar si un elemento existe en una lista de animales.

# Ejercicio 1

first5 = [1, 2, 3, 4, 5]
print("3º Número de la lista:", first5[2])

# Ejercicio 2

empty_list = []

for i in range(1, 11):
    empty_list.append(i)

print("Lista con números del 1 al 10:", empty_list)

# Ejercicio 3

countries = ["Argentina", "Paraguay" , "Chile", "Uruguay", "Brasil"]
countries[1] = "España"

print("Lista de países modificada:", countries)

# Ejercicio 4

colors = ["Rojo", "Azul", "Verde", "Amarillo"]
colors.insert(1, "Naranja")

print("Lista de colores modificada:", colors)

# Ejercicio 5

fruits = ["Manzana", "Banana", "Cereza", "Durazno"]
fruits.pop()
print("Lista de frutas con el primer elemento eliminado:", fruits)

# Ejercicio 6

numbers = [1, 2, 3, 4]

numbers.remove(3)

print("Lista de números con un elemento específico eliminado:", numbers)

# Ejercicio 7

numbers_reversed = [1, 2, 3, 4, 5, 6]
numbers_reversed.reverse()
print("Lista de números invertida:", numbers_reversed)

# Ejercicio 8

numbers_unordered = [3, 5, 1, 4, 2, 6]
numbers_unordered.sort()
print("Lista de números ordenada:", numbers_unordered)

# Ejercicio 9

names = ["Ana", "Juan", "Pedro", "Ana", "Luis", "Ana"]
count_same_names = names.count("Ana")
print("Número de veces que aparece 'Ana' en la lista:", count_same_names)

# Ejercicio 10
animals = ["Perro", "Gato", "Pájaro", "Pez"]
print("¿Existe 'Gato' en la lista de animales?", "Gato" in animals)