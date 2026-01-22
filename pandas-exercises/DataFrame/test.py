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

# 10. Calcula la desviación estándar del promedio general de las notas.

basic_df = df.copy()

basic_df = test_calculate_final_grade(basic_df, subjects)

cleared_df = basic_df[[
    "Programación", "Base de Datos", "Lenguajes", "Sistemas", "Entornos"]]

std_dev = cleared_df.mean(axis=0).std(axis=0)

print(f"La desviación estándar del promedio general de las notas es: {std_dev}")
