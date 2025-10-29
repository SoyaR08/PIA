def calculate_factorial(n):

    abs_number = abs(n)
    factorial = 1

    if abs_number > 1:
        for i in range(abs_number, 0, -1):
            factorial *= i

    
    return factorial

def isPrimeNumber(n):
    if n % 2 == 0:
        return False
    
    for i in range(1, n, 1):
        if n % i == 0 and i != 1:
            return False
        
    return True

def plus_digits(number):

    result = 0

    if not number.isnumeric() and '-' in number:
        return "Input no válido"
    
    digits_array = list(number)

    for n in digits_array:
        result += int(n)

    return result

def parseCelsiusToFahrenheit(celsius):
    return (celsius * 9) / 5 + 32

def sumArrayNumbers(array):
    sumathory = 0

    for number in array:
        sumathory += number

    return sumathory

def fibonacci(number):

    start = 0
    next = 1

    sequence = []

    for i in range(0, number):
        sequence.append(start)

        fibo = start + next
        start = next
        next = fibo

    return sequence

def whoIsBigger(num1, num2):
    if num1 > num2:
        return -1
    elif num1 < num2:
        return 1
    else:
        return 0

def mcdEuclideAlorithm(a, b):
    # Function: A = B * Q + R
    mcd = 0
    choice = whoIsBigger(a, b)

    match (choice):
        case -1:
            largerNumber = a
            lowerNumber = b
        case 1:
            largerNumber = b
            lowerNumber = a
        case 0: # If a and b are the same, then that value is the mcd
            return a

    coefficient = 0    
    rest = 1

    mcdFinded = False

    while not mcdFinded:
        rest = largerNumber % lowerNumber
        coefficient = largerNumber // lowerNumber
            
        print(f"Dividendo: {largerNumber}, Divisor: {lowerNumber}, Coeficiente: {coefficient}, Resto: {rest}")
        print()

        largerNumber = lowerNumber
        lowerNumber = rest

        if rest < 1:
            mcd = coefficient
            mcdFinded = True



    return mcd

def isSorted(array):
    return array == sorted(array)

def sortArray(numberArray):
    
    isTheArraySorted = isSorted(numberArray)

    sorted_array = numberArray.copy()

    while not isTheArraySorted:

        for i in range(len(sorted_array)):
            if i != (len(sorted_array) - 1) and sorted_array[i + 1] < sorted_array[i]:
                before = sorted_array[i + 1]
                after = sorted_array[i]
                sorted_array[i] = before
                sorted_array[i + 1] = after
                break

        print(f"Elementos cambiados: {before} y {after}, aspecto actual de la lista: {sorted_array}")

        isTheArraySorted = isSorted(sorted_array)

    return sorted_array

def calculateCircleArea(radius):
    return 3.14 * radius**2

def parseToSeconds(hours, minutes, seconds):
    seconds += (hours * 3600) + (minutes * 60)
    return seconds

def parseSecondsToDate(secondsToParse):

    hours = 0
    minutes = 0

    hours, secondsToParse = secondsToParse // 3600, secondsToParse % 3600
    minutes, secondsToParse = secondsToParse // 60, secondsToParse % 60

    new_date = f"{hours}:{minutes}:{secondsToParse}"

    return new_date

def calculateStepsToKm(steps):
    return (steps * 0.78) * 1 / 1000

#----------------- Lambda Section -----------------

# Elevar un número al cuadado

squared = lambda a: a**2

# Sumar 2 números

addition = lambda a,b: a+b

# Mayor que

greatherThan = lambda a,b: a if a > b else b

# Invertir una cadena

revertString = lambda a: a[::-1]

# Averiguar si es palíndromo

isPalindrome = lambda a: a.lower().replace(" ", "") == a[::-1].lower().replace(" ", "")