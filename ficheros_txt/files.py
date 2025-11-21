import unicodedata
import string

def count_words(text):
    words = text.split()
    return len(words)

def normalize(text):
    # Pasamos a minúsculas
    text = text.lower()
    # Separamos los acentos de las letras
    text = unicodedata.normalize("NFD", text)
    # Eliminamos signos de puntuación
    text = "".join(c for c in text if c not in string.punctuation)
    # Eliminamos acentos
    text = "".join(c for c in text if unicodedata.category(c) != "Mn")
    return text

def count_many_times(text, word):
    text_norm = normalize(text)
    word_norm = normalize(word)
    words = text_norm.split()
    return sum(1 for w in words if w == word_norm)

def calc_media_length(text):
    words = text.split()

    total_length = sum(len(word) for word in words)
    return total_length / len(words) if words else 0

def create_index():
    words_count = {}
    first_line_register = {}

    # Abrimos el fichero
    with open("ficheros_txt/el_quijote.txt", "rt", encoding="utf-8") as file:
        # Recorremos línea a línea
        for line_num, line in enumerate(file, start=1):
            # Normalizamos la línea y separamos en palabras
            words = normalize(line).split()
            for w in words:
                # Contamos palabras
                words_count[w] = words_count.get(w, 0) + 1
                # Guardamos la primera línea en la que aparece
                if w not in first_line_register:
                    first_line_register[w] = line_num

    # Ordenamos por frecuencia y nos quedamos con las 10 más comunes
    top_10 = sorted(words_count.items(), key=lambda item: item[1], reverse=True)[:10]

    # Creamos un diccionario con palabra: (frecuencia, primera línea)
    result = {word: f"{count} veces, línea {first_line_register[word]}" for word, count in top_10}
    return result

def getTenMoreUsed(text):

    words_time = {}
    words = normalize(text).split()

    for w in words:

        if w in words_time:
            words_time[w] += 1
        else:
            words_time[w] = 1

    ordered_words_time = sorted(words_time.items(), key=lambda item: item[1], reverse=True)

    return dict(ordered_words_time[:10])

def getLongestPhrases(text):
    phrases = text.split(".")
    phrases = [phrase.strip() for phrase in phrases if phrase.strip()]

    phrases.sort(key=lambda p: len(p), reverse=True)

    return phrases[:5]


with open("ficheros_txt/el_quijote.txt", "rt", encoding="utf-8") as file:
    data = file.read()



print("Número de palabras en el texto:", count_words(data))
print("Número de veces que aparece 'capítulo':", count_many_times(data, "capítulo"))
print(f"Número de veces que aparece 'Dulcinea': {count_many_times(data, 'Dulcinea')}, Quijote: {count_many_times(data, 'Quijote')} y Sancho {count_many_times(data, 'Sancho')}")
print(getTenMoreUsed(data))
print(create_index())
print("La longitud media de las palabras es:", calc_media_length(data))
# print("Las 5 frases más largas son:", getLongestPhrases(data))