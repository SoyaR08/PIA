# Ejercicio 47
print("====================Ejercicio 47====================")
numbers_duplicated = [1, 2, 3, 4, 4, 2, 9, 4, 6, 7, 8, 1, 3]
print("Lista con duplicados:", numbers_duplicated)
dictionary_duplications = {}
numbers_non_duplicated = []

for i in range(0, len(numbers_duplicated)):
    for j in range(0, len(numbers_duplicated)):
        if numbers_duplicated[i] == numbers_duplicated[j] and i != j:
            if numbers_duplicated[i] not in dictionary_duplications:
                dictionary_duplications[numbers_duplicated[i]] = [j]
            else:
                if j not in dictionary_duplications[numbers_duplicated[i]]:
                    dictionary_duplications[numbers_duplicated[i]].append(j)

print("Diccionario de duplicados:", dictionary_duplications.values())

for position in dictionary_duplications.values():
    for i in range(1, len(position)):
        numbers_duplicated[position[i]] = ""

numbers_non_duplicated = list(filter(lambda x: x != "", numbers_duplicated))

print("Lista sin duplicados:", numbers_non_duplicated)
print()