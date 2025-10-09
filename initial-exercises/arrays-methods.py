# Ejercicio 6: Métodos de listas
# Crea una lista llamada colores que contenga los siguientes valores: "rojo", "verde", "azul", "amarillo".
# Agrega el color "morado" al final de la lista.
# Inserta el color "naranja" en la segunda posición.
# Elimina el color "verde" de la lista.
# Ordena la lista alfabéticamente.
# Invierte el orden de los elementos de la lista.
# Imprime la lista final.

# *author: Rafael Navarro Gómez | rafa140200@gmail.com

colores = ["rojo", "verde", "azul", "amarillo"]
print("- Lista base:", colores)
colores.append("morado")
print("- Lista con morado:", colores)
colores.insert(2, "naranja")
print("- Lista con naranja:", colores)
colores.remove("verde")
print("- Lista sin verde:", colores)
colores.sort()
print("- Lista ordenada:", colores)
colores.reverse()
print("- Lista invertida:", colores)