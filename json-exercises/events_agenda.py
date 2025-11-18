import json
import random as rd
from datetime import date as dt

def addNewEvents(data):

    event_titles = ["NerdearLA", "Mangafest", "Comic Con", "Concierto de Anuel AA"]
    event_possible_days = range(dt.today().day, 31)
    event_possible_months = range(dt.today().month, 12)
    event_locations = ["Madrid", "Barcelona", "Sevilla", "Valencia"]
    organizers = ["Eventos S.A.", "Conciertos y Más", "Mundo Friki"]

    for _ in range(4):
        title = rd.choice(event_titles)
        event_titles.remove(title)
        organizer = rd.choice(organizers)
        event = {
            "titulo": title,
            "fecha": f"2024-{rd.choice(event_possible_months):02d}-{rd.choice(event_possible_days):02d}",
            "ubicacion": rd.choice(event_locations),
            "organizador": organizer
        }

        data.append(event)

def filterByField(data, location="", field=0, date=dt.today()):
    filtered_data = []

    match field:

        case 0:
            for event in data:
                parsed_event_date = dt.fromisoformat(event["fecha"])
                if not isinstance(date, dt):
                    parsed_given_date = dt.fromisoformat(date)
                else:
                    parsed_given_date = date
                if parsed_event_date == parsed_given_date:
                    filtered_data.append(event)

        case 1:
            filtered_data = list(filter(lambda event: location.replace(" ", "").lower() in event["ubicacion"].replace(" ", "").lower(), data))

    return filtered_data

def removePastEvents(data):
    today = dt.today()
    count = 0
    for event in data:
        event_date = dt.fromisoformat(event["fecha"])
        if event_date < today:
            data.remove(event)
            count += 1

    return f"Se han eliminado {count} eventos pasados."

    

file = open("json-exercises/jsons/data.json", "rt")

json_string = file.read()

data = json.loads(json_string)

addNewEvents(data["eventos"])
print(filterByField(data=data["eventos"], date="2024-11-15"))
print(removePastEvents(data["eventos"]))
# print(data["eventos"])