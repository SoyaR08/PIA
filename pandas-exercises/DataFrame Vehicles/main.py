import pandas as pd
from datetime import date

# Carga los datos del excel en un DataFrame
def load_from_excel(path):

    df = pd.read_excel(path)

    return df.copy()

# Rellena los datos faltantes por columna
def fill_data_per_column(df, column):

   
    sub_values = {
        "Marca": "Desconocida",
        "Modelo": "Desconocido",
        "Año": date.today().year,
        "Color": "De Fábrica",
        "Kilómetros": 0,
        "Motor": "Desconocido",
        "Combustible": "Gasolina",
        "Tamaño (m3)": 15,
        "N_Ocupantes": 5,
        "Peso (kg)": 3000,
        "C_Maletero (L)": 300,
        "Potencia (CV)": 200,
        "Emisiones (g/km)": 0,
        "Autonomía (WLTP km)": 10000,
        "Precio (€)": 20000
    }

    return df[column].fillna(sub_values[column])

# Crea un DataFrame con las estadísticas solicitadas
def create_stats_excel(df):

    prices_mean = df["Precio (€)"].mean()
    km_mean = df["Kilómetros"].mean()

    df_stats = pd.DataFrame(
        {"Precio (€)": prices_mean, "Kilómetros": km_mean}, 
        index=["Media"]
    )

    return df_stats

# Crea el archivo excel con las estadísticas
def create_excel_file(df, path):

    with pd.ExcelWriter(path) as writer:
        stats_df = create_stats_excel(df)
        stats_df.to_excel(writer, sheet_name="Estadísticas", index=True)

df = load_from_excel("excel/data.xlsx")

columns_with_missing_values = []

for col in df.columns:
    missing_count = df[col].isna().sum()
    if missing_count > 0:
        columns_with_missing_values.append(col)

for col in columns_with_missing_values:
    df[col] = fill_data_per_column(df, col)

create_excel_file(df, "excel_result/vehicle_stats.xlsx")
print("Archivo 'vehicle_stats.xlsx' creado con éxito en la carpeta 'excel_result'.")

print("Ordenando por Precio (€) de menor a mayor...")
df.sort_values(by="Precio (€)", ascending=True, inplace=True)
print(df)

print("Ordenando por Año de menor a mayor...")
df.sort_values(by="Año", ascending=True, inplace=True)
print(df)

