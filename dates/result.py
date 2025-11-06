import datetime

# Ejercicio de Fechas 1

print("========= Ejercicio de Fechas 1 =========")

current_date = datetime.date.today().strftime("%d/%m/%Y")

print(f"Fecha actual: {current_date}")
print()

# Ejercicio de Fechas 2

print("========= Ejercicio de Fechas 2 =========")

def getActualDate():

    date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return date

print(getActualDate())
print()