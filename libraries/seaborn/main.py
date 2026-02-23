import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Gráfico de dispersión avanzado con estilo personalizado:
# Utiliza un dataset de automóviles (mpg) de Seaborn.
# Convierte las columnas horsepower, weight y mpg a arrays de 
# NumPy y crea un gráfico de dispersión donde el tamaño de los 
# puntos represente el peso y el color la eficiencia de combustible.
# Personaliza con temas y ajustes de tamaño.

df = sns.load_dataset("mpg")

horsepower, weight, mpg = np.array(df["horsepower"]), np.array(df["weight"]), np.array(df["mpg"])

ax = sns.scatterplot(x=horsepower, y=mpg, size=weight, hue=mpg)
ax.set(xlabel="Caballos de fuerza", ylabel="Millas por Galón")
ax.set_title("Relación entre Caballos de Fuerza y Millas por Galón")

plt.tight_layout()
plt.show()