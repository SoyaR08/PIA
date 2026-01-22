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

def write_in_excel(dataframe, path):

    if not os.path.exists(path):
        dataframe.to_excel(path, index=False)
        print("Archivo creado y datos guardados.")
    else:
        dataframe.to_excel(path, index=False)
        print("Datos sobrescritos.")


subjects = ["Programación", "Base de Datos", "Lenguajes", "Sistemas", "Entornos"]

# 11. Carga un archivo Excel con datos de alumnos en un DataFrame y muestra los primeros 5 registros.

loaded_df = df.copy()

print(loaded_df.head())

# 12. Guarda una copia del archivo Excel en un archivo CSV.

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

# 13. Filtra los alumnos que tienen una edad mayor a 22 años y guarda este subconjunto en un nuevo archivo Excel.

df_gt22 = df.copy().loc[df['Edad'] > 22]

path = "pandas-exercises/DataFrame/excel/df_gt22.xlsx"

if not os.path.exists(path):
    df_gt22.to_excel(path, index=False)
    print("Archivo creado y datos guardados.")
else:
    df_gt22.to_excel(path, index=False)
    print("Datos sobrescritos.")


print(df_gt22)

# 14. Modifica las notas de los alumnos en el DataFrame y guarda los cambios en una nueva versión del archivo CSV.

df_from_csv = pd.read_csv('pandas-exercises/DataFrame/csv/df_copy.csv')

columns = ["Programación T1", "Programación T2", "Programación T3",
"Base de Datos T1", "Base de Datos T2", "Base de Datos T3",
"Lenguajes T1", "Lenguajes T2", "Lenguajes T3",
"Sistemas T1", "Sistemas T2", "Sistemas T3",
"Entornos T1", "Entornos T2", "Entornos T3"]

df_from_csv[columns] = (df[columns] + 1).clip(upper=10)

path = "pandas-exercises/DataFrame/csv/df_mod.csv"

if not os.path.exists(path):
    with open(path, "x", encoding="utf-8") as f:
        f.write(df_from_csv.to_csv(index=False))
    print("Archivo creado y datos guardados.")

else: 
    with open(path, "wt", encoding="utf-8") as f:
        f.write(df_from_csv.to_csv(index=False))

    print("Datos guardados.")


print(df_from_csv)

# 15. Lee un archivo CSV con datos de alumnos y calcula el promedio de las notas de un módulo específico.

df_from_csv = pd.read_csv('pandas-exercises/DataFrame/csv/df_copy.csv')

df_from_csv = test_calculate_final_grade(df_from_csv, subjects)

cleaned_df = df_from_csv[["Nombre", "Apellidos", "Correo", "Edad"] + subjects]

module = "Programación"

module_mean = calculate_mean(cleaned_df, [module], desired_axis=0)

print(module_mean)

# 16. Agrupa a los alumnos por edad y guarda el promedio de cada grupo en un nuevo archivo Excel.

df_ages = df.copy()

df_ages = test_calculate_final_grade(df_ages, subjects)

desired_columns = ["Edad",
    "Programación", "Base de Datos", "Lenguajes",
    "Sistemas", "Entornos"]

df_ages["Promedio"] = calculate_mean(df_ages, desired_columns[1:])

df_ages = df_ages[["Edad", "Promedio"]]

df_ages = df_ages.groupby('Edad').mean(numeric_only=True)

path = "pandas-exercises/DataFrame/excel/df_ages.xlsx"

if not os.path.exists(path):
    df_ages.to_excel(path, index=True)
    print("Archivo creado y datos guardados.")
else:
    df_ages.to_excel(path, index=True)
    print("Datos sobrescritos.")

# 17. Añade una nueva columna al archivo CSV para indicar si el alumno está en el grupo de honor (promedio general superior a 9).

df_final = pd.read_csv('pandas-exercises/DataFrame/csv/df_copy.csv')

df_final = test_calculate_final_grade(df_final, subjects)

df_final = df_final[["Nombre", "Apellidos", "Correo", "Edad"] + subjects]

df_final["Promedio"] = df_final[subjects].mean(axis=1)

df_final["Grupo de Honor"] = df_final["Promedio"] > 9

path = "pandas-exercises/DataFrame/csv/df_final.csv"

if not os.path.exists(path):
    with open(path, "x", encoding="utf-8") as f:
        f.write(df_final.to_csv(index=False))
    print("Archivo creado y datos guardados.")

else: 
    with open(path, "wt", encoding="utf-8") as f:
        f.write(df_final.to_csv(index=False))

    print("Datos guardados.")


print(df_final)

# 18. Carga un archivo Excel, calcula la nota mínima de cada módulo y guarda el resultado en un archivo CSV.

df_min_module_grade = pd.read_csv('pandas-exercises/DataFrame/csv/df_copy.csv')

df_min_module_grade = test_calculate_final_grade(df_min_module_grade, subjects)

df_min_module_grade = df_min_module_grade[["Nombre", "Apellidos", "Correo", "Edad"] + subjects]

min_grades = df_min_module_grade[subjects].min()

path = "pandas-exercises/DataFrame/csv/df_min_module_grade.csv"

if not os.path.exists(path):
    with open(path, "x", encoding="utf-8") as f:
        f.write(min_grades.to_csv(index=True))
    print("Archivo creado y datos guardados.")

else: 
    with open(path, "wt", encoding="utf-8") as f:
        f.write(min_grades.to_csv(index=True))

    print("Datos guardados.")

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

write_in_excel(df_merged, path)

# 20. Exporta un DataFrame a Excel y asegúrate de formatear los valores de las notas con dos decimales.

df_final_excel = df.copy()

df_final_excel = test_calculate_final_grade(df_final_excel, subjects)

df_final_excel = df_final_excel[["Nombre", "Apellidos", "Edad", "Correo"] + subjects]

df_final_excel[subjects] = df_final_excel[subjects].round(2)

path = "pandas-exercises/DataFrame/excel/df_final_excel.xlsx"

write_in_excel(df_final_excel, path)