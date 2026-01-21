import pandas as pd

df = pd.read_excel('pandas-exercises/DataFrame/datos_alumnos.xlsx')

# 1. Filtra a los alumnos que tienen 20 años o más y muestra sus notas finales.

df_gt_20 = df.loc[df['Edad'] >= 20, [
    "Nombre", "Apellidos", "Edad", 
    "Programación T3", "Base de Datos T3", "Lenguajes T3",
    "Sistemas T3", "Entornos T3"
]]
print(df_gt_20)

# 2. Añade una nueva columna llamada 'Aprobado' que indique si el alumno ha aprobado o no (si su promedio general es mayor o igual a 5).

def test_calculate_final_grade(passed_df, subjects):

    for sub in subjects:
        # Creamos la columna sub
        passed_df[sub] = df[[ # Esto le dice que va a coger las columnas T1, T2 y T3 de sub
            f"{sub} T1", f"{sub} T2", f"{sub} T3"
        ]].mean(axis=1) # Mean hace la media y axis le dice si por fila (1) o por columna (0)

    return passed_df
# Copiamos el DataFrame original
new_df = df.copy()

# Promedios por asignatura (por alumno)
subjects = ["Programación", "Base de Datos", "Lenguajes", "Sistemas", "Entornos"]
new_df = test_calculate_final_grade(new_df, subjects)

# Promedio general y aprobado
new_df["Aprobado"] = new_df[[
    "Programación", "Base de Datos", "Lenguajes",
    "Sistemas", "Entornos"
]].mean(axis=1) >= 5 # Hace que la columna Aprobado sea True o False dependiendo si el promedio es mayor o igual a 5

# Nos quedamos solo con las columnas relevantes
new_df = new_df[[
    "Nombre", "Apellidos",
    "Programación", "Base de Datos", "Lenguajes",
    "Sistemas", "Entornos",
    "Aprobado"
]]

print(new_df)

# 3. Calcula la nota máxima de cada módulo y muestra los resultados.

# Copiamos el DataFrame original
calc_aprv = df.copy()

calc_aprv = test_calculate_final_grade(calc_aprv, subjects)

# Nos quedamos solo con las columnas relevantes
calc_aprv = calc_aprv[[
    "Nombre", "Apellidos",
    "Programación", "Base de Datos", "Lenguajes",
    "Sistemas", "Entornos"
]]

notas = calc_aprv[subjects]

idx_max = notas.idxmax(axis=0)
data = {
    "Nombre": calc_aprv.loc[idx_max, "Nombre"].values,
    "Apellidos": calc_aprv.loc[idx_max, "Apellidos"].values,
    "Nota": notas.max(axis=0).values
}

result_df = pd.DataFrame(data, index=subjects)
result_df.index.name = None  # opcional, para que el índice sea limpio

print(result_df)

# 4. Filtra a los alumnos que tienen una nota final superior a 9 en la asignatura de 'Lenguajes'.

# Copiamos el DataFrame original
calc_subject_mean = df.copy()

# Promedios por asignatura (por alumno)
calc_subject_mean["Programación"] = df[[
    "Programación T1", "Programación T2", "Programación T3"
]].mean(axis=1)

calc_subject_mean["Base de Datos"] = df[[
    "Base de Datos T1", "Base de Datos T2", "Base de Datos T3"
]].mean(axis=1)

calc_subject_mean["Lenguajes"] = df[[
    "Lenguajes T1", "Lenguajes T2", "Lenguajes T3"
]].mean(axis=1)

calc_subject_mean["Sistemas"] = df[[
    "Sistemas T1", "Sistemas T2", "Sistemas T3"
]].mean(axis=1)

calc_subject_mean["Entornos"] = df[[
    "Entornos T1", "Entornos T2", "Entornos T3"
]].mean(axis=1)

# Promedio general y aprobado
calc_subject_mean["Aprobado"] = calc_subject_mean[[
    "Programación", "Base de Datos", "Lenguajes",
    "Sistemas", "Entornos"
]].mean(axis=1) >= 5

# Nos quedamos solo con las columnas relevantes
calc_subject_mean = calc_subject_mean[[
    "Nombre", "Apellidos",
    "Programación", "Base de Datos", "Lenguajes",
    "Sistemas", "Entornos",
    "Aprobado"
]]

asignaturas = ["Lenguajes"] # Esto sirve para crear un DataFrame con los datos de las columnas que queremos
notas = calc_subject_mean[asignaturas] # Creamos un nuevo DataFrame con las notas de las asignaturas

idx_max = notas.idxmax(axis=0) # Esto es para obtener la nota o notas más altas
data = { # Creamos un diccionario para usarlo de estructra para el DataFrame
    
    "Nombre": calc_subject_mean.loc[idx_max, "Nombre"].values, # Crea un array con los nombres de los alumnos con la nota más alta
    "Apellidos": calc_subject_mean.loc[idx_max, "Apellidos"].values,
    "Nota": notas.max(axis=0).values # Crea un array con los datos más altos de las filas
}

greater_than_nine_df = pd.DataFrame(data, index=asignaturas)
greater_than_nine_df.index.name = None  # opcional, para que el índice sea limpio

greater_than_nine_df = greater_than_nine_df.loc[greater_than_nine_df["Nota"] > 9]

print(greater_than_nine_df if greater_than_nine_df.empty == False else "No hay alumnos con nota superior a 9 en Lenguajes.")

# 5. Cuenta cuántos alumnos tienen una nota final menor a 5 en la asignatura de 'Sistemas'.

# Copiamos el DataFrame original
calc_subject_mean = df.copy()

# Promedios por asignatura (por alumno)

calc_subject_mean["Sistemas"] = df[[
    "Sistemas T1", "Sistemas T2", "Sistemas T3"
]].mean(axis=1)


# Nos quedamos solo con las columnas relevantes
calc_subject_mean = calc_subject_mean[[
    "Nombre", "Apellidos",
    "Sistemas"
]]

lower_than_five_df = calc_subject_mean.loc[calc_subject_mean["Sistemas"] < 5]

print(lower_than_five_df if lower_than_five_df.empty == False else "No hay alumnos con nota inferior a 5 en Sistemas.")

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