# 21. Crea una lista de números y usa sum() para obtener la suma de todos los elementos.
# 22. Crea una lista de booleanos y usa all() para verificar si todos los elementos son True.
# 23. Usa any() para verificar si al menos uno de los elementos en una lista de booleanos es True.
# 24. Convierte una lista de cadenas en una cadena única separada por comas usando join().
# 25. Usa list() para convertir una cadena en una lista de caracteres.
# 26. Crea una lista con 10 números y usa slicing para obtener una sublista con los números del índice 2 al 6.
# 27. Elimina el último elemento de una lista de ciudades usando pop() con índice negativo.
# 28. Usa max() para encontrar el valor más grande en una lista de números.
# 29. Usa min() para encontrar el valor más pequeño en una lista de números.
# 30. Crea una lista de números al azar y usa sorted() para ordenar la lista sin modificar la original.

# Ejercicio 21

numbers = [1, 2, 3, 4, 5]
print("Suma de todos los elementos:", sum(numbers))

# Ejercicio 22

bools = [True, True, True, False]
print("¿Son todos True?:", all(bools))

# Ejercicio 23

print("¿Hay algún True?:", any(bools))

# Ejercicio 24

strings = ["¡", "Hola", "Mundo", "!"]
joined_string = ",".join(strings)
print("Cadena unida:",joined_string)

# Ejercicio 25

string = "Hello World"
string_list = list(string)
print("Cadena convertida en lista:",string_list)

# Ejercicio 26

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sub_array = array[2:7]
print("Sublista del índice 2 al 6:",sub_array)

# Ejercicio 27

cities = ["Madrid", "Barcelona", "Sevilla", "Teruel"]
cities.pop(-1)
print("Lista después de eliminar el último elemento:",cities)

# Ejercicio 28

max_value = max(numbers)
print("Valor más grande:",max_value)

# Ejercicio 29

min_value = min(numbers)
print("Valor más pequeño:",min_value)

# Ejercicio 30

random_numbers = [5, 2, 9, 1, 7, 6]
random_numbers_sorted = sorted(random_numbers.copy())
print("Lista original:", random_numbers," Lista ordenada:", random_numbers_sorted)