import pandas as pd
import os

df = pd.read_excel('pandas-exercises/DataFrame/datos_alumnos.xlsx')

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

# Descomentar si el código del ejercicio lo usa (Cntrl + U)
subjects = ["Programación", "Base de Datos", "Lenguajes", "Sistemas", "Entornos"]

# 19. Fusiona los datos de dos archivos Excel con datos de alumnos y guarda el resultado combinado en un nuevo archivo.

df_excel1 = pd.read_excel('pandas-exercises/DataFrame/datos_alumnos.xlsx')
df_excel2 = pd.read_excel('pandas-exercises/DataFrame/excel/df_final_excel.xlsx')

fields_to_merge = ["Nombre", "Apellidos", "Correo", "Edad"]

df_merged = pd.merge(df_excel1, df_excel2, on=fields_to_merge, how='outer')

df_merged.rename(columns={
    "Programación": "Programación Nota Final",
    "Base de Datos": "Base de Datos Nota Final",
    "Lenguajes": "Lenguajes Nota Final",
    "Sistemas": "Sistemas Nota Final",
    "Entornos": "Entornos Nota Final"
}, inplace=True)

path = "pandas-exercises/DataFrame/excel/df_merged.xlsx"

if not os.path.exists(path):
    df_merged.to_excel(path, index=False)
    print("Archivo creado y datos guardados.")
else:
    df_merged.to_excel(path, index=False)
    print("Datos sobrescritos.")