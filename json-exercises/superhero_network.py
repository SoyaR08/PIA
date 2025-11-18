import json
import random as rd
from datetime import date as dt

def addNewHeroes(data):

    heroes_aliases = ["Spider-Man", "Batman", "Superman", "Iron Man", "Capitán América"]
    heroes_teams = ["Avengers", "Justice League", "Justice League", "Avengers", "Avengers"]
    habilities = [["Superfuerza", "Sentido del peligro", 
                   "Trepar muros", "Agilidad", "Producir telarañas"], ["Inteligencia", "Habilidad en combate", "Intuición detective"],
                  ["Superfuerza", "Vuelo", "Visión de rayos X"], ["Inteligencia", "Vuelo", "Armadura avanzada"], 
                  ["Habilidad en combate", "Agilidad", "Liderazgo"]]
    cities = ["Nueva York", "Gotham", "Metrópolis", "Los Ángeles", "Washington D.C."]

    for i in range(5):
        alias = heroes_aliases[i]
        team = heroes_teams[i]
        ability = habilities[i]
        city = cities[i]
        hero = {
            "alias": alias,
            "equipo": team,
            "habilidades": ability,
            "ciudad": city
        }

        data.append(hero)

def filterByField(data, field, value):
    filtered_data = []
    match field:
        case 0:
            filtered_data = list(filter(lambda hero: value.replace(" ", "").lower() in hero["ciudad"].replace(" ", "").lower(), data))
        case 1:
            filtered_data = list(filter(lambda hero: value.replace(" ", "").lower() in hero["equipo"].replace(" ", "").lower(), data))

    return filtered_data

def listUniqueHabilities(data):

    habilites = set()
    habilities_collection = []

    hab_times = {}

    for hero in data:
        hability_list = hero["habilidades"]

        for hab in hability_list:
            if hab not in habilites:
                habilites.add(hab)
            habilities_collection.append(hab)

    for hab in habilites:
        times = 0
        for hab2 in habilities_collection:
            if hab == hab2:
                times += 1

        hab_times[hab] = times

    unique_habilities = list(filter(lambda hab: hab_times[hab] == 1, hab_times))

    return unique_habilities


file = open("json-exercises/jsons/data.json", "rt")

json_string = file.read()

data = json.loads(json_string)

addNewHeroes(data["superheroes"])
print(filterByField(data["superheroes"], 0, "nuevayork"))
print(listUniqueHabilities(data["superheroes"]))
# print(data["superheroes"])