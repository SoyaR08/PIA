import pandas as pd
# import matplotlib.pyplot as plt

quantities = [20, 18, 23, 12, 7, None, 4, 19]
names = ["Manzanas", "Naranjas", "Plátanos", "Peras", "Uvas", "Mangos", "Kiwis", "Cervezas"]

series = pd.Series(quantities, index=names, dtype=object)
print(f"Productos escasos: {series.lt(10).to_dict()}")
series = series.apply(
    lambda x: 0 if pd.isnull(x) else x
)
series.sort_values(ascending=False, inplace=True)
print(series)