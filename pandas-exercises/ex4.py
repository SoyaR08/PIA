import pandas as pd
import matplotlib.pyplot as plt

temperatures = [8, 8, 10, 12, 6]

series = pd.Series(temperatures, index=["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"], dtype=float)
total_hours = series.sum()
print(f"Total de horas trabajadas: {total_hours} horas")
print(f"Días en los que el empleado trabajó más de 8 horas:\n{series.gt(8).to_dict()}")
series = series.apply(
    lambda x: "Medio tiempo" if x < 8 else "Extra" if x > 8 else "Normal"
)

print(series)

plt.title("Horas trabajadas durante la semana")
plt.plot(series.index, series.values, marker='o')
plt.show()