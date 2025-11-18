import json
import random as rd
from datetime import date as dt

def insertData(data):
    products_names = ["Alfombrilla de ratón", "Estantería", "Fregadero", "iPhone", "Tarjeta gráfica", 
                "Monitor", "Ratón", "Funda para portátil", "Air Pods",
                "Cargador de iPhone"]
    possible_dates = range(1, 18)


    for _ in range(10):
        name = rd.choice(products_names)
        products_names.remove(name)
        task = {
            "producto": name,
            "cantidad": rd.randint(1, 10),
            "precio": rd.randint(25, 1500),
            "fecha": f"2025-11-{rd.choice(possible_dates):02d}"
        }

        data.append(task)

"""
This function calculates the real prize (prize * amount) and sums it for each product
@param data a list of dictionaries
"""
def calculateTotalAmount(data):
    return sum(sell["precio"] * sell["cantidad"] for sell in data)

def filterByField(data, field=1, date=dt.today(), productName=""):
    filtered_data = []
    match field:
        case 1:
            for product in data:
                parsed_product_date = dt.fromisoformat(product["fecha"])
                if not isinstance(date, dt):
                    parsed_given_date = dt.fromisoformat(date)
                else:
                    parsed_given_date = date
                if parsed_product_date == parsed_given_date:
                    filtered_data.append(product)
        case 2:
            filtered_data = list(filter(lambda product: productName.replace(" ", "").lower() in product["producto"].replace(" ", "").lower(), data))


    return filtered_data

def tryCatchNumberException(message):
    number = ""
    try:
        number = int(input(message))
    except ValueError:
        while not isinstance(number, int):
            try:
                number = int(input(message))
            except Exception:
                number = ""
    finally:
        return number

def addSell(data):
    product = input("Introduce el nombre del producto vendido: ")
    prize = tryCatchNumberException("Introduce el precio del producto: ")
    quantity = tryCatchNumberException("Introduce la cantidad de Producto vendida: ")
    date = dt.today()

    sell = {
        "producto": product,
        "cantidad": quantity,
        "precio": prize,
        "fecha": date.strftime("%Y-%m-%d")
    }

    data.append(sell)

    return sell

file = open("jsons/sells_register.json", "rt")

json_string = file.read()

data = json.loads(json_string)
insertData(data["ventas"])
print(f"La suma total de todas las ventas es de {calculateTotalAmount(data['ventas'])}€")
print(filterByField(data=data["ventas"], field=1, date="2024-10-27"))
print(addSell(data["ventas"]))

