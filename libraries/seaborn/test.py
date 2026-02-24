import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

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
