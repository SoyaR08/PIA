import os



def build_table():
    try:
        n = int(input("Introduce un número entre 1 y 10: "))
        if n < 1 or n > 10:
            print("❌ El número debe estar entre 1 y 10.")
            return
        
        filename = f"tabla-{n}.txt"
        
        with open(filename, "w") as f:
            for i in range(1, 11):
                f.write(f"{n} x {i} = {n*i}\n")
        
        print(f"Tabla de multiplicar de {n} creada en {filename}")
    
    except ValueError:
        print("Debes introducir un número entero.")


def read_table():
    try:
        n = int(input("Introduce un número entre 1 y 10: "))
        if n < 1 or n > 10:
            print("El número debe estar entre 1 y 10.")
            return
        
        filename = f"tabla-{n}.txt"
        
        if not os.path.exists(filename):
            print(f"El fichero {filename} no existe.")
            return
        
        print(f"\n Contenido de {filename}:")
        with open(filename, "r") as f:
            print(f.read())
    
    except ValueError:
        print("Debes introducir un número entero.")


def read_table_line():
    try:
        n = int(input("Introduce un número entre 1 y 10: "))
        m = int(input("Introduce la línea que quieres leer (1 a 10): "))
        
        if n < 1 or n > 10 or m < 1 or m > 10:
            print("Los números deben estar entre 1 y 10.")
            return
        
        filename = f"tabla-{n}.txt"
        
        if not os.path.exists(filename):
            print(f"El fichero {filename} no existe.")
            return
        
        with open(filename, "r") as f:
            lineas = f.readlines()
        
        print(f"Línea {m} de la tabla-{n}.txt:")
        print(lineas[m-1].strip())
    
    except ValueError:
        print("Debes introducir números enteros.")


def menu():
    print("==================================")
    print("1. Crear la tabla de multiplicar de un número")
    print("2. Leer tabla de multiplicar de un número")
    print("3. Leer una línea de la tabla de multiplicar de un número")
    print("4. Salir")
    print("==================================")


finished = False

while not finished:
    menu()
    opcion = input("Elige una opción: ")

    match opcion:
        case "1":
            build_table()
        case "2":
            read_table()
        case "3":
            read_table_line()
        case "4":
            print("Saliendo del programa...")
            finished = True
        case _:
            print("Opción no válida. Intenta de nuevo.")
