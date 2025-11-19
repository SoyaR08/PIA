## Expresiones Regulares Python
Crea dos archivos JSON: uno llamado alumnos.json y otro vehiculos.json.
Cada archivo tendrá un conjunto de datos. En alumnos.json, almacena información
sobre los alumnos, y en vehiculos.json, información sobre los vehículos.
Utiliza expresiones regulares en Python para filtrar y validar información en cada
archivo, tal como correos electrónicos, matrículas, números de teléfono y otros detalles.
Archivo alumnos.json
Este archivo contiene información sobre cada alumno, con las siguientes claves:
 nombre: Nombre completo del alumno.
 email: Dirección de correo electrónico.
 telefono: Número de teléfono (9 dígitos, comenzando por 6, 7 o 9).
 codigo_postal: Código postal (5 dígitos).
 curso: Curso en el que está inscrito el alumno (ej. "DAW2").
Ejemplo de ALUMNOS.JSON
Expresiones Regulares Python
Archivo vehiculos.json
Este archivo contiene información sobre vehículos, con las siguientes claves:
 matricula: Matrícula del vehículo (formato de matrícula española: 4 dígitos
seguidos de 3 letras, como "1234ABC").
 marca: Marca del vehículo.
 modelo: Modelo del vehículo.
 año: Año de fabricación (4 dígitos, entre 1900 y el año actual).
 propietario_email: Email del propietario (debe ser válido).
Ejemplo de VEHICULOS.JSON
Se deberá realizar las siguientes funciones/operaciones sobre los ficheros JSON indicados:
Carga de datos: Función cargar_datos, abre y carga el contenido JSON.
Validación de Alumnos:
 patron_email valida que el email sea correcto.
 patron_telefono comprueba que el teléfono comienza por 9, 6 o 7 y tiene 9 cifras.
 patron_codigo_postal verifica que el código postal tenga exactamente 5 dígitos.
Validación de Vehículos:
 patron_matricula verifica que la matrícula siga el formato español de 4 números y 3
letras.
 patron_ano acepta años entre 1900 y el actual.
 patron_email valida el email del propietario.
