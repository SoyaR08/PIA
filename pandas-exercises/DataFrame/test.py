import pandas as pd

df = pd.read_excel('pandas-exercises/DataFrame/datos_alumnos.xlsx')

# Descomentar si el código del ejercicio lo usa (Cntrl + U)
def test_calculate_final_grade(passed_df, subjects):

    for sub in subjects:
        # Creamos la columna sub
        passed_df[sub] = df[[ # Esto le dice que va a coger las columnas T1, T2 y T3 de sub
            f"{sub} T1", f"{sub} T2", f"{sub} T3"
        ]].mean(axis=1) # Mean hace la media y axis le dice si por fila (1) o por columna (0)

    return passed_df

def calculate_mean(dataframe, fields, desired_axis=1):

    return dataframe[fields].mean(axis=desired_axis)

# Descomentar si el código del ejercicio lo usa (Cntrl + U)
subjects = ["Programación", "Base de Datos", "Lenguajes", "Sistemas", "Entornos"]

# 9. Crea un gráfico de dispersión que muestre la relación entre las notas finales de 'Programación' y 'Base de Datos'.
import matplotlib.pyplot as plt
import numpy as np

students_df = df.copy()

students_df = test_calculate_final_grade(students_df, ["Programación", "Base de Datos"])

students_df = students_df[[
    "Nombre", "Apellidos", "Programación", "Base de Datos"
]]

print(students_df)

plt.style.use('_mpl-gallery')

# make the data
# np.random.seed(3)
# x = 4 + np.random.normal(0, 2, 24)
# y = 4 + np.random.normal(0, 2, len(x))

# # size and color:
# sizes = np.random.uniform(15, 80, len(x))
# colors = np.random.uniform(15, 80, len(x))

# # plot
# fig, ax = plt.subplots()

# ax.scatter(x, y, s=sizes, c=colors, vmin=0, vmax=100)

# ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
#        ylim=(0, 8), yticks=np.arange(1, 8))

# plt.show()