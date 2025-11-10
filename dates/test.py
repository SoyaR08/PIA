from datetime import datetime, date

# Ejercicio de Fechas 3

print("========= Ejercicio de Fechas 3 =========")

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

def diffamongdates(date1, date2):

    
 
    return ""

print(isInFormat("2025-04-12"))

print()