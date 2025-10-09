# Ejercicio Diccionarios
# Crea un programa que:
# 1. Declare un diccionario llamado estudiante con las siguientes claves y valores:
# - "nombre": "Ana"
# - "edad": 22
# - "curso": "Matemáticas"
# 2. Cambia el valor de "edad" a 23.
# 3. Agrega una nueva clave "promedio" con el valor 8.5.
# 4. Imprime todas las claves del diccionario.
# 5. Imprime el valor asociado a la clave "nombre"

# *author: Rafael Navarro Gómez | rafa140200@gmail.com

estudiante = {
    "nombre": "Ana",
    "edad": 22,
    "curso": "Matemáticas"
}

print("- Estudiante sin modificar:",estudiante)
estudiante["edad"] = 23
print("- Estudiante modificado:",estudiante)
estudiante["promedio"] = 8.5
print("- Nombre: ",estudiante["nombre"])