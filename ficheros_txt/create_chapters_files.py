import re
import os
import unicodedata
import string

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

# Archivo de entrada
archivo_entrada = "el_quijote.txt"

# Carpeta donde guardar los capítulos
carpeta_salida = "capitulos"
os.makedirs(carpeta_salida, exist_ok=True)

# Patrón: captura el encabezado del capítulo y el número (grupo 2)
# Permite "capítulo" con o sin tilde, mayúsculas/minúsculas, espacios antes de ":".
pattern = r"capitulo+ \d"

with open(archivo_entrada, "rt", encoding="utf-8") as f:
    contenido = f.read()
    splited_content = contenido.split('\n')[4:] # Quito el encabezado
    
    limits = []
    sections = {}

    for index, line  in enumerate(splited_content, start=1):
        normalized_line = normalize(line)
        if re.match(pattern, normalized_line):
            limits.append(index)

    
    for i in range(len(limits)):
        start = limits[i] - 1
        if i + 1 < len(limits):
            end = limits[i + 1] - 1
            sections[i] = splited_content[start:end]
        else:
            end = len(splited_content) + 1
            sections[i] = splited_content[start:]
        

    for cap, content in sections.items():
        text = "\n".join(content)
        sections[cap] = text

    for cap, content in sections.items():
        nombre_archivo = f"Capitulo_{str(cap + 1).zfill(2)}.txt"
        ruta = os.path.join(carpeta_salida, nombre_archivo)

        # Guardar capítulo
        with open(ruta, "w", encoding="utf-8") as salida:
            salida.write(content)

        print(f"Creado: {nombre_archivo}")

    


    
            


# # Encuentra todos los inicios de capítulo en el texto original
# coincidencias = list(pattern.finditer(contenido))

# if not coincidencias:
#     print("No se han encontrado capítulos con el patrón indicado.")
# else:
#     for i, match in enumerate(coincidencias):
#         inicio = match.start()
#         # El final será el inicio del siguiente capítulo o el final del texto
#         if i + 1 < len(coincidencias):
#             final = coincidencias[i + 1].start()
#         else:
#             final = len(contenido)

#         # Extraer texto del capítulo (desde el encabezado encontrado hasta el siguiente)
#         capitulo_texto = contenido[inicio:final].strip()

#         # Número del capítulo (grupo 2 en la regex)
#         numero = match.group(2)
#         nombre_archivo = f"Capitulo_{numero.zfill(2)}.txt"
#         ruta = os.path.join(carpeta_salida, nombre_archivo)

#         # Guardar capítulo
#         with open(ruta, "w", encoding="utf-8") as salida:
#             salida.write(capitulo_texto)

#         print(f"Creado: {nombre_archivo}")
