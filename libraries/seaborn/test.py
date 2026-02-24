import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 5. Violin plot con categorización de datos:
# Utiliza el dataset iris.
# Convierte la columna de longitud del sépalo y la especie a arrays 
# de NumPy.
# Genera un violin plot para analizar la distribución de la longitud del 
# sépalo por cada especie.
# Ajusta la división interna y muestra puntos individuales.

# Cargar dataset
df = sns.load_dataset("diamonds")

# Seleccionar columnas de interés y convertir a NumPy
carat = np.array(df["carat"])
price = np.array(df["price"])
depth = np.array(df["depth"])

# Revisar primeras filas
print(df.head())

# Crear categorías de carat
df['carat_bin'] = pd.cut(df['carat'], bins=[0, 0.5, 1, 1.5, 2, 5], 
                         labels=['0-0.5','0.5-1','1-1.5','1.5-2','2-5'])

plt.figure(figsize=(10,6))

sns.set_theme(style="whitegrid")  # Estilo general

sns.boxplot(
    data=df,
    x='carat_bin',
    y='price',
    hue='cut',
    palette='Set2',          # Paleta de colores
    linewidth=2,             # Grosor del borde de las cajas
    fliersize=4,             # Tamaño de los puntos atípicos
    dodge=True               # Separar cajas por hue
)

plt.xlabel("Rango de Quilates")
plt.ylabel("Precio ($)")
plt.title("Distribución de Precio por Quilates y Tipo de Corte")
plt.legend(title="Corte", bbox_to_anchor=(1.05,1), loc='upper left')
plt.tight_layout()
plt.show()