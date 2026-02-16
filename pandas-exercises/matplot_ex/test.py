from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import math

plt.style.use('_mpl-gallery')

# make the data
np.random.seed(3) # Esto me indica que será siempre lo mismo


## Ejercicio 09. 
# El fichero “titanic.csv” contiene información sobre los pasajeros del Titanic. Crear 
# un dataframe con Pandas y a partir del mismo, generar los siguientes diagramas;  
# 1. Diagrama de Sectores con los fallecidos y supervivientes 
# 2. Histograma con las edades 
# 3. Diagrama de Barras con el número de personas en cada clase 
# 4. Diagrama de Barras con el número de personas fallecidas y 
# supervivientes en cada clase. 
# 5. Diagrama de Barras con el número de personas fallecidas y 
# supervivientes acumuladas en cada clase.

def load_csv(path):

    return pd.read_csv(path).copy()

def create_survivors_pie(dataframe):
    
    fig, ax = plt.subplots()

    for key, value in dataframe:
        print(key)   # el nombre del banco
        print(value.head(3))  # primeras 3 filas de ese banco
        ax.plot(value["Fecha"], value["Cierre"], marker='o', label=key, linewidth=2.0)

    # Títulos y etiquetas
    plt.title('Evolución de Cotizaciones de Bancos')
    plt.xlabel('Fecha')
    plt.ylabel('Cierre (USD)')
    plt.xticks(rotation=45)  # rotar nombres de meses
    plt.grid(True)
    plt.legend()  # muestra la leyenda
    plt.tight_layout()  # ajusta el gráfico para que no se corten los labels

    plt.show()


    # colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, sells.size))

    # fig, ax = plt.subplots()

    # ax.set_title(title)

    # ax.pie(
    #     sells.values,
    #     labels=months,
    #     colors=colors,
    #     autopct=lambda p: f'{int(p * sum(sells) / 100)}',
    #     wedgeprops={"linewidth": 1, "edgecolor": "white"}
    # )

    # ax.axis('off')

    # plt.tight_layout()


df = load_csv("pandas-exercises/matplot_ex/titanic.csv")
print(df.head(3))

