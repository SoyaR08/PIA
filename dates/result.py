from datetime import datetime, date, timedelta

# Ejercicio de Fechas 1

print("========= Ejercicio de Fechas 1 =========")

def getActualDate():

    date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return date


print(getActualDate())
print()

# Ejercicio de Fechas 2

print("========= Ejercicio de Fechas 2 =========")

def stringToDatetime(string):

    newDateTime = datetime.strptime(string, "%d/%m/%Y")

    return newDateTime

print(stringToDatetime("13/12/2005"))
print()

# Ejercicio de Fechas 3

print("========= Ejercicio de Fechas 3 =========")

# I thought that the user had to input the date so i created thisW
def isInFormat(string, format=None):
    formats = ["%d/%m/%Y", "%Y-%m-%d", "%d-%m-%Y", "%Y/%m/%d"]

    # Si no se pasa un formato, probamos todos
    if format is None:
        for fmt in formats:
            try:
                return datetime.strptime(string, fmt)
            except ValueError:
                continue
        return None  # no coincide con ninguno
    
    return datetime.strptime(string, format)

def diffamongdates(date1, date2):
 
    return abs(date1 - date2)

date1 = isInFormat("12/11/2025", "%d/%m/%Y")
date2 = isInFormat("12/11/2026", "%d/%m/%Y")

print(f"La diferencia en días es: {diffamongdates(date1, date2).days} días")
print()

# Ejercicio de Fechas 4

print("========= Ejercicio de Fechas 4 =========")

def plusDays(dateGiven, days):

    return dateGiven + timedelta(days=days)

userDate = datetime.strptime("11/11/2025", "%d/%m/%Y")
daysToAdd = 5

print(f"La nueva fecha es: {plusDays(userDate, daysToAdd).strftime('%d/%m/%Y')}")
print()

# Ejercicio de Fechas 5

print("========= Ejercicio de Fechas 5 =========")

def changeFormat(dateGiven):
    return dateGiven.strftime("%d/%m/%Y")


userDate = datetime.strptime("2025-12-31", "%Y-%m-%d")
print(f"La fecha en formato dd/mm/yyyy es: {changeFormat(userDate)}")
print()