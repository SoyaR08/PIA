import pandas as pd

# Cargar los datos del excel en un DataFrame
def load_from_excel(path):

    df = pd.read_excel(path)

    return df.copy()


df = load_from_excel("pandas-exercises\DataFrame\datos_alumnos.xlsx")

print(df)