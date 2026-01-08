import pandas as pd
from validations import validate_is_a_number as isANumber
from validations import validate_x_numeric_items as validate_data

students_califications = []
students = {}

for i in range(10):
    name = input(f"Introduce el nombre del estudiante {i + 1}: ")

    num_of_notes = input(f"¿Cuántas calificaciones tiene {name}? ")
    
    while not isANumber(num_of_notes) or int(num_of_notes) <= 0:
        print("Por favor, introduce un número válido de calificaciones.")
        num_of_notes = input(f"¿Cuántas calificaciones tiene {name}? ")

    students_califications = input(f"Introduce las {num_of_notes} calificaciones en el siguiente formato: cal1,cal2,cal3... ")

    if not validate_data(students_califications, int(num_of_notes)):
        print("Datos inválidos. Por favor, inténtalo de nuevo.")
        stopped = False
        while not stopped:
            students_califications = input(f"Introduce las {num_of_notes} calificaciones en el siguiente formato: cal1,cal2,cal3... ")
            if validate_data(students_califications, int(num_of_notes)):
                stopped = True

    students[name] = students_califications.strip().split(",")
    students_califications = []

series = pd.Series(students)
print(series)

