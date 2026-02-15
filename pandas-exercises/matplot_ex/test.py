from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import math

plt.style.use('_mpl-gallery')

# make the data
np.random.seed(3) # Esto me indica que será siempre lo mismo


# Ejercicio 06.  
# Escribir una función que reciba una serie de Pandas con el número de ventas de un 
# producto por años y una cadena con el tipo de gráfico a generar (líneas, barras, 
# sectores, áreas) y devuelva un diagrama del tipo indicado con la evolución de las 
# ventas por años y con el título “Evolución del Número de Ventas” 

def create_graphics(data, years, option):
    
    fig, ax = plt.subplots()

    match option:

        case 'a': # Gráfico de líneas

            x = years
            y = data

            ax.plot(x, y, linewidth=2.0)

            ax.set_title(f"Evolución de ventas entre {x.min()} y {x.max()}")
            ax.set_xlabel("Año")
            ax.set_ylabel("Ventas")

            ax.set_xticks(x)
            ax.tick_params(axis='x', rotation=45)
            ax.set(xlim=(x.min() - 1, x.max() + 1),
                ylim=(y.min() - 10000, y.max() + 10000), yticks=y)
            
        case 'b': # Gráfico de barras

            x = years
            y = data

            ax.bar(x, y, color="blue")

            ax.set_title(f"Evolución de ventas entre {x.min()} y {x.max()}")
            ax.set_xlabel("Año")
            ax.set_ylabel("Ventas")
            ax.set(xlim=(x.min() - 1, x.max() + 1), xticks=x,
                ylim=(y.min() - 10000, y.max() + 10000), yticks=y)
            

        case 'c': # Gráfico de sectores (tarta)
            print()

        case 'd': # Gráfico de áreas
            print()
        
    plt.tight_layout()
    plt.show()


data = pd.Series([50000, 30000, 80000])
years = pd.Series([2020, 2021, 2022])


create_graphics(data, years, "b")