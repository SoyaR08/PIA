# 11. Contador decreciente con while
# a. Escribe un programa que imprima los números del 10 al 1 utilizando un bucle while.
# 12. Mínimo común múltiplo (MCM) con while
# a. Escribe un programa que encuentre el MCM de dos números utilizando un bucle while.
# 13. Palabras que empiezan con una letra con for
# a. Escribe un programa que recorra una lista de palabras y cuente cuántas empiezan con 
# una letra específica utilizando un bucle for.
# 14. Buscar máximo en una lista con for
# a. Escribe un programa que busque el número más grande en una lista utilizando un bucle for.
# 15. Suma de números en un rango con for
# a. Escribe un programa que sume todos los números en un rango dado utilizando un bucle 
# for.
# 16. Tablas de multiplicar con for
# a. Escribe un programa que imprima la tabla de multiplicar del 1 al 10 utilizando un bucle 
# for.
# 17. Potencia de un número con for
# a. Escribe un programa que calcule la potencia de un número dado utilizando un bucle 
# for
# 18. Calcular promedio con for
# Escribe un programa que calcule el promedio de una lista de números utilizando un bucle 
# for.
# 19. Contar letras y dígitos con for
# Escribe un programa que cuente cuántas letras y cuántos dígitos hay en una cadena 
# utilizando un bucle for.
# 20. Comparación de listas con for
# Escribe un programa que compare dos listas y cuente cuántos elementos coinciden utilizando 
# un bucle for.

# Ejercicio 11
print("============= Ejercicio 11 =============")
count = 10
while count >= 1:
    print(count)
    count -= 1
print()

# Ejercicio 12
print("============= Ejercicio 12 =============")
num1 = 5
num2 = 27

"""This function factorizes a number, returning a list with its divisors"""
def findDivisors(n):
    divisors = []
    start = 2
    while n > 1:
        if n % start == 0:
            divisors.append(start)
            n = n / start
        else:
            start += 1

    return divisors

"""This function maybe can be optimized, but i don't know how. Its functionality is to count how many times a number appears in a list, returning a dictionary with the number as key and the count as value"""
def countTimesNumberAppears(list):
    countDict = {}

    for n in list:
        if n in countDict:
            countDict[n] += 1
        else:
            countDict[n] = 1

    return countDict

num1_divisors = findDivisors(num1)
num2_divisors = findDivisors(num2)

"""This function compares two lists of divisors and returns which one is larger, or if they are equal in length"""
def findLargerDivisorsList(list1, list2):
    if len(list1) > len(list2):
        return -1
    elif len(list1) < len(list2):
        return 1
    else:
        return 0
    

"""This function calculates the MCM of two numbers given their divisors lists"""
def calculateMCM(num1_divisors, num2_divisors):
    mcm_list = []

    divisors1List, divisors2List = countTimesNumberAppears(num1_divisors), countTimesNumberAppears(num2_divisors)

    comparison = findLargerDivisorsList(divisors1List, divisors2List)

    match comparison:
        case -1:
            largerList = divisors1List
            smallerList = divisors2List
        case 1:
            largerList = divisors2List
            smallerList = divisors1List
        case 0:
            largerList = divisors1List
            smallerList = divisors2List
            mcm_list = [largerList, smallerList]
            return multiplyDictionaryListContent(mcm_list)


    for key in largerList:
        print("Clave actual: ", key)
        if smallerList.get(key) != None:
            if largerList[key] >= smallerList[key]:
                mcm_list.append({key: largerList[key]})
                smallerList.pop(key)
            else:
                mcm_list.append({key: smallerList[key]})
                smallerList.pop(key)
        else:
            mcm_list.append({key: largerList[key]})
    
    print("Smaller List remaining items: ", smallerList)

    print("Lista de factores para el MCM: ", mcm_list)

    return multiplyDictionaryListContent(mcm_list)

"""This function multiplies the content of a list of dictionaries, where the key is the base and the value is the exponent"""
def multiplyDictionaryListContent(mcm_list):
    mcm = 1
    for dict in mcm_list:
        for key in dict:
            mcm *= key ** dict[key]
    
    return mcm

print("Divisores de ", num1, ": ", findDivisors(num1))
print("Divisores de ", num2, ": ", findDivisors(num2))
print(countTimesNumberAppears(num1_divisors))
print(countTimesNumberAppears(num2_divisors))
print("El mínimo común múltiplo de ",num1," y ",num2," es:",calculateMCM(num1_divisors, num2_divisors))
print()