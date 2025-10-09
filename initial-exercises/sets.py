# Ejercicio 8: Sets (conjuntos)
# Crea un set llamado frutas con los valores: "manzana", "banana", "naranja", "uva".
# Agrega una nueva fruta "pera" al set.
# Intenta agregar la fruta "banana" nuevamente al set (nota lo que sucede).
# Elimina la fruta "naranja" del set.
# Imprime todos los elementos del set.

# *author: Rafael Navarro Gómez | rafa140200@gmail.com

frutas = {"manzana", "banana", "naranja", "uva"}
print("Set: ",frutas)
frutas.add("pera")
print("Set actualizado: ", frutas)
frutas.add("banana") # No da error, pero no lo añade
print("Set actualizado v.2: ", frutas)