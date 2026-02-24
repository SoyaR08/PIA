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

# 5. Violin plot con categorización de datos:
# Utiliza el dataset iris.
# Convierte la columna de longitud del sépalo y la especie a arrays 
# de NumPy.
# Genera un violin plot para analizar la distribución de la longitud del 
# sépalo por cada especie.
# Ajusta la división interna y muestra puntos individuales.

# Cargar dataset
df = sns.load_dataset("iris")

# Convertir columnas a arrays de NumPy
sepal_length = np.array(df["sepal_length"])
species = np.array(df["species"])

# Crear violin plot
plt.figure(figsize=(8,6))
sns.violinplot(
    x=species,
    y=sepal_length,
    inner="quartile"   # División interna (cuartiles)
)

# Mostrar puntos individuales
sns.stripplot(
    x=species,
    y=sepal_length,
    color="black",
    size=3,
    jitter=True
)

plt.title("Distribución de la longitud del sépalo por especie")
plt.xlabel("Especie")
plt.ylabel("Longitud del sépalo")
plt.show()

# 6. Gráfico de barras con agregación de datos:
# Carga el dataset titanic.
# Convierte la columna de clase (class) y tarifa (fare) a arrays.
# Crea un gráfico de barras que muestre el promedio de tarifas 
# pagadas por clase, con desviaciones estándar indicadas.
# Aplica una paleta de color diferenciada por género.

# Cargar dataset
df = sns.load_dataset("titanic")

print(df.head())

# Eliminar valores nulos relevantes
df = df.dropna(subset=["class", "fare", "sex"])

# Convertir columnas a arrays de NumPy
clase = df["class"].to_numpy()
tarifa = df["fare"].to_numpy()
genero = df["sex"].to_numpy()

# Crear DataFrame auxiliar para agregación
data = pd.DataFrame({
    "class": clase,
    "fare": tarifa,
    "sex": genero
})

# Calcular promedio y desviación estándar
resumen = data.groupby(["class", "sex"])["fare"].agg(["mean", "std"]).reset_index()

# Crear gráfico de barras
plt.figure(figsize=(10,6))

sns.barplot(
    data=resumen,
    x="class",
    y="mean",
    hue="sex",
    palette="Set2",
    capsize=0.1
)

plt.title("Promedio de tarifas pagadas por clase y género")
plt.xlabel("Clase")
plt.ylabel("Tarifa promedio")
plt.legend(title="Género")
plt.show()

# 7. FacetGrid con múltiples gráficos de distribución:
# Trabaja con el dataset fmri.
# Convierte las columnas de tiempo y respuesta a arrays de NumPy.
# Crea una cuadrícula de gráficos de KDE por sujeto para comparar 
# patrones de respuesta.
# Personaliza la disposición de las subparcelas.

# Cargar dataset
df = sns.load_dataset("fmri")

print(df.head())

# Eliminar valores nulos
df = df.dropna(subset=["timepoint", "signal", "subject"])

# Convertir columnas a arrays de NumPy
tiempo = df["timepoint"].to_numpy()
respuesta = df["signal"].to_numpy()

# Crear FacetGrid por sujeto
g = sns.FacetGrid(
    df,
    col="subject",
    col_wrap=4,          # Número de columnas antes de saltar a la siguiente fila
    height=3,
    aspect=1.2,          # Relación ancho/alto
    sharex=True,
    sharey=True
)

# Añadir KDE a cada subgráfico
g.map(sns.kdeplot, "signal", fill=True)

# Personalización
g.set_titles("Sujeto {col_name}")
g.set_axis_labels("Respuesta (signal)", "Densidad")
g.figure.subplots_adjust(top=0.9, hspace=0.4, wspace=0.3)
g.figure.suptitle("Distribución KDE de la respuesta por sujeto")

plt.show()

# 8. Pairplot para el análisis multivariado:
# Usa el dataset iris.
# Convierte todas las columnas numéricas a arrays.
# Genera un pairplot con diferentes tipos de gráficos en la diagonal y 
# fuera de la diagonal.
# Cambia los estilos y agrega una regresión lineal a las relaciones.

# Cargar dataset
df = sns.load_dataset("iris")

