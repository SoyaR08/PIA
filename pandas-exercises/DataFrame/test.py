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

# Descomentar si el código del ejercicio lo usa (Cntrl + U)
subjects = ["Programación", "Base de Datos", "Lenguajes", "Sistemas", "Entornos"]

# 8. Exporta a un archivo CSV los alumnos que han reprobado al menos un módulo.

# Copiamos el DataFrame original
calc_subject_mean = df.copy()

calc_subject_mean = test_calculate_final_grade(calc_subject_mean, ["Lenguajes"])

# Nos quedamos solo con las columnas relevantes
calc_subject_mean = calc_subject_mean[[
    "Nombre", "Apellidos", "Lenguajes"
]]

# En mi caso solo no existe ese alumno, pero hay una alumna con 9.0 exactos
greater_than_nine_df = calc_subject_mean.loc[calc_subject_mean["Lenguajes"] > 9]

print(greater_than_nine_df if greater_than_nine_df.empty == False else "No hay alumnos con nota superior a 9 en Lenguajes.")