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

def validateData(data):

    errors = []

    phone_pattern = r"^[679]\d{8}$"
    pc_pattern = r"\d{5}"
    mail_pattern = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
    year_pattern = r"^\d{4}"

    for std, car in zip(data["alumnos"], data["vehiculos"]):

        if not re.fullmatch(phone_pattern, std["telefono"]):
            errors.append(f"{std['telefono']} debe empezar por 6, 7 o 9 y tener 9 caractéres numéricos")

        if not re.fullmatch(pc_pattern, std["codigo_postal"]):
            errors.append(f"{std['codigo_postal']} debe tener 5 caractéres numéricos exactos")

        if not re.fullmatch(mail_pattern, std["email"]):
            errors.append(f"{std['email']} debe ser válido")

        if not re.fullmatch(year_pattern, car["anyo"]):
            errors.append(f"{car['anyo']} no debe estar comprendido entre 1900 y 2025")

    return errors if len(errors) > 0 else "Los datos son válidos"


data = load_data()

print(validateData(data))