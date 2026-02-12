from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import math

plt.style.use('_mpl-gallery')

# make the data
np.random.seed(3) # Esto me indica que será siempre lo mismo


# Ejercicio 05. 
# Escribir una función que reciba una serie de Pandas con el número de ventas de un 
# producto durante los meses de un trimestre y un título, y cree un diagrama de 
# sectores con las ventas en formato PNG con el título dado. El diagrama debe 
# guardarse en un fichero con el formato PNG y el título dado. 

def create_pie_sells_graphic(grades):
    
    if not isinstance(grades, pd.Series):
       raise Exception("Formato no válido")
    
    colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7,grades.size))

    # plot
    fig, ax = plt.subplots()
    ax.pie(grades.values, colors=colors, radius=3, center=(4, 4),
        wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)

    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
        ylim=(0, 8), yticks=np.arange(1, 8))

    plt.tight_layout()
    plt.show()

data = pd.Series([50000, 30000, 80000])

# colores: red, blue, green, cyan, magenta, yellow, black, white
create_pie_sells_graphic(data)