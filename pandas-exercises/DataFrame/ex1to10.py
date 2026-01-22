import pandas as pd

df = pd.read_excel('pandas-exercises/DataFrame/datos_alumnos.xlsx')

def test_calculate_final_grade(passed_df, subjects):

    for sub in subjects:
        # Creamos la columna sub
        passed_df[sub] = df[[ # Esto le dice que va a coger las columnas T1, T2 y T3 de sub
            f"{sub} T1", f"{sub} T2", f"{sub} T3"
        ]].mean(axis=1) # Mean hace la media y axis le dice si por fila (1) o por columna (0)

    return passed_df

def calculate_mean(dataframe, fields, desired_axis=1):

    return dataframe[fields].mean(axis=desired_axis)

# 1. Filtra a los alumnos que tienen 20 años o más y muestra sus notas finales.

df_gt_20 = df.loc[df['Edad'] >= 20, [
    "Nombre", "Apellidos", "Edad", 
    "Programación T3", "Base de Datos T3", "Lenguajes T3",
    "Sistemas T3", "Entornos T3"
]]
print(df_gt_20)

# 2. Añade una nueva columna llamada 'Aprobado' que indique si el alumno ha aprobado o no (si su promedio general es mayor o igual a 5).

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

calc_subject_mean = test_calculate_final_grade(calc_subject_mean, ["Lenguajes"])

# Nos quedamos solo con las columnas relevantes
calc_subject_mean = calc_subject_mean[[
    "Nombre", "Apellidos", "Lenguajes"
]]

# En mi caso solo no existe ese alumno, pero hay una alumna con 9.0 exactos
greater_than_nine_df = calc_subject_mean.loc[calc_subject_mean["Lenguajes"] > 9]

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

# 7. Agrupa a los alumnos según si han aprobado o no y cuenta cuántos alumnos hay en cada grupo.

classroom_df = df.copy()

# Promedios por asignatura (por alumno)
classroom_df = test_calculate_final_grade(classroom_df, subjects)

# Promedio general y aprobado
classroom_df["Promedio"] = classroom_df[[
    "Programación", "Base de Datos", "Lenguajes",
    "Sistemas", "Entornos"
]].mean(axis=1) # Hace que la columna Aprobado sea True o False dependiendo si el promedio es mayor o igual a 5

# Nos quedamos solo con las columnas relevantes
classroom_df = classroom_df[[
    "Nombre", "Apellidos", "Promedio"
]]

classroom_df["Aprobado"] = classroom_df[[
    "Promedio"
]].mean(axis=1) >= 5 # Hace que la columna Aprobado sea True o False dependiendo si el promedio es mayor o igual a 5

approved = classroom_df[classroom_df["Aprobado"] == True]
failed = classroom_df[classroom_df["Aprobado"] == False]

print(f"Hay {approved.shape[0]} alumnos aprobados y {failed.shape[0]} alumnos suspensos.")

# 8. Exporta a un archivo CSV los alumnos que han reprobado al menos un módulo.
import os

classroom_df = df.copy()

# Promedios por asignatura (por alumno)
classroom_df = test_calculate_final_grade(classroom_df, subjects)

# Promedio general y aprobado
classroom_df["Promedio"] = calculate_mean(classroom_df, subjects)

# Nos quedamos solo con las columnas relevantes
classroom_df = classroom_df[[
    "Nombre", "Apellidos", "Promedio"
]]

classroom_df["Aprobado"] = classroom_df[[
    "Promedio"
]].mean(axis=1) >= 5 # Hace que la columna Aprobado sea True o False dependiendo si el promedio es mayor o igual a 5

failed = classroom_df.loc[classroom_df["Aprobado"] == False, ["Nombre", "Apellidos", "Promedio"]]

path = "pandas-exercises/DataFrame/csv/alumnos_suspensos.csv"

if not os.path.exists(path):
    with open(path, "x", encoding="utf-8") as f:
        f.write(failed.to_csv(index=False))
    print("Archivo creado y datos guardados.")

else: 
    with open(path, "at", encoding="utf-8") as f:
        f.write(failed.to_csv(index=False))

    print("Datos guardados.")

# 9. Crea un gráfico de dispersión que muestre la relación entre las notas finales de 'Programación' y 'Base de Datos'.
import matplotlib.pyplot as plt
import numpy as np

students_df = df.copy()

students_df = test_calculate_final_grade(students_df, ["Programación", "Base de Datos"])

students_df = students_df[[
    "Nombre", "Apellidos", "Programación", "Base de Datos"
]]

plt.style.use('_mpl-gallery')

# Datos
x = students_df["Programación"]
y = students_df["Base de Datos"]

# size and color:
sizes = np.random.uniform(15, 80, len(x))
colors = np.random.uniform(15, 80, len(x))

# plot
fig, ax = plt.subplots()

ax.scatter(x, y, s=sizes, c=colors, vmin=0, vmax=10)


# Límites y ticks
ax.set(xlim=(0, 10), xticks=np.arange(0, 11),
       ylim=(0, 10), yticks=np.arange(0, 11))

# Etiquetas y título (aquí está la clave)
ax.set_xlabel("Notas Finales de Programación")
ax.set_ylabel("Notas Finales de Base de Datos")
ax.set_title("Relación entre Notas Finales de Programación y Base de Datos")

plt.tight_layout()
plt.show()

# 10. Calcula la desviación estándar del promedio general de las notas.

basic_df = df.copy()

basic_df = test_calculate_final_grade(basic_df, subjects)

cleared_df = basic_df[[
    "Programación", "Base de Datos", "Lenguajes", "Sistemas", "Entornos"]]

std_dev = cleared_df.mean(axis=0).std(axis=0)

print(f"La desviación estándar del promedio general de las notas es: {std_dev}")