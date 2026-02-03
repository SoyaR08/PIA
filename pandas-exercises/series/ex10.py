import pandas as pd

scores = [85, 90, 62, 78, 92, 88, 55, 95]
rounds = [f"Ronda {i}" for i in range(1, 9)]

series = pd.Series(scores, index=rounds)

max_score = series.max()
min_score = series.min()
diff = max_score - min_score

print(f"Puntuación máxima: {max_score}. Puntuación mínima: {min_score}. Diferencia: {diff}.")

print(f"Rondas con puntuación +80: {series[series > 80].to_dict()}")

series.sort_values(ascending=False, inplace=True)

print(series)