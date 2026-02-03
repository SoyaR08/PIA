import pandas as pd
from validations import validate_seven_numeric_items as validate_data
import matplotlib.pyplot as plt

content = input("Introduce los datos de temperatura de los últimos 7 días en el siguiente formato: dia1,dia2,dia3,dia4,dia5,dia6,dia7 ")

if not validate_data(content):
    print("Datos inválidos. Por favor, inténtalo de nuevo.")
    stopped = False
    while not stopped:
        content = input("Introduce los datos de temperatura de los últimos 7 días en el siguiente formato: dia1,dia2,dia3,dia4,dia5,dia6,dia7 ")
        if validate_data(content):
            stopped = True

series = pd.Series([float(x) for x in content.split(",")], index=["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"], dtype=float)

mean = series.mean()

print(mean)
print(f"Temperatura máxima: {series.idxmax()}, con {series.max()}ºC")
print(f"Días con temperaturas mayores a la media:\n{series.gt(25).to_dict()}")
series = series.apply(lambda x: 25 if pd.isna(x) else x)

plt.title("Temperaturas de la semana")
plt.plot(series.index, series.values, marker='o')
plt.show()