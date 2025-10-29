# Ejercicio 15
print("============= Ejercicio 15 =============")

year = 2024

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f"El año {year} es bisiesto.")

print()