from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import math

plt.style.use('_mpl-gallery')

# make the data
np.random.seed(3) # Esto me indica que será siempre lo mismo

## Ejercicio 01  
# Utilizar la función de la raíz cuadrada (librería Math), generar un gráfico (Matplotlib) 
# de dispersión (Random) en el que se muestre 20 números enteros aleatorios entre 
# el 0 y 100 en el eje X y su raíz cuadrada en el eje Y. 


x = np.random.randint(0, 101, 20)

y = np.array([math.sqrt(i) for i in x])

# size and color:
sizes = np.random.uniform(15, 80, len(x))
colors = np.random.uniform(15, 80, len(x))

# plot
fig, ax = plt.subplots()

ax.scatter(x, y, s=sizes, c=colors, vmin=0, vmax=100)

ax.set(xlim=(0, 100), xticks=np.arange(1, 101, 10),
       ylim=(0, 10), yticks=np.arange(1, 11, 1))

plt.tight_layout()
plt.show()

## Ejercicio 02 
# Escribir un programa que pregunte al usuario por las ventas de un rango de años y 
# muestre por pantalla un diagrama de líneas con la evolución de las ventas. 

x = np.arange(2000, 2021)

size = len(x)

y = np.random.randint(10000, 15000, size)

# plot
fig, ax = plt.subplots()

ax.plot(x, y, linewidth=2.0)

ax.set_title("Evolución de ventas entre 2000 y 2020")
ax.set_xlabel("Año")
ax.set_ylabel("Ventas")

ax.set_xticks(x)
ax.tick_params(axis='x', rotation=45)

ax.set(xlim=(1999, 2021),
       ylim=(0, 15000), yticks=np.arange(0, 20001, 5000))

plt.tight_layout()
plt.show()

# Ejercicio 03.  
# Escribir una función que reciba un diccionario con las notas de las asignaturas de 
# un curso y una cadena con el nombre de un color y devuelva un diagrama de barras 
# de las notas en el color dado. 

def create_grades_graphic(grades, color="blue"):
    
    if not isinstance(grades, dict):
       raise Exception("Formato no válido")
    
    x = []
    y = []

    for item in grades.items():
        x.append(item[0])
        y.append(item[1])

    # plot
    fig, ax = plt.subplots()

    ax.bar(x, y, color=color)

    ax.set_title("Comparación de notas por asignatura")
    ax.set_xlabel("Asignatura")
    ax.set_ylabel("Nota")

    plt.tight_layout()
    plt.show()

# colores: red, blue, green, cyan, magenta, yellow, black, white
create_grades_graphic({"Matemáticas": 8, "Lengua": 7, "Inglés": 9}, color="blue")

# Ejercicio 04. 
# Escribir una función que reciba una serie de Pandas con las notas de los alumnos 
# de un curso y devuelva un diagrama de cajas con las notas. El diagrama debe tener 
# el título “Distribución de Notas”

def create_box_plot_grades_graphic(grades, color="blue"):
    
    if not isinstance(grades, pd.Series):
       raise Exception("Formato no válido")
    
    grades.plot.box(
        patch_artist=True, # Permite rellenar la caja
        boxprops=dict(facecolor=color)
    )
    plt.title("Distribución de Notas")
    plt.ylabel("Notas")

    plt.tight_layout()
    plt.show()

# colores: red, blue, green, cyan, magenta, yellow, black, white
create_box_plot_grades_graphic(pd.Series([8, 7, 9, 5, 6, 10]), color="blue")

# Ejercicio 05. 
# Escribir una función que reciba una serie de Pandas con el número de ventas de un 
# producto durante los meses de un trimestre y un título, y cree un diagrama de 
# sectores con las ventas en formato PNG con el título dado. El diagrama debe 
# guardarse en un fichero con el formato PNG y el título dado. 

def create_pie_sells_graphic(sells, months, title):
    
    if not isinstance(sells, pd.Series):
       raise Exception("Formato no válido")
    
    colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, sells.size))

    fig, ax = plt.subplots()

    ax.set_title(title)

    ax.pie(
        sells.values,
        labels=months,
        colors=colors,
        autopct=lambda p: f'{int(p * sum(sells) / 100)}',
        wedgeprops={"linewidth": 1, "edgecolor": "white"}
    )

    ax.axis('off')

    plt.tight_layout()

    # Guardar en PNG
    plt.savefig("result/ventas_mensuales.png", dpi=300)

    plt.show()

data = pd.Series([50000, 30000, 80000])
months = ["Enero", "Febrero", "Marzo"]

create_pie_sells_graphic(data, months, "Ventas 1º Trimestre")

# Ejercicio 06.  
# Escribir una función que reciba una serie de Pandas con el número de ventas de un 
# producto por años y una cadena con el tipo de gráfico a generar (líneas, barras, 
# sectores, áreas) y devuelva un diagrama del tipo indicado con la evolución de las 
# ventas por años y con el título “Evolución del Número de Ventas” 

