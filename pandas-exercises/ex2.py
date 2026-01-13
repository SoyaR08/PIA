import pandas as pd
from validations import validate_is_a_number as isANumber
from validations import validate_x_numeric_items as validate_data

def transform_to_numeric_list(data):
    return [int(item.strip()) for item in data.strip().split(",")]

students_names = ["Alex", "Maria", "Juan", "Luisa", "Carlos", "Ana", "Pedro", "Sofia", "Miguel", "Elena"]
students_califications = []
students = {}

for n in students_names:

    num_of_notes = input(f"¿Cuántas calificaciones tiene {n}? ")
    
    while not isANumber(num_of_notes) or int(num_of_notes) <= 0:
        print("Por favor, introduce un número válido de calificaciones.")
        num_of_notes = input(f"¿Cuántas calificaciones tiene {n}? ")

    students_califications = input(f"Introduce las {num_of_notes} calificaciones en el siguiente formato: cal1,cal2,cal3... ")

    if not validate_data(students_califications, int(num_of_notes)):
        print("Datos inválidos. Por favor, inténtalo de nuevo.")
        stopped = False
        while not stopped:
            students_califications = input(f"Introduce las {num_of_notes} calificaciones en el siguiente formato: cal1,cal2,cal3... ")
            if validate_data(students_califications, int(num_of_notes)):
                stopped = True

    students[n] = transform_to_numeric_list(students_califications)
    students_califications = []

print(students)
series = pd.Series(students)
print(series)
mean = series.explode().astype(float).mean()
median = series.explode().astype(float).median()
std = series.explode().astype(float).std()
print(f"La media de las calificaciones es: {mean}, la mediana es: {median} y la desviación estándar es: {std}")


