# Ejercicios propuestos de fechas

### Obtener la fecha actual y formatearla 
Crea una función que obtenga la fecha y hora actuales, luego formatea la fecha para que 
se muestre en el formato DD/MM/YYYY HH:MM:SS. 
- Usa datetime.now() para obtener la fecha y hora actual. 
- Formatea la fecha en el formato DD/MM/YYYY HH:MM:SS usando strftime. 

### Convertir una cadena a una fecha 
Escribe una función que reciba una cadena en formato DD/MM/YYYY y la convierta en un 
objeto datetime usando strptime(). 
- La cadena debe ser convertida a un objeto datetime. 
- Muestra la fecha convertida. 

### Calcular la diferencia en días entre dos fechas 
Crea una función que reciba dos cadenas de fecha en formato DD/MM/YYYY y calcule 
cuántos días hay entre ambas. 
- Convierte ambas cadenas a objetos datetime. 
- Resta las dos fechas y devuelve el número de días de diferencia. 

### Sumar días a una fecha 
Escribe una función que reciba una fecha en formato DD/MM/YYYY y un número de días, 
y luego devuelva la nueva fecha después de sumar esos días. 
- Convierte la cadena de fecha en un objeto datetime. 
- Usa timedelta para sumar los días a la fecha. 
- Muestra la nueva fecha resultante. 

### Convertir una fecha a otro formato 
Crea una función que reciba una fecha en formato YYYY-MM-DD y la convierta en el 
formato DD/MM/YYYY. 
- Usa strptime para convertir la cadena en un objeto datetime. 
- Formatea la fecha en el nuevo formato utilizando strftime.