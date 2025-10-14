"""
ANAGRAMA
Función que reciba dos palabras (string) y devuelva verdadero/falso según sean o no anagramas.
"""
def is_anagram(word, word2):
    if word.lower() == word2.lower():
        return False
    
    return sorted(word.lower()) == sorted(word2.lower())


print(is_anagram("Monja", "Jamon"))