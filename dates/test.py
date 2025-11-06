import datetime

# Ejercicio de Fechas 2

print("========= Ejercicio de Fechas 2 =========")

def getActualDate():

    date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return date

print(getActualDate())
print()