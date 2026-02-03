import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

visits = [120, None, 150, 90, 200, None, 170, 120, 160, None]

days = ["día1", "día2", "día3", "día4", "día5", "día6", "día7", "día8", "día9", "día10"]

series = pd.Series(visits, index=days, dtype=float)

total_visits = series.sum()
mean_visits = series.mean()

print(f"Número total de visitas: {total_visits}. Media diaria de visitas (días con datos): {mean_visits}.")

print(f"Días con visitas mayores a la media: {series[series > mean_visits].to_dict()}")

series_changed = series.apply(
    lambda x: "Baja visita" if pd.isna(x) or x < 50 else x
)

print(series_changed)

plt.style.use('_mpl-gallery')

# make data:
x = series.index
y = series.values

# plot
fig, ax = plt.subplots()

ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)

max_y = series.max()

print(max_y)

yticks = np.arange(0, max_y + 10, 210)

xticks = series.index.tolist()


ax.set(xlim=(1, series.idxmax()), xticks=xticks,
       ylim=(0, max_y + 10), yticks=yticks)

plt.show()