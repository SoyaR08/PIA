import pandas as pd
from db import df_alumnos as df

# 1. Filtra a los alumnos que tienen 20 años o más y muestra sus notas finales.

df_gt_20 = df.loc[df['Edad'] >= 20, [
    "Nombre", "Apellidos", "Edad", 
    "Programación T3", "Base de Datos T3", "Lenguajes T3",
    "Sistemas T3", "Entornos T3"
]]
print(df_gt_20.to_dict())