def revert_strings(string):
    reversed = ""

    for i in range(len(string), 0, -1):
        reversed += string[i-1]

    return reversed


print(revert_strings("Hola"))
