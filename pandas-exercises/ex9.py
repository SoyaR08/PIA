import pandas as pd

visits = [120, None, 150, 90, 200, None, 170, 120, 160, None]

days = ["día1", "día2", "día3", "día4", "día5", "día6", "día7", "día8", "día9", "día10"]

series = pd.Series(visits, index=days, dtype=float)

total_visits = series.sum()
mean_visits = series.mean()

print(f"Número total de visitas: {total_visits}. Media diaria de visitas (días con datos): {mean_visits}.")

print(f"Días con visitas mayores a la media: {series[series > mean_visits].to_dict()}")

series = series.apply(
    lambda x: "Baja visita" if pd.isna(x) or x < 50 else x
)

print(series)