def create_graphics(data, years, option):
    
    fig, ax = plt.subplots()
    x = years
    y = data

    match option:

        case 'a': # Gráfico de líneas

            ax.plot(x, y, linewidth=2.0)

            ax.set_title(f"Evolución de ventas entre {x.min()} y {x.max()}")
            ax.set_xlabel("Año")
            ax.set_ylabel("Ventas")

            ax.set_xticks(x)
            ax.tick_params(axis='x', rotation=45)
            ax.set(xlim=(x.min() - 1, x.max() + 1),
                ylim=(y.min() - 10000, y.max() + 10000), yticks=y)
            
        case 'b': # Gráfico de barras

            ax.bar(x, y, color="blue")

            ax.set_title(f"Evolución de ventas entre {x.min()} y {x.max()}")
            ax.set_xlabel("Año")
            ax.set_ylabel("Ventas")
            ax.set(xlim=(x.min() - 1, x.max() + 1), xticks=x,
                ylim=(y.min() - 10000, y.max() + 10000), yticks=y)
            

        case 'c': # Gráfico de sectores (tarta)

            colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, y.size))

            fig, ax = plt.subplots()

            ax.set_title(f"Evolución de ventas entre {x.min()} y {x.max()}")

            ax.pie(
                y.values,
                labels=x,
                colors=colors,
                autopct=lambda p: f'{int(p * sum(y) / 100)}',
                wedgeprops={"linewidth": 1, "edgecolor": "white"}
            )

            ax.axis('off')

        case 'd': # Gráfico de áreas
            ax.fill_between(x, y, color="skyblue", alpha=0.5) # alpha controla la transparencia 
            ax.plot(x, y, color="Slateblue", alpha=0.8)       # línea opcional encima del área
            ax.set_title(f"Evolución de ventas entre {x.min()} y {x.max()}")
            ax.set_xlabel("Año")
            ax.set_ylabel("Ventas")
            plt.grid(True)
        
    plt.tight_layout()
    plt.show()


# Ejercicio 07.  
# Escribir una función que reciba un dataframe de Pandas con los ingresos y gastos 
# de una empresa por meses y devuelva un diagrama de líneas con dos líneas, la 
# primera para los ingresos, y la segunda para los gastos. El diagrama debe tener una 
# leyenda identificando la línea de los ingresos y la de los gastos, un título con el 
# nombre “Evolución de Ingresos y Gastos” y el eje Y debe empezar en 0.  

def create_income_outcome_graphics(dataframe):
    
    fig, ax = plt.subplots()

    x = dataframe['month']
    y = dataframe['income']
    y2 = dataframe['outcome']

    plt.ylim(0, 150000)  # eje Y de 0 a 150000

    ax.plot(x, y, marker='o', color='green', label='Ingresos', linewidth=2.0)
    ax.plot(x, y2, marker='o', color='red', label='Gastos' , linewidth=2.0)

    # Títulos y etiquetas
    plt.title('Evolución de Ingresos y Gastos')
    plt.xlabel('Mes')
    plt.ylabel('Monto')
    plt.xticks(rotation=45)  # rotar nombres de meses
    plt.grid(True)
    plt.legend()  # muestra la leyenda
    plt.tight_layout()  # ajusta el gráfico para que no se corten los labels

    plt.show()

xlsx = {
    'month': ['Enero', 'Febrero', 'Marzo', 'Abril', 
              'Mayo', 'Junio', 'Julio', 'Agosto', 
              'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
    'income': np.random.uniform(25000, 120000, size=12),
    'outcome': np.random.uniform(30000, 110000, size=12)
}

df = pd.DataFrame(xlsx)
create_income_outcome_graphics(df)

# Ejercicio 08. 
# El fichero “bancos.csv” contiene las cotizaciones de los principales bancos de 
# España con los siguientes datos:  - - - - - - 
# Empresa: Nombre de la empresa 
# Apertura: Precio de la acción a la apertura de la Bolsa 
# Máximo: Precio máximo de la acción durante la jornada. 
# Mínimo: Precio mínimo de la acción durante la jornada. 
# Cierre: Precio de la acción al cierre de la Bolsa 
# Volumen: Volumen de negocios al cierre de la Bolsa 
# Construir una función que reciba el fichero “bancos.csv” y cree un diagrama de 
# líneas con las series temporales de las cotizaciones de cierre de cada banco. 

def load_csv(path):

    return pd.read_csv(path, parse_dates=["Fecha"]).copy()

def create_bank_wall_street_cotization(dataframe):
    
    fig, ax = plt.subplots()

    for key, value in dataframe:
        print(key)   # el nombre del banco
        print(value.head(3))  # primeras 3 filas de ese banco
        ax.plot(value["Fecha"], value["Cierre"], marker='o', label=key, linewidth=2.0)

    # Títulos y etiquetas
    plt.title('Evolución de Cotizaciones de Bancos')
    plt.xlabel('Fecha')
    plt.ylabel('Cierre (USD)')
    plt.xticks(rotation=45)  # rotar nombres de meses
    plt.grid(True)
    plt.legend()  # muestra la leyenda
    plt.tight_layout()  # ajusta el gráfico para que no se corten los labels

    plt.show()



df = load_csv("bancos.csv")

cleaned_csv = df.loc[:, ["Empresa", "Fecha", "Cierre"]].copy()

test = cleaned_csv.groupby(cleaned_csv["Empresa"])
create_bank_wall_street_cotization(test)

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

df = load_csv("titanic.csv")

ages = df["Age"].dropna()
classes = df["Pclass"].value_counts()

df_survived = df[df["Survived"] == 1]
df_not_survived = df[df["Survived"] == 0]

create_survivors_pie(df)
create_histogram(ages)
create_bar_classes(classes)
create_bar_survival_by_class(df)
create_bar_survival_by_class_cumulative(df)