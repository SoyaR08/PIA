import csv

def read_file(file):
    students = []

    with open(file, encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=';')
        
        for line in reader:

            # Convertir valores vacíos a None o numérico cuando toca
            for key, value in line.items():
                line[key] = value.strip() if value and value.strip() != "" else None

                # Convertir números
                if key not in ("Apellidos", "Nombre", "Asistencia") and line[key] is not None:

                    if "," in line[key]:
                        line[key] = line[key].replace(",", ".")

                    line[key] = float(line[key])

                if key == "Asistencia" and line[key] is not None:
                    line[key] = float(line[key].replace("%", ""))

                

            students.append(line)

    # Ordenar por apellidos
    students.sort(key=lambda x: x["Apellidos"])

    return students



def calc_final_grades(students_list):
    for student in students_list:

        # Obtener notas originales o 0 si están vacías
        p1 = student["Parcial1"] or 0
        p2 = student["Parcial2"] or 0
        pr = student["Practicas"] or 0

        
        if p1 < 4 and student["Ordinario1"] is not None:
            p1 = student["Ordinario1"]

        if p2 < 4 and student["Ordinario2"] is not None:
            p2 = student["Ordinario2"]

        if pr < 4 and student["OrdinarioPracticas"] is not None:
            pr = student["OrdinarioPracticas"]

        
        final_grade = p1 * 0.30 + p2 * 0.30 + pr * 0.40
        student["NotaFinal"] = round(final_grade, 2)

    return students_list



def split_passed_students(students_list):
    passed = []
    failed = []

    for student in students_list:
        asistance = student["Asistencia"] or 0

        p1 = student["Parcial1"] or 0
        p2 = student["Parcial2"] or 0
        pr = student["Practicas"] or 0

        if p1 < 4 and student["Ordinario1"] is not None:
            p1 = student["Ordinario1"]

        if p2 < 4 and student["Ordinario2"] is not None:
            p2 = student["Ordinario2"]

        if pr < 4 and student["OrdinarioPracticas"] is not None:
            pr = student["OrdinarioPracticas"]

        final = student["NotaFinal"]

        # Condiciones para aprobar
        approve_conditions = (
            asistance >= 75 and
            p1 >= 4 and p2 >= 4 and pr >= 4 and
            final >= 5
        )

        if approve_conditions:
            passed.append(student)
        else:
            failed.append(student)

    return passed, failed


file = "ficheros_txt_and_csv/calificaciones.csv"

students = read_file(file)
students = calc_final_grades(students)
passed, failed = split_passed_students(students)

print(" Alumnos aprobados:")
for a in passed:
    print(a["Apellidos"], a["Nombre"], "→", a["NotaFinal"])

print("\n Alumnos suspensos:")
for a in failed:
    print(a["Apellidos"], a["Nombre"], "→", a["NotaFinal"])


