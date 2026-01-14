import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

names = [
    "Ana", "Luis", "Carlos", "Marta", "Sofía", "Jorge",
    "Lucía", "Diego", "Elena", "Pablo", "Carmen", "Raúl"
]
grades = [3, 2, 4, 5, 1, 5, 3, 1, 2, 4, 3, 1]

series = pd.Series(grades, index=names)

percentage_of_each_grade = series.value_counts(normalize=True).sort_index(ascending=True) * 100

print(f"Porcentaje de cada nota: \n{percentage_of_each_grade}\n")

clients_satisfied = series[series >= 4].size * 100 / series.size

print(f"Porcentaje de clientes satisfechos (nota >= 4): {clients_satisfied}%")

series = series.apply(
    lambda x: "Insatisfecho" if x == 1 else x
)

plt.style.use('_mpl-gallery')

# make data:
x = percentage_of_each_grade.index
y = percentage_of_each_grade.values

# plot
fig, ax = plt.subplots()

ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)

max_y = percentage_of_each_grade.max()

yticks = np.arange(0, max_y + 10, 10)

xticks = percentage_of_each_grade.index.tolist()


ax.set(xlim=(1, percentage_of_each_grade.idxmax()), xticks=xticks,
       ylim=(0, max_y + 10), yticks=yticks)

plt.show()