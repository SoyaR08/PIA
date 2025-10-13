# Ejercicio 12: Operaciones con sets
# 1. Crea un diccionario llamado clase con la siguiente estructura: 
# clase = { 
#     "estudiante1": { 
#         "nombre": "Carlos", 
#         "edad": 19, 
#         "materias": ["Matemáticas", "Física"] 
#     }, 
#     "estudiante2": { 
#         "nombre": "Marta", 
#         "edad": 20, 
#         "materias": ["Química", "Biología"] 
#     } 
# }
# 2. Agrega un tercer estudiante llamado "Pedro", de 21 años, con las materias "Historia" y "Geografía". 
# 3. Imprime el nombre y la edad de todos los estudiantes.  
# 4. Cambia la edad de "Marta" a 21 años.  
# 5. Elimina las materias de "Carlos". 

# *author: Rafael Navarro Gómez | rafa140200@gmail.com

clase = { 
    "estudiante1": { 
        "nombre": "Carlos", 
        "edad": 19, 
        "materias": ["Matemáticas", "Física"] 
    }, 
    "estudiante2": { 
        "nombre": "Marta", 
        "edad": 20, 
        "materias": ["Química", "Biología"] 
    } 
}

print("Diccionario inicial de clase:", clase)
clase["estudiante3"] = {
    "nombre": "Pedro",
    "edad": 21,
    "materias": ["Historia", "Geografía"]
}
print("Después de agregar a Pedro:", clase)

for student in clase.values():
    name, age = student["nombre"], student["edad"]
    print("Nombre:", name, "| Edad:", age)


clase["estudiante2"]["edad"] = 21
print("Después de cambiar la edad de Marta:", clase["estudiante2"])
clase["estudiante1"]["materias"].clear()
print("Después de eliminar las materias de Carlos:", clase["estudiante1"])