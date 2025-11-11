from datetime import datetime, date, timedelta

# Ejercicio de Fechas 5

print("========= Ejercicio de Fechas 5 =========")

def changeFormat(dateGiven):
    return dateGiven.strftime("%d/%m/%Y")


userDate = datetime.strptime("2025-12-31", "%Y-%m-%d")
print(f"La fecha en formato dd/mm/yyyy es: {changeFormat(userDate)}")
print()