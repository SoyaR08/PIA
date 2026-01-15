# Librería Pandas

La librería Pandas está especializada en el manejo y análisis de estructuras de datos.

## Características:

- Define nuevas estructuras de datos en los arrays de la librería NumPy pero con nuevas funcionalidades.

- Permite leer y escribir fácilmente en ficheros en formato CSV, Excel y bases de datos SQL.

- Permite acceder a los datos mediante índices o nombres para filas y columnas.

- Permite trabajar con series temporales.

- Realiza operaciones de forma muy eficiente.

## Estructuras de datos:

- Series: Unidimensionales.

- DataFrame: Bidimensionales (tablas).

- Panel: Tridimensionales (cubos).

Estas estructuras se construyen a partir de arrays de la librería NumPy.

## Series

Estructuras similares a los arrays. Sus elementos no tienen que ser del mismo tipo y no se puede modificar su tamaño pero sí su contenido.

Dispone de un índice que asocia un nombre a cada elemento de la serie, a través de la cual se accede al elemento.

### Crear Serie a partir de una Lista

```python
Series(data=lista, index=indices, dtype=tipo)
```

Devuelve un objeto de tipo Series con los datos de la lista, las filas especificadas en la lista de índices y el tipo de datos indicado en el tipo.

### Crear Serie a partir de un Diccionario

```python
Series(data=diccionario, index=indices)
```

Devuelve un objeto de tipo Series con los valores del diccionario, las filas especificadas en la lista de índices. En caso de que no se pasen, se usarán las claves del diccionario.

### Atributos de una Serie

serie.size: Devuelve el nº de elementos de la serie.

serie.index: Devuelve una lista con los nombres de las filas.

serie.dtype: Devuelve el tipo de datos de los elementos de la serie.

### Acceso a los elementos de una Serie

Podemos realizar el acceso a los elementos de una Serie bien mediante la posición o bien por el índice del elemento a mostrar:

- serie[i]: Devuelve el elemento de la posición i+1 de la serie.

- serie[rango]: Devuelve otra serie con los elementos que ocupan las posiciones dentro de ese rango.

- serie[nombre_indice]: Devuelve el elemento con el nombre en el índice.

- serie[nombres]: Devuelve otra serie con los elementos correspondientes a los nombres.

### Métodos de una Serie

- head(): Devuelve las primeras n filas de una serie.

- tail(): Devuelve las últimas n filas de una serie.

- describe(): Proporciona estadísticas resumidas de la serie.

- value_counts(): Cuenta la frecuencia de los valores únicos.