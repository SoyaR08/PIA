import pandas as pd
import os

df = pd.read_excel('datos_alumnos.xlsx')

# Descomentar si el código del ejercicio lo usa (Cntrl + U)
def test_calculate_final_grade(passed_df, subjects):

    for sub in subjects:
        # Creamos la columna sub
        passed_df[sub] = passed_df[[ # Esto le dice que va a coger las columnas T1, T2 y T3 de sub
            f"{sub} T1", f"{sub} T2", f"{sub} T3"
        ]].mean(axis=1) # Mean hace la media y axis le dice si por fila (1) o por columna (0)

    return passed_df

def calculate_mean(dataframe, fields, desired_axis=1):

    return dataframe[fields].mean(axis=desired_axis)

def write_in_excel(dataframe, path):

    if not os.path.exists(path):
        dataframe.to_excel(path, index=False)
        print("Archivo creado y datos guardados.")
    else:
        dataframe.to_excel(path, index=False)
        print("Datos sobrescritos.")

    

# Descomentar si el código del ejercicio lo usa (Cntrl + U)
subjects = ["Programación", "Base de Datos", "Lenguajes", "Sistemas", "Entornos"]

# 20. Exporta un DataFrame a Excel y asegúrate de formatear los valores de las notas con dos decimales.

df_final_excel = df.copy()

df_final_excel = test_calculate_final_grade(df_final_excel, subjects)

df_final_excel = df_final_excel[["Nombre", "Apellidos", "Edad", "Correo"] + subjects]

df_final_excel[subjects] = df_final_excel[subjects].round(2)

path = "excel/df_final_excel.xlsx"

write_in_excel(df_final_excel, path)