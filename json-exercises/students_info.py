import json
import random as rd
from datetime import date as dt

def insert10Students(data):

    students_names = ["Rafa", "Joseca", "Rogolo", "Kike", "Jesús", "Carlos",
                      "Mario", "Iván", "Parra", "Luis"]
    
    students_grades = range(40, 100)
    students_ages = range(19, 24)
    students_cities = ["Sevilla", "Los Villares", "Madrid"]
   
    for _ in range(10):
        name = rd.choice(students_names)
        students_names.remove(name)

        student = {
            "nombre": name,
            "edad": rd.choice(students_ages),
            "calificacion": rd.choice(students_grades),
            "ciudad": rd.choice(students_cities)
        }

        data.append(student)
    
def filterPassedStudents(data):
    filtered_data = list(filter(lambda student: student["calificacion"] >= 50, data))
    return filtered_data

def findStudentByName(data, studentName):
    filtered_data = list(filter(lambda student: student["nombre"].replace(" ", "").lower() in studentName.replace(" ", "").lower(), data))

    return filtered_data[0] if len(filtered_data) > 0 else None

def removeStudent(data, studentName):
    student = findStudentByName(data, studentName)
    isThere = True if not isinstance(student, None.__class__) else False

    if isThere:
        data.remove(student)
        return f"Se ha eliminado a {student}"
    
    else:
        return "No se ha encontrado al estudiante"
    
def addStudent(data):
    name = input("Introduce el nombre del nuevo alumno: ")
    age = ""
    mark = 0
    while not isinstance(age, int):
        try:
            age = int(input("Introduce la edad del estudiante: "))
        except Exception:
            pass

    city = input("Introduce la ciudad del nuevo alumno: ")

    student = {
        "nombre": name,
        "edad": age,
        "calificacion": mark,
        "ciudad": city
    }

    data.append(student)

    return f"Se ha añadido al estudiante {student}"

    

file = open("json-exercises/jsons/students_info.json", "rt")

json_string = file.read()

data = json.loads(json_string)
insert10Students(data["alumnos"])
print(filterPassedStudents(data["alumnos"]))
print(removeStudent(data["alumnos"], "Luis"))
print(addStudent(data["alumnos"]))