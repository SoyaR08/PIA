# Ejercicio 9: Diccionarios (Segunda parte)
# 1. Crea un diccionario llamado capitales que contenga las siguientes parejas clave-valor: 
# - "España": "Madrid" 
# - "Francia": "París" 
# - "Italia": "Roma" 
# 2. Agrega una nueva pareja clave-valor "Alemania": "Berlín". 
# 3. Cambia el valor asociado a la clave "Francia" para que sea "Lyon". 
# 4. Elimina la entrada correspondiente a "Italia".
# 5. Imprime todas las claves del diccionario.
# 6. Imprime todos los valores del diccionario.
# 7. Imprime el diccionario final.


# *author: Rafael Navarro Gómez | rafa140200@gmail.com

dictionary = {
    "España": "Madrid",
    "Francia": "París",
    "Italia": "Roma"
}

print("Diccionario inicial: ", dictionary)
dictionary["Alemania"] = "Berlín"
print("Diccionario después de agregar Alemania: ", dictionary)
dictionary["Francia"] = "Lyon"
print("Diccionario después de cambiar Francia: ", dictionary)
dictionary.pop("Italia")
print("Diccionario después de eliminar Italia: ", dictionary)
print("Claves del diccionario: ", dictionary.keys())
print("Valores del diccionario: ", dictionary.values())
print("Diccionario final: ", dictionary)