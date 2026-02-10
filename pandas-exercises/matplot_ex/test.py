from matplotlib import pyplot as plt
import numpy as np
import math

plt.style.use('_mpl-gallery')

# make the data
np.random.seed(3) # Esto me indica que será siempre lo mismo


# Ejercicio 03.  
# Escribir una función que reciba un diccionario con las notas de las asignaturas de 
# un curso y una cadena con el nombre de un color y devuelva un diagrama de barras 
# de las notas en el color dado. 

def create_grades_graphic(grades):
    
    if not isinstance(grades, dict):
       raise Exception("Formato no válido")
    
    x, y = grades.items()

    return ""

# x = np.arange(2000, 2021)

# size = len(x)

# y = np.random.randint(10000, 15000, size)

# # plot
# fig, ax = plt.subplots()

# ax.plot(x, y, linewidth=2.0)

# ax.set_title("Evolución de ventas entre 2000 y 2020")
# ax.set_xlabel("Año")
# ax.set_ylabel("Ventas")

# ax.set_xticks(x)
# ax.tick_params(axis='x', rotation=45)

# ax.set(xlim=(1999, 2021),
#        ylim=(0, 15000), yticks=np.arange(0, 20001, 5000))

# plt.tight_layout()
# plt.show()

create_grades_graphic(9)