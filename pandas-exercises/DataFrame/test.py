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

# 6. Obtén al alumno con la nota más alta en la asignatura de 'Programación'.

# Copiamos el DataFrame original
find_prg_max_grade = df.copy()

find_prg_max_grade = test_calculate_final_grade(find_prg_max_grade, ["Programación"])

# Nos quedamos solo con las columnas relevantes
find_prg_max_grade = find_prg_max_grade[[
    "Nombre", "Apellidos",
    "Programación"
]]

print(find_prg_max_grade.sort_values(by="Programación", ascending=False).head(1))