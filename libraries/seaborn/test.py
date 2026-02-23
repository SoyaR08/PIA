import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = sns.load_dataset("penguins")

df["bill_length_mm"] = df["bill_length_mm"].fillna(df["bill_length_mm"].mean())
df["bill_depth_mm"] = df["bill_depth_mm"].fillna(df["bill_depth_mm"].mean())
df["flipper_length_mm"] = df["flipper_length_mm"].fillna(df["flipper_length_mm"].mean())
df["body_mass_g"] = df["body_mass_g"].fillna(df["body_mass_g"].mean())

print(df.head())