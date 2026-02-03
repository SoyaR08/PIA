import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

prizes = [9.99, None, 10.99, 7.99, 8.99]
shops = ["Dia", "Carrefour", "Mercadona", "Lidl", "Aldi"]

series = pd.Series(prizes, index=shops, dtype=float)

print(f"Precio más bajo: {series.min()}€ en {series.idxmin()}. Precio más alto: {series.max()}€ en {series.idxmax()}.")

median = series.median()

print(f"Precios mayores a la mediana: {series[series > median].to_dict()}")

series = series.apply(
    lambda x: median if pd.isna(x) else x
)

plt.style.use('_mpl-gallery')

# make data:
x = series.index
y = series.values

# plot
fig, ax = plt.subplots()

ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)

max_y = series.max()

yticks = np.arange(0, max_y + 10, 10)

xticks = series.index.tolist()


ax.set(xlim=(1, series.idxmax()), xticks=xticks,
       ylim=(0, max_y + 10), yticks=yticks)

plt.show()