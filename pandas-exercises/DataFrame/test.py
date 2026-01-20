import pandas as pd

# 3. Calcula la nota máxima de cada módulo y muestra los resultados.

df = pd.read_excel('pandas-exercises/DataFrame/datos_alumnos.xlsx')

# Copiamos el DataFrame original
calc_aprv = df.copy()

# Promedios por asignatura (por alumno)
calc_aprv["Programación"] = df[[
    "Programación T1", "Programación T2", "Programación T3"
]].mean(axis=1)

calc_aprv["Base de Datos"] = df[[
    "Base de Datos T1", "Base de Datos T2", "Base de Datos T3"
]].mean(axis=1)

calc_aprv["Lenguajes"] = df[[
    "Lenguajes T1", "Lenguajes T2", "Lenguajes T3"
]].mean(axis=1)

calc_aprv["Sistemas"] = df[[
    "Sistemas T1", "Sistemas T2", "Sistemas T3"
]].mean(axis=1)

calc_aprv["Entornos"] = df[[
    "Entornos T1", "Entornos T2", "Entornos T3"
]].mean(axis=1)

# Promedio general y aprobado
calc_aprv["Aprobado"] = calc_aprv[[
    "Programación", "Base de Datos", "Lenguajes",
    "Sistemas", "Entornos"
]].mean(axis=1) >= 5

# Nos quedamos solo con las columnas relevantes
calc_aprv = calc_aprv[[
    "Nombre", "Apellidos",
    "Programación", "Base de Datos", "Lenguajes",
    "Sistemas", "Entornos",
    "Aprobado"
]]

asignaturas = ["Programación", "Base de Datos", "Lenguajes", "Sistemas", "Entornos"]
notas = calc_aprv[asignaturas]

idx_max = notas.idxmax(axis=0)
data = {
    "Nombre": calc_aprv.loc[idx_max, "Nombre"].values,
    "Apellidos": calc_aprv.loc[idx_max, "Apellidos"].values,
    "Nota": notas.max(axis=0).values
}

result_df = pd.DataFrame(data, index=asignaturas)
result_df.index.name = None  # opcional, para que el índice sea limpio

print(result_df)