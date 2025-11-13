import json
from classes import Contact

def findAContact(contactName, contactList):

    finded_contact = {}

    for contact in contactList:
        
        if contactName.lower() in contact["nombre"].lower():
            finded_contact = contact
            return finded_contact
        
    else:
        return "Contacto no encontrado"

def updatePhoneNumber(contact, newNumber):
    contact["telefono"] = newNumber
    return contact

def deleteContact(contact, contactList):
    contactList.remove(contact)
    return "Contacto eliminado"

file = open("json-exercises/jsons/phone_book.json", "rt")
json_string = file.read()

data = json.loads(json_string)

print("========= Inserción de 10 contactos =========")
for i in range(1):
    print(f"Contacto {i+1}:")
    name = input("Introduzca un nombre: ")
    surname = input("Introduzca un apellido: ")
    phone = input("Introduzca un teléfono: ")
    mail = input("Introduce un e-mail: ")
    c = Contact(name, surname, phone, mail)
    contact_dict = c.parseToDict()
    data["contactos"].append(contact_dict)
    print()

# Finding contacts
contact_to_search = input("Introduce el nombre del contacto a buscar: ")

returned_contact = findAContact(contact_to_search, data["contactos"])

print(f"Contacto: {returned_contact}")

edited_contact = findAContact(contact_to_search, data["contactos"])

edited_contact = updatePhoneNumber(edited_contact, "123456789")

print(f"Contacto editado: {edited_contact}")

name_contact_to_delete = input("Introduce el nombre del contacto a eliminar: ")

contact_to_delete = findAContact(name_contact_to_delete, data["contactos"])

print(deleteContact(contact_to_delete, data["contactos"]))

print(data)
    