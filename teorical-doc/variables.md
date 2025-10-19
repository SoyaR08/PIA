# Variables en Python y primeras líneas

Python es un lenguaje de programación interpretado, lo que significa que como desarrollador escribes archivos Python (.py) en un editor de texto y posteriormente el intéprete de Python los ejecuta.

### Primer programa: hola_mundo.py

```python
# Comentarios de código con almohadillas

#Primer programa Python -- Hola Mundo!

print("Hola Mundo!!!")
```

Al ejecutar el código, Python interpreta el código y nos muestra por consola el resultado de la operación indicada;

```bash
Hola Mundo!!!
Press any key to continue . . .
```

¡Ya tienes el primer programa en Python realizado!

```python
# Comentarios de código con almohadillas

#Primer programa Python -- Hola Mundo!

print("Hola Mundo!!!")

# Comentario ...

#Consultamos el tipo de dato
print(type("Hola Mundo")) # <class 'str'>
print(type(5)) # <class 'int'>
print(type(1.5)) # <class 'float'>
print(type(3 + 1j)) # <class 'complex'>
print(type(True)) # <class 'bool'>
print(type(print("Cadena de texto"))) # Cadena de texto <class 'NoneType'>
```

Para conocer el tipo de dato al que hacemos referencia, utilizamos la función disponible en Python type(dato_a_evaluar)

### Variables

Python no tiene comandos para declarar variables. Una variable se crea en el momento que se asigna un valor por primera vez.

```python
### Variables ###

my_string_variable = "My String variable"

print(my_string_variable)

my_int_variable = 5

print(my_int_variable)
```

### Reglas para definir variables:

- Un nombre de variable debe comenzar con una letra o guión bajo.
- El nombre de variable no puede comenzar con un número.
- Solo puede contener caracteres alfanuméricos y guiones bajos (A-Z, 0-9, y _).
- Los nombres de variables distinguen entre mayúsculas y minúsculas.
- Un nombre de varible no puede ser ninguna de las palabras reservadas de Python.

Python permite asignar valores a múltiples variables:

```python
var1, var2, var3 = 1, 2, 3
```

A su vez, se le puede asignar el mismo valor a múltiples variables en la misma línea:

```python
var1, var2, var3 = 1
```

Si tenemos una colección de valores en una lista, tupla, etc. Python permite extraer los valores en variables (desempaquetar):

```python
fruits = ['Plátano', 'Manzana', 'Melón']
var1, var2, var3 = fruits
print(fruits)
['Plátano', 'Manzana', 'Melón']
print(var1)
Plátano
print(var2)
Manzana
print(var3)
Melón
```

Para visualizar los datos, disponemos de la función print(). Para visualizar varios datos, concatenar variables, utilizamos las variables separadas por coma.

```python
print(var1," ",var2," ",var3)
Plátano Manzana Melón
```

### Tipos de Datos

| Utilidad            	| Nombre del tipo     	|
|---------------------	|---------------------	|
| Tipo de texto:      	| str                 	|
| Tipos numéricos:    	| int, float, complex 	|
| Tipos de secuencia: 	| list, tuple, range  	|
| Tipo de mapeo:      	| dict                	|
| Tipos de conjuntos: 	| set, frozenset      	|
| Tipo booleano:      	| bool                	|
| Tipo binario:       	| bytes, bytearray, memoryview 	|
| Ningún tipo:        	| NoneType                     	|

Las variables no necesitan declararse con ningún tipo en particular, e incluso pueden cambiar de tipo después de haber sido configuradas.

Si se desea especificar el tipo de datos de una variable, se puede realizar mediante conversión:

```python
x = str(10)
y = int(10)
z = float(10)

print("Cadena: ", x)
print("Numérico: ", y)
print("Decimal: ", z)
```