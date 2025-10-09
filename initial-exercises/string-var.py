# Ejercicio Variables de tipo cadena (string)
# Crea un programa que:
# 1. Declare dos variables de tipo cadena: nombre con el valor "Juan" y apellido con el valor "Pérez".
# 2. Concatenar las dos cadenas en una nueva variable nombre_completo, separadas por un espacio.
# 3. Imprime la longitud de la cadena nombre_completo.
# 4. Convierte nombre_completo a mayúsculas y minúsculas.

# *author: Rafael Navarro Gómez | rafa140200@gmail.com

name, surname = "Juan", "Pérez"
nombre_completo = name+" "+surname
print(nombre_completo)
print(len(nombre_completo))
print("Mayúsculas: ", nombre_completo.upper(),". Minúsculas: ", nombre_completo.lower())