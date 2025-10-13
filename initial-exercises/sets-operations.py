# Ejercicio 12: Operaciones con sets
# 1. Crea un set llamado animales con los siguientes valores: "gato", "perro", "loro", "pez". 
# 2. Crea un segundo set llamado animales_domesticos con los valores "gato", "perro", "conejo". 
# 3. Encuentra la intersección entre ambos sets (es decir, los animales que están en ambos).  
# 4. Encuentra la diferencia entre animales y animales_domesticos. 
# 5. Haz la unión de los dos sets.   

# *author: Rafael Navarro Gómez | rafa140200@gmail.com

animales = set(("gato", "perro", "loro", "pez"))
print("Set animales:",animales)
animales_domesticos = set(("gato", "perro", "conejo"))
print("Set animales domésticos:",animales_domesticos)
intersection = animales.intersection(animales_domesticos)
print("Intersección:", intersection)
diff = animales.difference(animales_domesticos)
print("Diferencia:", diff)
union = animales.union(animales_domesticos)
print("Unión:", union)