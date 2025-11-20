import unicodedata

def count_many_times(text, word):
    count = 0
    words_list = text.split()

    for w in words_list:
        p = unicodedata.normalize('NFD', w)
        if p == word.lower():
            count += 1

    return count


with open("ficheros_txt/el_quijote.txt", "rt", encoding="utf-8") as file:
    data = file.read()


words = data.split()

print(f"Número de palabras en el texto: {len(words)}")
print(f"Número de veces que aparece la palabra 'capítulo': {count_many_times(data, 'capítulo')}")