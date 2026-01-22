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

# 13. Filtra los alumnos que tienen una edad mayor a 22 años y guarda este subconjunto en un nuevo archivo Excel.

import os

df_copy = df.copy()

path = "pandas-exercises/DataFrame/csv/df_copy.csv"

if not os.path.exists(path):
    with open(path, "x", encoding="utf-8") as f:
        f.write(df_copy.to_csv(index=False))
    print("Archivo creado y datos guardados.")

else: 
    with open(path, "wt", encoding="utf-8") as f:
        f.write(df_copy.to_csv(index=False))

    print("Datos guardados.")


