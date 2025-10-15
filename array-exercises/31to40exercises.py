# 31. Crea una lista que contenga tanto números como cadenas, y accede al segundo elemento.
# 32. Usa enumerate() para imprimir el índice y valor de cada elemento de una lista.
# 33. Crea una lista de listas y usa for para recorrer los elementos de cada lista interna.
# 34. Usa del para eliminar un rango de elementos en una lista de números.
# 35. Filtra los elementos de una lista de números para obtener solo los mayores a 5.
# 36. Crea una lista de cadenas y usa split() para dividir cada cadena en palabras.
# 37. Convierte una tupla en una lista y luego añade un nuevo elemento.
# 38. Usa set() para eliminar los elementos duplicados de una lista.
# 39. Crea una lista de números e invierte el orden de los números sin usar reverse().
# 40. Divide una lista en partes iguales, p.e. , una lista de 12 elementos en 3 listas de 4.

# Ejercicio 31
print("====================Ejercicio 31====================")
array = [1, "dos", 3, "cuatro", 5]
print("Segundo elemento:", array[1])
print()

# Ejercicio 32
print("====================Ejercicio 32====================")
enumerated_array = list(enumerate(array))
print("Índice y valor de cada elemento:", enumerated_array)
print()

# Ejercicio 33
print("====================Ejercicio 33====================")
anidated_array = [[1, 2, 3], ["a", "b", "c"], [True, False]]

index = 0
for i in anidated_array:
    print("Lista interna:", index+1)
    for j in i:
        print("-",j)
    index += 1
print()

# Ejercicio 34
print("====================Ejercicio 34====================")
numbers = [1, 2, 3, 4,5 ,6 , 7, 8, 9, 10]
del numbers[3:5]
print("Lista después de eliminar un rango de elementos:",numbers)
print()

# Ejercicio 35
print("====================Ejercicio 35====================")
greatherthan5 = lambda x: x > 5
print("Números mayores a 5:",list(filter(greatherthan5, numbers)))
print()

# Ejercicio 36
print("====================Ejercicio 36====================")
string_array = ["Hola Mundo", "Me gusta Python"]
new_list = []
for i in string_array:
    for j in i.split():
        new_list.append(j)

print("Lista de cadenas divididas en palabras:",new_list)
print()

# Ejercicio 37
print("====================Ejercicio 37====================")
new_tuple = tuple((1, 2, 3, 4, 5, 6))
list_from_tuple = list(new_tuple)
list_from_tuple.append(7)
print("Tupla convertida en lista y con un nuevo elemento añadido:",list_from_tuple)
print()

# Ejercicio 38
print("====================Ejercicio 38====================")
duplicated_array = [1, 2 ,2 ,3 ,5 ,6, 7, 7, 8, 9]
set_from_array = set(duplicated_array)
print("Lista sin elementos duplicados:",list(set_from_array))
print()

# Ejercicio 39
print("====================Ejercicio 39====================")
ordered_array = [1, 2, 3, 4, 5]
ordered_array.sort(reverse=True)
print("Lista con el orden de los números invertido:",ordered_array)
print()

# Ejercicio 40
print("====================Ejercicio 40====================")
array_to_slice = list(range(1, 13))

def find_divisors(length):
    divisors = []
    for i in range(1, length + 1):
        if length % i == 0 and (i != 1 and i != length):
            divisors.append(i)
    return divisors

print("Lista dividida en partes iguales:", find_divisors(len(array_to_slice)))