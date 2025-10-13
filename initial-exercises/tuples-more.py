# Ejercicio 11: Más sobre tuplas
# 1. Crea una tupla llamada dias_semana que contenga los días de la semana, empezando por "Lunes". 
# 2. Verifica si el día "Sábado" está en la tupla. 
# 3. Usa un loop para imprimir cada día de la semana. 
# 4. Intenta modificar el valor del primer día de la tupla y observa lo que ocurre.  

# *author: Rafael Navarro Gómez | rafa140200@gmail.com

dias_semana = tuple(("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"))
print("Tupla días de la semana:",dias_semana)
print("¿El día 'Sábado' está en la tupla?", "Sábado" in dias_semana)
for day in dias_semana:
    print(day)

try:
    dias_semana[0] = "Lunes Modificado" # Genera error: 'tuple' object does not support item assignment
except TypeError as e:
    print("Error al intentar modificar la tupla:", e)