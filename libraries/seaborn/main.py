import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

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

# 2. Análisis de correlación con mapa de calor:
# Carga el dataset penguins de Seaborn.
# Convierte todas las variables numéricas a arrays y calcula la matriz 
# de correlación.
# Visualiza la correlación usando un mapa de calor con anotaciones 
# y personalización de la paleta de colores.

df = sns.load_dataset("penguins")

df["bill_length_mm"] = df["bill_length_mm"].fillna(df["bill_length_mm"].mean())
df["bill_depth_mm"] = df["bill_depth_mm"].fillna(df["bill_depth_mm"].mean())
df["flipper_length_mm"] = df["flipper_length_mm"].fillna(df["flipper_length_mm"].mean())
df["body_mass_g"] = df["body_mass_g"].fillna(df["body_mass_g"].mean())

cleaned_df = df[["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]]

corr_matrix = cleaned_df.corr()


ax = sns.heatmap(corr_matrix, annot=True, cmap="crest")

ax.set_title("Matriz de Correlación entre las Características de los Pingüinos")

plt.tight_layout()
plt.show()

# 3. Distribución de datos con KDE Plot y rug plot:
# A partir del dataset tips, convierte las columnas total_bill y tip a 
# arrays.
# Genera un gráfico de densidad kernel (KDE) superpuesto con un 
# gráfico de rug.
# Ajusta el ancho de banda y experimenta con diferentes estilos de 
# visualización.

df = sns.load_dataset("tips")

t_bill, tip = np.array(df["total_bill"]), np.array(df["tip"])

# Gráfico KDE + Rug para total_bill
plt.figure(figsize=(8,5))
sns.kdeplot(x=t_bill, fill=True, alpha=0.5, bw_adjust=2)
sns.rugplot(x=t_bill, height=0.05)

plt.xlabel("Total de la Cuenta ($)")
plt.title("Distribución de Total Bill con KDE y Rug")
plt.show()

# Gráfico KDE + Rug para tip
plt.figure(figsize=(8,5))
sns.kdeplot(x=tip, fill=True, alpha=0.5, color="orange", bw_adjust=2)
sns.rugplot(x=tip, height=0.05, color="red")

plt.xlabel("Propina ($)")
plt.title("Distribución de Tip con KDE y Rug")
plt.show()

# 4. Boxplot multivariado con ajuste de estilo:
# Trabaja con el dataset diamonds.
# Convierte las columnas carat, price y depth a arrays de NumPy.
# Crea un gráfico de caja para analizar la distribución de precios en 
# diferentes rangos de quilates, segmentado por el tipo de corte.
# Personaliza el gráfico con diferentes estilos de borde y paletas.

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