# Convertir todas las columnas numéricas a arrays de NumPy
numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns
numeric_arrays = {col: df[col].to_numpy() for col in numeric_cols}

# Cambiar estilo
sns.set_style("whitegrid")
sns.set_context("notebook")

# Crear pairplot
g = sns.pairplot(
    df,
    hue="species",
    diag_kind="kde",              # KDE en la diagonal
    kind="reg",                   # Regresión fuera de la diagonal
    plot_kws={
        "line_kws": {"color": "red"},
        "scatter_kws": {"alpha": 0.5}
    },
    diag_kws={"fill": True}
)

plt.suptitle("Análisis Multivariado - Dataset Iris", y=1.02)
plt.show()

# 9. Gráfico de líneas con datos de series temporales:
# Crea un DataFrame simulado con datos de ventas diarias y 
# conviértelos a arrays.
# Genera un gráfico de líneas para analizar las tendencias 
# estacionales.
# Aplica un suavizado con Seaborn y personaliza las líneas con 
# estilos diferenciados.

# 1. Crear datos simulados
np.random.seed(42)

fechas = pd.date_range(start="2024-01-01", periods=180, freq="D")

# Patrón estacional (sinusoidal) + tendencia + ruido
ventas = (
    200
    + 0.3 * np.arange(180)                         # Tendencia creciente
    + 20 * np.sin(2 * np.pi * np.arange(180)/30)   # Estacionalidad mensual
    + np.random.normal(0, 10, 180)                 # Ruido
)

df = pd.DataFrame({
    "fecha": fechas,
    "ventas": ventas
})

print(df.head())

# 2. Convertir a arrays de NumPy
fechas_array = df["fecha"].to_numpy()
ventas_array = df["ventas"].to_numpy()

print("Fechas:", fechas_array[:5])
print("Ventas:", ventas_array[:5])

# 🔹 3. Configuración estética
sns.set_style("darkgrid")
sns.set_context("talk")

plt.figure(figsize=(12,6))

# 4. Línea original
sns.lineplot(
    x=fechas_array,
    y=ventas_array,
    label="Ventas diarias",
    linestyle="--"
)

# 5. Suavizado (media móvil con rolling)
df["suavizado"] = df["ventas"].rolling(window=7).mean()

sns.lineplot(
    data=df,
    x="fecha",
    y="suavizado",
    label="Tendencia suavizada (7 días)",
    linewidth=3
)

plt.title("Tendencia Estacional de Ventas Diarias")
plt.xlabel("Fecha")
plt.ylabel("Ventas")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# 10. Catplot para variables categóricas con ajuste de orden:
# Usa el dataset exercise.
# Convierte la columna de duración y tipo de ejercicio a arrays.
# Crea un catplot de tipo stripplot para observar la dispersión de 
# duración en diferentes tipos de ejercicio.
# Ajusta el orden de categorías y el ancho de puntos.

# 🔹 1. Cargar dataset
df = sns.load_dataset("exercise")

print(df.head())

# 🔹 2. Eliminar valores nulos relevantes
df = df.dropna(subset=["time", "kind"])

# 🔹 3. Convertir columnas a arrays de NumPy
duracion = df["time"].to_numpy()
tipo_ejercicio = df["kind"].to_numpy()

print("Duración:", duracion[:5])
print("Tipo ejercicio:", tipo_ejercicio[:5])

# 🔹 4. Definir orden personalizado
orden_categorias = ["rest", "walking", "running"]

# 🔹 5. Configuración estética
sns.set_style("whitegrid")
sns.set_context("talk")

# 🔹 6. Crear catplot tipo stripplot
g = sns.catplot(
    data=df,
    x="kind",
    y="time",
    kind="strip",
    order=orden_categorias,
    height=6,
    aspect=1.3,
    jitter=True,
    size=6      # ancho/tamaño de puntos
)

g.set_axis_labels("Tipo de ejercicio", "Duración")
g.figure.suptitle("Dispersión de la duración según tipo de ejercicio", y=1.02)
plt.tight_layout()
plt.show()

# 11. Swarmplot con ajuste de jitter:
# Usa el dataset penguins.
# Convierte el tamaño de las aletas y el peso corporal a arrays de 
# NumPy.
# Genera un swarmplot mostrando la relación entre estos valores, 
# ajustando el parámetro dodge.

