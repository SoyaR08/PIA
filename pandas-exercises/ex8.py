import pandas as pd

rains = [5.2, 3.8, None, 4.0, 6.1, 2.9, None]
days = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

series = pd.Series(rains, index=days, dtype=float)

series = series.apply(
    lambda x: "Sin precipitación" if pd.isna(x) or x == 0 else x
)

precipitations = series[series != "Sin precipitación"]

total_rain = precipitations.sum()

mean_rain = precipitations.mean()

print(f"Total de precipitación semanal: {total_rain} mm. Media diaria de precipitación (días con lluvia): {mean_rain} mm.")

print(f"Días con precipitación mayor a la media: {precipitations[precipitations > mean_rain].to_dict()}")