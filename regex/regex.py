import json
import re

def load_data():

    vehicles_file = open("regex/vehiculos.json", "rt")
    students_file = open("regex/alumnos.json", "rt")

    json_vehicles = vehicles_file.read()
    json_students = students_file.read()

    data_vehicles = json.loads(json_vehicles)
    data_students = json.loads(json_students)

    data = {"alumnos": data_students, "vehiculos": data_vehicles}

    return data


data = load_data()
print(data)