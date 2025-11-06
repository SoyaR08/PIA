from datetime import datetime, date

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