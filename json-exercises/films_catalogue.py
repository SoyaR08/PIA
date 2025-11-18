import json
import random as rd
from datetime import date as dt

def filterByGender(data, genre):
    filtered_data = list(filter(lambda film: genre.replace(" ", "").lower() in film["genero"].replace(" ", "").lower(), data))
    return filtered_data

def addNewFilms(data):

    film_titles = ["Inception", "The Godfather", "La máscara del zorro", "The Dark Knight"]
    film_directors = ["Christopher Nolan", "Francis Ford Coppola", "Guillermo del Toro", "Steven Spielberg"]
    film_genres = ["Action", "Drama", "Comedy", "Thriller"]
    film_years = range(1990, 2024)

    for _ in range(4):
        title = rd.choice(film_titles)
        film_titles.remove(title)
        director = rd.choice(film_directors)
        genre = rd.choice(film_genres)
        year = rd.choice(film_years)
        film = {
            "titulo": title,
            "director": director,
            "año_lanzamiento": year,
            "genero": genre
        }

        data.append(film)

def listUniqueDirectors(data):
    unique_directors = []
    for i in range(len(data)):
        director = data[i]["director"]
        coincidence = False

        for j in range(len(data)):
            if i != j and director == data[j]["director"]:
                coincidence = True
                break

        if not coincidence:
            unique_directors.append(director)

    return unique_directors


file = open("jsons/data.json", "rt")

json_string = file.read()

data = json.loads(json_string)

print(filterByGender(data=data["peliculas"], genre="Drama"))
addNewFilms(data["peliculas"])
print(listUniqueDirectors(data["peliculas"]))