from matplotlib import pyplot as plt
import numpy as np
import math

plt.style.use('_mpl-gallery')

# make the data
np.random.seed(3) # Esto me indica que será siempre lo mismo


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