# Cargar dataset
df = sns.load_dataset("penguins").dropna(subset=["flipper_length_mm", "body_mass_g", "species"])

# Convertir a arrays
aletas = df["flipper_length_mm"].to_numpy()
peso = df["body_mass_g"].to_numpy()

sns.set_style("whitegrid")
plt.figure(figsize=(8,6))

sns.swarmplot(
    data=df,
    x="flipper_length_mm",
    y="body_mass_g",
    hue="species",
    dodge=True,      # Ajuste por especie
    size=4
)

plt.title("Relación entre tamaño de aleta y peso corporal")
plt.xlabel("Longitud de aleta (mm)")
plt.ylabel("Peso corporal (g)")
plt.legend(title="Especie")
plt.show()

# 12. Regresión lineal múltiple con visualización avanzada:
# Usa el dataset mpg.
# Convierte las columnas de potencia (horsepower) y peso (weight) a 
# arrays.
# Genera un gráfico de regresión múltiple mostrando la relación entre 
# peso y potencia con diferentes niveles de confianza.

df = sns.load_dataset("mpg").dropna(subset=["horsepower", "weight", "origin"])

# Convertir a arrays
potencia = df["horsepower"].to_numpy()
peso = df["weight"].to_numpy()

sns.set_style("darkgrid")
plt.figure(figsize=(8,6))

sns.lmplot(
    data=df,
    x="weight",
    y="horsepower",
    hue="origin",
    ci=95,          # Nivel de confianza
    height=6,
    aspect=1.2
)

plt.title("Relación entre peso y potencia por origen")
plt.show()

# 13. Histogramas superpuestos con diferentes bins:
# Crea un DataFrame con distribuciones normales simuladas, 
# conviértelas a arrays.
# Genera histogramas superpuestos de diferentes grupos con ajuste de 
# bins.
# Personaliza las transparencias y colores.

np.random.seed(42)

grupo1 = np.random.normal(50, 10, 500)
grupo2 = np.random.normal(60, 15, 500)

df = pd.DataFrame({
    "Grupo 1": grupo1,
    "Grupo 2": grupo2
})

# Convertir a arrays
g1_array = df["Grupo 1"].to_numpy()
g2_array = df["Grupo 2"].to_numpy()

plt.figure(figsize=(8,6))

plt.hist(g1_array, bins=20, alpha=0.5, label="Grupo 1")
plt.hist(g2_array, bins=30, alpha=0.5, label="Grupo 2")

plt.title("Histogramas superpuestos")
plt.xlabel("Valores")
plt.ylabel("Frecuencia")
plt.legend()
plt.show()

# 14. Plot de violin combinado con stripplot:
# Usa el dataset titanic.
# Convierte la columna de edad y clase a arrays de NumPy.
# Superpone un stripplot sobre un violin plot para observar la distribución 
# de edades por clase.

df = sns.load_dataset("titanic").dropna(subset=["age", "class"])

# Convertir a arrays
edad = df["age"].to_numpy()
clase = df["class"].to_numpy()

plt.figure(figsize=(8,6))

sns.violinplot(
    data=df,
    x="class",
    y="age",
    inner="quartile"
)

sns.stripplot(
    data=df,
    x="class",
    y="age",
    color="black",
    size=3,
    jitter=True,
    alpha=0.4
)

plt.title("Distribución de edades por clase")
plt.show()

# 15. Mapa de calor de confusión para clasificación:
# Simula un DataFrame con resultados de clasificación, conviértelo a 
# array.
# Crea un mapa de calor con las tasas de falsos positivos y negativos.
# Ajusta la escala de colores y anota la matriz

# Simular matriz de confusión
conf_matrix = np.array([[85, 15],
                        [10, 90]])

df_conf = pd.DataFrame(
    conf_matrix,
    index=["Real Negativo", "Real Positivo"],
    columns=["Pred Negativo", "Pred Positivo"]
)

plt.figure(figsize=(6,5))

sns.heatmap(
    df_conf,
    annot=True,
    fmt="d",
    cmap="coolwarm",
    linewidths=0.5
)

plt.title("Mapa de calor - Matriz de confusión")
plt.show()