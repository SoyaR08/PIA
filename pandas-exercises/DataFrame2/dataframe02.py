import pandas as pd
import numpy as np

# Función para filtrar alumnos suspensos
def filter_failed_students(df):

    result_list = [] # Lista de diccionarios con la que crearemos el DataFrame

    # Recorremos cada fila del DataFrame
    for y, x in df.iterrows():

        student = x["Alumno"]

        failed = [col for col in df.columns[1:] if x[col] < 5] # Buscamos las asignaturas suspensas

        if failed:
            result_list.append({ # Añadimos a la lista
                "Alumno": student,
                "Asignaturas Suspensas": ", ".join(failed)
            })

    return pd.DataFrame(result_list)

# Función para filtrar alumnos con sobresalientes
def filter_excellent(df):

    result_list = [] # Lista de diccionarios con la que crearemos el DataFrame

    # Recorremos cada fila del DataFrame
    for y, x in df.iterrows():

        student = x["Alumno"]

        excellent = [col for col in df.columns[1:] if x[col] >= 9] # Buscamos las asignaturas sobresalientes

        if excellent:
            result_list.append({ # Añadimos a la lista
                "Alumno": student,
                "Asignaturas con sobresaliente": ", ".join(excellent)
            })

    return pd.DataFrame(result_list)

def create_blanck_df(students_names):
    array = np.array([1,2,3,4,5,6,7,8,9,10,np.nan])


    notas = {
        "Alumno": students_names,
        "BD": np.random.choice(array, len(students_names)),
        "PR": np.random.choice(array, len(students_names)),
        "SI": np.random.choice(array, len(students_names)),
        "LM": np.random.choice(array, len(students_names)),
        "ED": np.random.choice(array, len(students_names)),
    }

    df = pd.DataFrame(notas)

    # Redondeamos las notas a 1 decimal, ignorando NaN
    for col in df.columns[1:]:
        df[col] = df[col].apply(lambda x: round(x, 1) if pd.notnull(x) else x)

    return df

# Mostrar más filas
pd.set_option('display.max_rows', 300)  

# Mostrar más columnas
pd.set_option('display.max_columns', 500) 

# Nombres alumnos
nombres_alumnos = [
    "Juan Pérez", "María López", "Carlos García", "Ana Fernández",
    "Luis Martínez", "Sofía Gómez", "Miguel Rodríguez", "Laura Sánchez",
    "José Torres", "Lucía Morales", "Andrés Herrera", "Carmen Ruiz",
    "Raúl Castro", "Elena Jiménez", "Javier Gil", "Isabel Romero",
    "Hugo Ortiz", "Sara Delgado", "Pablo Ramírez", "Marta Vargas"
]

# Generar notas aleatorias 
notas = {
    "Alumno": nombres_alumnos,
    "Base de Datos": np.random.uniform(1, 10, 20).round(1),
    "Programación": np.random.uniform(1, 10, 20).round(1),
    "Sistemas Informáticos": np.random.uniform(1, 10, 20).round(1),
    "Lenguajes de Marcas": np.random.uniform(1, 10, 20).round(1),
    "Entornos de Desarrollo": np.random.uniform(1, 10, 20).round(1),
}

# DataFrame
df_alumnos = pd.DataFrame(notas)

# Renombrar columnas

renamed_columns = ["Alumno", "BD", "PR", "SI", "LM", "ED"]

df_alumnos.columns = renamed_columns

# Filtrado

# Filtrado por suspensos

print(filter_failed_students(df_alumnos))

# Filtrado por suspensos en Programación
df_failed_pg = df_alumnos.loc[df_alumnos["PR"] < 5, ["Alumno", "PR"]]

print(df_failed_pg)

# Filtrado por sobresalientes
df_excellent = filter_excellent(df_alumnos)

print(df_excellent)

# Filtrado por dos alumnas
students = ["Marta Vargas", "Carmen Ruiz"]

df = df_alumnos.loc[df_alumnos["Alumno"].isin(students)]
print(df)

# Pivotar el DataFrame

df_pivot = df_alumnos.melt(id_vars=["Alumno"], var_name="Asignatura", value_name="Nota")
print(df_pivot)

# Ordenar el DataFrame

df_alumnos.sort_values(by=["Alumno"], ascending=True, inplace=True)
print(df_alumnos)

df_alumnos.sort_values(by=["PR"], ascending=True, inplace=True)
print(df_alumnos)

df_alumnos.sort_values(by=["BD"], ascending=False, inplace=True)
print(df_alumnos)

# Agrupar el DataFrame

df_alumnos["Media"] = df_alumnos[["BD", "PR", "SI", "LM", "ED"]].mean(axis=1)

print(f"{df_alumnos}\n")

df_mean_subjects = df_alumnos[["BD", "PR", "SI", "LM", "ED"]].mean(axis=0)

print(f"{df_mean_subjects}\n")

df_best_student = df_alumnos.loc[df_alumnos["Media"] == df_alumnos["Media"].max(), ["Alumno", "Media"]]
print(df_best_student)

# Concatenar

df_alumnos.sort_index(inplace=True)
df_alumnos2 = df_alumnos.copy()

# Introducir NaN aleatoriamente (aprox. 20% de los datos)
for col in df_alumnos2.columns[1:]:  # excluimos la columna "Alumno"
    df_alumnos2.loc[df_alumnos2.sample(frac=0.2).index, col] = np.nan

print("DataFrame con algunos valores faltantes:")
print(df_alumnos2)

# --- Concatenar los dos DataFrames ---
df_concatenado = pd.concat([df_alumnos, df_alumnos2], ignore_index=True)
print("\nDataFrame concatenado (manteniendo NaN):")
print(df_concatenado)

# --- Eliminar filas que tengan NaN ---
df_sin_nan = df_concatenado.dropna()
print("\nDataFrame concatenado sin filas con NaN:")
print(df_sin_nan)



