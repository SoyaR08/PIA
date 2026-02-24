import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 10. Catplot para variables categóricas con ajuste de orden:
# Usa el dataset exercise.
# Convierte la columna de duración y tipo de ejercicio a arrays.
# Crea un catplot de tipo stripplot para observar la dispersión de 
# duración en diferentes tipos de ejercicio.
# Ajusta el orden de categorías y el ancho de puntos.

# Simular matriz de confusión
conf_matrix = np.array([[85, 15],
                        [10, 90]])

df_conf = pd.DataFrame(
    conf_matrix,
    index=["Real Negativo", "Real Positivo"],
    columns=["Pred Negativo", "Pred Positivo"]
)

print(conf_matrix)

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