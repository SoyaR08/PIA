import os

FICHERO = "ficheros_txt_and_csv/listin.txt"


def create_file():
    """Crea el fichero si no existe."""
    if not os.path.exists(FICHERO):
        with open(FICHERO, "w") as f:
            pass
        print("Fichero listin.txt creado.")
    else:
        print("El fichero ya existe.")


def search_phone():
    """Consulta el teléfono de un cliente."""
    name = input("Introduce el nombre del cliente: ").strip()

    if not os.path.exists(FICHERO):
        create_file()

    with open(FICHERO, "r") as f:
        for linea in f:
            client, phone = linea.strip().split(",")
            if client.lower() == name.lower():
                print(f"Teléfono de {client}: {phone}")
                return

    print("Cliente no encontrado.")


def add_client():
    """Añade un nuevo cliente al listín."""
    name = input("Introduce el nombre del nuevo cliente: ").strip()
    phone = input("Introduce su teléfono: ").strip()

    if not os.path.exists(FICHERO):
        create_file()

    with open(FICHERO, "a") as f:
        f.write(f"{name},{phone}\n")

    print(f"Cliente '{name}' añadido con éxito.")


def delete_client():
    """Elimina un cliente del listín."""
    name = input("Introduce el nombre del cliente a eliminar: ").strip()

    if not os.path.exists(FICHERO):
        create_file()

    finded = False
    new_lines = []

    with open(FICHERO, "r") as f:
        for linea in f:
            client, phone = linea.strip().split(",")
            if client.lower() != name.lower():
                new_lines.append(linea)
            else:
                finded = True

    if not finded:
        print("Cliente no encontrado.")
        return

    with open(FICHERO, "w") as f:
        f.writelines(new_lines)

    print(f"Cliente '{name}' eliminado correctamente.")


def menu():
    print("\n=========== LISTÍN TELEFÓNICO ===========")
    print("1. Crear fichero del listín")
    print("2. Consultar teléfono de un cliente")
    print("3. Añadir cliente")
    print("4. Eliminar cliente")
    print("5. Salir")
    print("===========================================")

finished = False

while not finished:
    menu()
    option = input("Elige una opción: ")

    match option:
        case "1":
            create_file()
        case "2":
            search_phone()
        case "3":
            add_client()
        case "4":
            delete_client()
        case "5":
            print("Saliendo del programa...")
            finished = True
        case _:
            print("Opción no válida.")
