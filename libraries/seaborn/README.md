1. Gráfico de dispersión avanzado con estilo personalizado:
Utiliza un dataset de automóviles (mpg) de Seaborn.
Convierte las columnas horsepower, weight y mpg a arrays de 
NumPy y crea un gráfico de dispersión donde el tamaño de los 
puntos represente el peso y el color la eficiencia de combustible.
Personaliza con temas y ajustes de tamaño.

2. Análisis de correlación con mapa de calor:
Carga el dataset penguins de Seaborn.
Convierte todas las variables numéricas a arrays y calcula la matriz 
de correlación.
Visualiza la correlación usando un mapa de calor con anotaciones 
y personalización de la paleta de colores.

3. Distribución de datos con KDE Plot y rug plot:
A partir del dataset tips, convierte las columnas total_bill y tip a 
arrays.
Genera un gráfico de densidad kernel (KDE) superpuesto con un 
gráfico de rug.
Ajusta el ancho de banda y experimenta con diferentes estilos de 
visualización.

4. Boxplot multivariado con ajuste de estilo:
Trabaja con el dataset diamonds.
Convierte las columnas carat, price y depth a arrays de NumPy.
Crea un gráfico de caja para analizar la distribución de precios en 
diferentes rangos de quilates, segmentado por el tipo de corte.
Personaliza el gráfico con diferentes estilos de borde y paletas.

5. Violin plot con categorización de datos:
Utiliza el dataset iris.
Convierte la columna de longitud del sépalo y la especie a arrays 
de NumPy.
Genera un violin plot para analizar la distribución de la longitud del 
sépalo por cada especie.
Ajusta la división interna y muestra puntos individuales.

6. Gráfico de barras con agregación de datos:
Carga el dataset titanic.
Convierte la columna de clase (class) y tarifa (fare) a arrays.
Crea un gráfico de barras que muestre el promedio de tarifas 
pagadas por clase, con desviaciones estándar indicadas.
Aplica una paleta de color diferenciada por género.

7. FacetGrid con múltiples gráficos de distribución:
Trabaja con el dataset fmri.
Convierte las columnas de tiempo y respuesta a arrays de NumPy.
Crea una cuadrícula de gráficos de KDE por sujeto para comparar 
patrones de respuesta.
Personaliza la disposición de las subparcelas.

8. Pairplot para el análisis multivariado:
Usa el dataset iris.
Convierte todas las columnas numéricas a arrays.
Genera un pairplot con diferentes tipos de gráficos en la diagonal y 
fuera de la diagonal.
Cambia los estilos y agrega una regresión lineal a las relaciones.

9. Gráfico de líneas con datos de series temporales:
Crea un DataFrame simulado con datos de ventas diarias y 
conviértelos a arrays.
Genera un gráfico de líneas para analizar las tendencias 
estacionales.
Aplica un suavizado con Seaborn y personaliza las líneas con 
estilos diferenciados.

10. Catplot para variables categóricas con ajuste de orden:
Usa el dataset exercise.
Convierte la columna de duración y tipo de ejercicio a arrays.
Crea un catplot de tipo stripplot para observar la dispersión de 
duración en diferentes tipos de ejercicio.
Ajusta el orden de categorías y el ancho de puntos.

11. Swarmplot con ajuste de jitter:
Usa el dataset penguins.
Convierte el tamaño de las aletas y el peso corporal a arrays de 
NumPy.
Genera un swarmplot mostrando la relación entre estos valores, 
ajustando el parámetro dodge.

12. Regresión lineal múltiple con visualización avanzada:
Usa el dataset mpg.
Convierte las columnas de potencia (horsepower) y peso (weight) a 
arrays.
Genera un gráfico de regresión múltiple mostrando la relación entre 
peso y potencia con diferentes niveles de confianza.

13. Histogramas superpuestos con diferentes bins:
Crea un DataFrame con distribuciones normales simuladas, 
conviértelas a arrays.
Genera histogramas superpuestos de diferentes grupos con ajuste de 
bins.
Personaliza las transparencias y colores.

14. Plot de violin combinado con stripplot:
Usa el dataset titanic.
Convierte la columna de edad y clase a arrays de NumPy.
Superpone un stripplot sobre un violin plot para observar la distribución 
de edades por clase.

15. Mapa de calor de confusión para clasificación:
Simula un DataFrame con resultados de clasificación, conviértelo a 
array.
Crea un mapa de calor con las tasas de falsos positivos y negativos.
Ajusta la escala de colores y anota la matriz
