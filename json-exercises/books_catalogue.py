import json
import random as rd
from datetime import date as dt

def insertBooks(data):

    books_names = ["El príncipe de la niebla", "El capitán Alatriste", "El cuarto de atrás", "Toda verdad debe ser contada", "Virtual Hero", "La íliada y la odisea",
                      "CSS I", "Como mandar a la mierda educadamente", "La vuelta al fútbol en 80 historias", "Cien años de soledad"]
    
    books_authors = ["Carlos Ruiz Zafon", "Perez Reverte", "Carmen Martin Gaite", "Alvaro Gomez Garcia", "ElRubiusOMG", "Hola", "Algun experto en CSS", "No me acuerdo la vd", "Iker Ruiz", "IlloJuan"]
    books_genre = ["Novela", "Historia", "Ciencia Ficción", "Fantasía", "Terror", "Romance", "Poesía", "Ensayo", "Biografía", "Aventura"]
    books_years = range(2020, 2025)
   
    for i in range(10):
        name = books_names[i]
        author = books_authors[i]
        book = {
            "titulo": name,
            "autor": author,
            "genero": rd.choice(books_genre),
            "anyo": rd.choice(books_years)
        }

        data.append(book)

"""I will consider a book as recent if it has been published in the last 3 years."""
def getRecientBooks(data):
    year = dt.today().year - 3
    return list(filter(lambda book: book["anyo"] >= year, data))


def addNewBook(data):
    title = input("Introduce el título del nuevo libro: ")
    author = input("Introduce el autor del nuevo libro: ")
    gender = input("Introduce el género del nuevo libro: ")

    book = {
        "titulo": title,
        "autor": author,
        "genero": gender,
        "anyo": dt.today().year
    }

    data.append(book)

    return f"Se ha añadido al estudiante {book}"

def filterByField(data, field, value):
    filtered_data = []
    match field:
        case 0:
            filtered_data = list(filter(lambda book: value.replace(" ", "").lower() in book["autor"].replace(" ", "").lower(), data))
        case 1:
            filtered_data = list(filter(lambda book: value.replace(" ", "").lower() in book["genero"].replace(" ", "").lower(), data))

    return filtered_data

file = open("jsons/books_catalogue.json", "rt")

json_string = file.read()

data = json.loads(json_string)
insertBooks(data["libros"])
print(getRecientBooks(data["libros"]))
print()
print(filterByField(data["libros"], 0, "cervantes"))
print()
print(addNewBook(data["libros"]))