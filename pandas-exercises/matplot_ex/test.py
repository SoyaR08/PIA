from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import math

plt.style.use('_mpl-gallery')

# make the data
np.random.seed(3) # Esto me indica que será siempre lo mismo


# Ejercicio 09. 
# El fichero “titanic.csv” contiene información sobre los pasajeros del Titanic. Crear 
# un dataframe con Pandas y a partir del mismo, generar los siguientes diagramas;  
# 1. Diagrama de Sectores con los fallecidos y supervivientes 
# 2. Histograma con las edades 
# 3. Diagrama de Barras con el número de personas en cada clase 
# 4. Diagrama de Barras con el número de personas fallecidas y 
# supervivientes en cada clase. 
# 5. Diagrama de Barras con el número de personas fallecidas y 
# supervivientes acumuladas en cada clase.

def load_csv(path):

    return pd.read_csv(path).copy()

def create_survivors_pie(dataframe):
    
    fig, ax = plt.subplots()

    colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, dataframe["Survived"].value_counts().size))


    ax.set_title("Fallecidos y Supervivientes del Titanic")

    ax.pie(
        dataframe["Survived"].value_counts(),
        labels=["Fallecidos", "Supervivientes"],
        colors=colors,
        autopct=lambda p: f'{int(p * sum(dataframe["Survived"].value_counts()) / 100)}',
        wedgeprops={"linewidth": 1, "edgecolor": "white"}
    )

    plt.tight_layout()
    plt.show()


def create_histogram(dataframe):

    fig, ax = plt.subplots()

    ax.set_title("Edades de los pasajeros del Titanic")

    ax.hist(dataframe, bins=20, color='blue', edgecolor='black')

    plt.tight_layout()
    plt.show()

def create_bar_classes(dataframe):

    fig, ax = plt.subplots()

    x = dataframe.index
    y = dataframe.values

    ax.bar(x, y, color="blue")

    ax.set_title(f"Número de personas en cada clase del Titanic")
    ax.set_xlabel("Clase")
    ax.set_ylabel("Número de personas")
    ax.set(xticks=x, yticks=np.arange(0, max(y) + 100, 100))
    plt.tight_layout()
    plt.show()
    
def create_bar_survival_by_class(dataframe):

    fig, ax = plt.subplots()

    survival_by_class = dataframe.groupby("Pclass")["Survived"].value_counts().unstack().fillna(0)

    x = survival_by_class.index
    y1 = survival_by_class[0]  # Fallecidos
    y2 = survival_by_class[1]  # Supervivientes

    ax.bar(x - 0.2, y1, width=0.4, label='Fallecidos', color='red')
    ax.bar(x + 0.2, y2, width=0.4, label='Supervivientes', color='green')

    ax.set_title("Número de personas fallecidas y supervivientes en cada clase")
    ax.set_xlabel("Clase")
    ax.set_ylabel("Número de personas")
    ax.set_xticks(x)
    ax.legend()
    plt.tight_layout()
    plt.show()

def create_bar_survival_by_class_cumulative(dataframe):

    fig, ax = plt.subplots()

    survival_by_class = dataframe.groupby("Pclass")["Survived"].value_counts().unstack().fillna(0)

    x = survival_by_class.index
    y1 = survival_by_class[0]  # Fallecidos
    y2 = survival_by_class[1]  # Supervivientes

    ax.bar(x - 0.2, y1, width=0.4, label='Fallecidos', color='red')
    ax.bar(x + 0.2, y2, width=0.4, label='Supervivientes', color='green')

    ax.set_title("Número de personas fallecidas y supervivientes acumuladas en cada clase")
    ax.set_xlabel("Clase")
    ax.set_ylabel("Número de personas")
    ax.set_xticks(x)
    ax.legend()
    plt.tight_layout()
    plt.show()

df = load_csv("pandas-exercises/matplot_ex/titanic.csv")

ages = df["Age"].dropna()
classes = df["Pclass"].value_counts()

df_survived = df[df["Survived"] == 1]
df_not_survived = df[df["Survived"] == 0]

create_survivors_pie(df)
create_histogram(ages)
create_bar_classes(classes)
create_bar_survival_by_class(df)
create_bar_survival_by_class_cumulative(df)
