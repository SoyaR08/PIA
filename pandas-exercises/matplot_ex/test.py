from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import math

plt.style.use('_mpl-gallery')

# make the data
np.random.seed(3) # Esto me indica que será siempre lo mismo


# Ejercicio 08. 
# El fichero “bancos.csv” contiene las cotizaciones de los principales bancos de 
# España con los siguientes datos:  - - - - - - 
# Empresa: Nombre de la empresa 
# Apertura: Precio de la acción a la apertura de la Bolsa 
# Máximo: Precio máximo de la acción durante la jornada. 
# Mínimo: Precio mínimo de la acción durante la jornada. 
# Cierre: Precio de la acción al cierre de la Bolsa 
# Volumen: Volumen de negocios al cierre de la Bolsa 
# Construir una función que reciba el fichero “bancos.csv” y cree un diagrama de 
# líneas con las series temporales de las cotizaciones de cierre de cada banco. 

def load_csv(path):

    return pd.read_csv(path).copy()

def create_income_outcome_graphics(dataframe):
    
    fig, ax = plt.subplots()

    x = dataframe['month']
    y = dataframe['income']
    y2 = dataframe['outcome']

    plt.ylim(0, 150000)  # eje Y de 0 a 150000

    ax.plot(x, y, marker='o', color='green', label='Ingresos', linewidth=2.0)
    ax.plot(x, y2, marker='o', color='red', label='Gastos' , linewidth=2.0)

    # Títulos y etiquetas
    plt.title('Evolución de Ingresos y Gastos')
    plt.xlabel('Mes')
    plt.ylabel('Monto')
    plt.xticks(rotation=45)  # rotar nombres de meses
    plt.grid(True)
    plt.legend()  # muestra la leyenda
    plt.tight_layout()  # ajusta el gráfico para que no se corten los labels

    plt.show()



df = load_csv("pandas-exercises/matplot_ex/bancos.csv")

test = df.groupby(df["Empresa"])
for nombre_banco, grupo in test:
    print(nombre_banco)   # el nombre del banco
    print(grupo.head(3))  # primeras 3 filas de ese banco