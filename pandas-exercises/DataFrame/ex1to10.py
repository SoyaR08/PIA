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

# Copiamos el DataFrame original
new_df = df.copy()

# Promedios por asignatura (por alumno)

# Creamos la columna Programación
new_df["Programación"] = df[[ # Esto le dice que va a coger las columnas T1, T2 y T3 de Programación
    "Programación T1", "Programación T2", "Programación T3"
]].mean(axis=1) # Mean hace la media y axis le dice si por fila (1) o por columna (0)

new_df["Base de Datos"] = df[[
    "Base de Datos T1", "Base de Datos T2", "Base de Datos T3"
]].mean(axis=1)

new_df["Lenguajes"] = df[[
    "Lenguajes T1", "Lenguajes T2", "Lenguajes T3"
]].mean(axis=1)

new_df["Sistemas"] = df[[
    "Sistemas T1", "Sistemas T2", "Sistemas T3"
]].mean(axis=1)

new_df["Entornos"] = df[[
    "Entornos T1", "Entornos T2", "Entornos T3"
]].mean(axis=1)

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
