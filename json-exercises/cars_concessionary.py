import json
import random as rd
from datetime import date as dt

def insertCars(data):

    cars_names = ["Porshe", "Pagani", "Ferrari", "Honda", "Renault", "Suzuki",
                      "Volskwagen", "Seat"]
    
    cars_prize = range(20000, 100000)
    cars_years = range(2020, 2025)
    cars_models = ["Zonda", "911", "F40", "Bitara", "Golf", "Ibiza"]
   
    for _ in range(10):
        name = rd.choice(cars_names)

        student = {
            "marca": name,
            "modelo": rd.choice(cars_models),
            "precio": rd.choice(cars_prize),
            "year": rd.choice(cars_years)
        }

        data.append(student)

def calcMediaValue(data):
    return sum(c["precio"] for c in data) / len(data)

def filterByBrand(data, brand):
    return list(filter(lambda car: brand.replace(" ", "").lower() in car["marca"].replace(" ", "").lower(), data))

def findCarByBrand(data, given_car):
    filtered_data = list(filter(lambda car: car == given_car, data))

    return filtered_data[0] if len(filtered_data) > 0 else None

def updatePrize(data, car):
    car = findCarByBrand(data, car)
    isThere = True if not isinstance(car, None.__class__) else False

    if isThere:
        data.remove(car)
        return f"Se ha eliminado a {car}"
    
    else:
        return "No se ha encontrado al estudiante"

file = open("json-exercises/jsons/cars_concessionary.json", "rt")

json_string = file.read()

data = json.loads(json_string)
insertCars(data["coches"])
print(calcMediaValue(data["coches"]))
print(filterByBrand(data["coches"], "ferrari"))
