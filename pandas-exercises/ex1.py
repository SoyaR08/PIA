import pandas as pd
from validations import validate_seven_numeric_items as validate_data

content = input("Introduce los datos de venta de los últimos 7 días en el siguiente formato: dia1,dia2,dia3,dia4,dia5,dia6,dia7 ")

if not validate_data(content):
    print("Datos inválidos. Por favor, inténtalo de nuevo.")
    stopped = False
    while not stopped:
        content = input("Introduce los datos de venta de los últimos 7 días en el siguiente formato: dia1,dia2,dia3,dia4,dia5,dia6,dia7 ")
        if validate_data(content):
            stopped = True

series = pd.Series([float(x) for x in content.split(",")], index=["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"], dtype=float)

mean = series.mean()

print(f"Promedio de ventas: {mean}")
print(f"Ventas totales: {series.sum()}")
print(f"Día de más ventas: {series.idxmax()}, con {series.max()} ventas")
print(f"Días con ventas mayores a la media:\n{series[series > mean].to_dict()}")