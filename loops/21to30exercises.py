# 21. Suma condicional de números con while
# Escribe un programa que sume números ingresados por el usuario hasta que ingrese un 
# número negativo utilizando un bucle while.
# 22. Encontrar múltiplos con for
# Escribe un programa que encuentre todos los múltiplos de un número en un rango dado 
# utilizando un bucle for.
# 23. Números perfectos con for
# Escribe un programa que verifique si un número es perfecto (igual a la suma de sus divisores) 
# utilizando un bucle for.
# 24. Número mayor y menor con for
# Escribe un programa que encuentre el número mayor y el menor de una lista utilizando un 
# bucle for.
# 25. Cifrar una cadena con for
# Escribe un programa que cifre una cadena desplazando cada letra una posición en el alfabeto 
# utilizando un bucle for.
# 26. Imprimir pirámide de números con for
# Escribe un programa que imprima una pirámide de números utilizando bucles for.
# 27. Simular lanzamiento de monedas con while
# Escribe un programa que simule el lanzamiento de una moneda hasta que salga cara tres 
# veces consecutivas utilizando un bucle while.
# 28. Dibujar un cuadrado con for
# Escribe un programa que dibuje un cuadrado de asteriscos de tamaño N utilizando bucles 
# for.
# 29. Comparar cadenas con while
# Escribe un programa que compare dos cadenas carácter por carácter utilizando un bucle 
# while.
# 30. Contador de intentos con else en while
# Escribe un programa que intente adivinar un número ingresado por el usuario y use un bucle 
# while. Si no logra adivinar después de 5 intentos, muestra un mensaje en el bloque else.

# Ejercicio 21
print("============= Ejercicio 21 =============")
result = 0
def ask_numbers(result):
    number_given = 1
    local_result = result
    
    while number_given > 0:
        try:
            number_given = int(input("Introduce un número: "))
            if number_given > 0:
                local_result += number_given
                print(f"Resultado actual {local_result}")
            else:
                break
        except Exception:
            print("Eso no es un número")
            ask_numbers(local_result)
            number_given = -1
            

    return local_result

result = ask_numbers(result)

print(f"El resultado es: {result}")
print()

# Ejercicio 22
print("============= Ejercicio 22 =============")
range_start = 10
range_end = 25
number_to_check = 4
multiples = []

if range_end >= range_start:
    start = range_start
    end = range_end
elif range_start > range_end:
    start = range_end
    end = range_start


for i in range(start, end + 1):
    if i % number_to_check == 0:
        multiples.append(i)

print(f"Los múltiplos de {number_to_check} comprendidos entre {start} y {end} son: {multiples}")
print()

# Ejercicio 23
print("============= Ejercicio 23 =============")

def find_divisors(number):
    divisors = []
    for i in range(1, number):
        if number % i == 0:
            divisors.append(i)

    return divisors

def isPerfect(number, divisors):
    total = sum(divisors)

    return number == total

number_possible_perfect = 28 
divisors = find_divisors(number_possible_perfect)
print(f"¿Es {number_possible_perfect} un número perfecto?: {isPerfect(number_possible_perfect, divisors)}")
print()

# Ejercicio 24
print("============= Ejercicio 24 =============")

number_list = [9, 10, 8, 3, 2, -7, 5, 6, 4, 1]
max_number = number_list[0]
min_number = number_list[0]

for number in number_list:
    if number > max_number:
        max_number = number
    elif number < min_number:
        min_number = number

print(f"El número mayor de la lista es: {max_number} y el menor es: {min_number}")

# Ejercicio 25
print("============= Ejercicio 25 =============")
alphabet = "abcdefghijklmnopqrstuvwxyz"
input_text = input("Introduce un texto: ")
cifred_word = ""


for char in input_text:
    index = alphabet.find(char.lower())

    if index + 1 > len(alphabet) - 1:
        cifred_word += alphabet[0]

    else:
        cifred_word += alphabet[index + 1]

print(f"Texto cifrado: {cifred_word}")
print()

# Ejercicio 26
print("============= Ejercicio 26 =============")

y_axis = 4
number = 1
for y in range(1, y_axis + 1):
    string = ""
    for x in range(y):
        string += str(number) + " "
        number+=1
    print(string)
print()

# Ejercicio 27
print("============= Ejercicio 27 =============")
import random

head_streak = 0
head_counter = 0
cross_counter = 0
history = []

while head_streak < 3:
    choice = random.randint(0, 1)

    match choice:
        case 0:
            head_counter += 1
            head_streak += 1
            history.append("Cara")
        case 1:
            cross_counter += 1
            head_streak = 0
            history.append("Cruz")

print(f"Han salido {head_counter} caras y {cross_counter} cruces hasta obtener 3 caras seguidas.")
print(f"Historial de lanzamientos: {history}")
print()

# Ejercicio 28
print("============= Ejercicio 28 =============")

square_height = 4
square_length = 4

for h in range(1, square_height + 1):
    string = ""
    for l in range(1, square_length + 1):
        string += "*" # Due to the output it looks like more similar to a rectangle but its sides are equal among themselves

    print(string)

print()

# Ejercicio 29
print("============= Ejercicio 29 =============")
string1 = "Hola"
string2 = "Hol4"

equals = True
i = 0
if len(string1) == len(string2):
    while (i < len(string1) and equals):
        if not string1[i].lower() == string2[i].lower():
            equals = False
        i += 1

else:
    equals = False

print(f"¿Las cadenas son iguales?: {equals}")
print()

# Ejercicio 30
print("============= Ejercicio 30 =============")
import random
user_number = input("Introduce un número entre 1 y 10: ")

while not user_number.isdigit():
    user_number = input("Eso no es un número, introduce otro entre 1 y 10: ")


user_number = int(user_number)

tries = 1
number_selected = random.randint(1, 10)
got_it = False
range_to_choose = [1,2,3,4,5,6,7,8,9,10]

while not got_it:
    if user_number == number_selected:
        got_it = True

    else:
        range_to_choose.remove(number_selected)
        number_selected = random.choice(range_to_choose)
        tries += 1
    print("Pensando...")

print(f"La máquina ha necesitado {tries} intentos para adivinar el número {user_number}")
print()