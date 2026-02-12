from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import math

plt.style.use('_mpl-gallery')

# make the data
np.random.seed(3) # Esto me indica que será siempre lo mismo

## Ejercicio 01  
# Utilizar la función de la raíz cuadrada (librería Math), generar un gráfico (Matplotlib) 
# de dispersión (Random) en el que se muestre 20 números enteros aleatorios entre 
# el 0 y 100 en el eje X y su raíz cuadrada en el eje Y. 


x = np.random.randint(0, 101, 20)

y = np.array([math.sqrt(i) for i in x])

# size and color:
sizes = np.random.uniform(15, 80, len(x))
colors = np.random.uniform(15, 80, len(x))

# plot
fig, ax = plt.subplots()

ax.scatter(x, y, s=sizes, c=colors, vmin=0, vmax=100)

ax.set(xlim=(0, 100), xticks=np.arange(1, 101, 10),
       ylim=(0, 10), yticks=np.arange(1, 11, 1))

plt.tight_layout()
plt.show()

## Ejercicio 02 
# Escribir un programa que pregunte al usuario por las ventas de un rango de años y 
# muestre por pantalla un diagrama de líneas con la evolución de las ventas. 

x = np.arange(2000, 2021)

size = len(x)

y = np.random.randint(10000, 15000, size)

# plot
fig, ax = plt.subplots()

ax.plot(x, y, linewidth=2.0)

ax.set_title("Evolución de ventas entre 2000 y 2020")
ax.set_xlabel("Año")
ax.set_ylabel("Ventas")

ax.set_xticks(x)
ax.tick_params(axis='x', rotation=45)

ax.set(xlim=(1999, 2021),
       ylim=(0, 15000), yticks=np.arange(0, 20001, 5000))

plt.tight_layout()
plt.show()

# Ejercicio 03.  
# Escribir una función que reciba un diccionario con las notas de las asignaturas de 
# un curso y una cadena con el nombre de un color y devuelva un diagrama de barras 
# de las notas en el color dado. 

def create_grades_graphic(grades, color="blue"):
    
    if not isinstance(grades, dict):
       raise Exception("Formato no válido")
    
    x = []
    y = []

    for item in grades.items():
        x.append(item[0])
        y.append(item[1])

    # plot
    fig, ax = plt.subplots()

    ax.bar(x, y, color=color)

    ax.set_title("Comparación de notas por asignatura")
    ax.set_xlabel("Asignatura")
    ax.set_ylabel("Nota")

    plt.tight_layout()
    plt.show()

# colores: red, blue, green, cyan, magenta, yellow, black, white
create_grades_graphic({"Matemáticas": 8, "Lengua": 7, "Inglés": 9}, color="blue")

# Ejercicio 04. 
# Escribir una función que reciba una serie de Pandas con las notas de los alumnos 
# de un curso y devuelva un diagrama de cajas con las notas. El diagrama debe tener 
# el título “Distribución de Notas”

def create_box_plot_grades_graphic(grades, color="blue"):
    
    if not isinstance(grades, pd.Series):
       raise Exception("Formato no válido")
    
    grades.plot.box(
        patch_artist=True, # Permite rellenar la caja
        boxprops=dict(facecolor=color)
    )
    plt.title("Distribución de Notas")
    plt.ylabel("Notas")

    plt.tight_layout()
    plt.show()

# colores: red, blue, green, cyan, magenta, yellow, black, white
create_box_plot_grades_graphic(pd.Series([8, 7, 9, 5, 6, 10]), color="blue")