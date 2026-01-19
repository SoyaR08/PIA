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

- sort_values(): Ordena los elementos de la serie por sus valores.

- isnull(): Devuelve una serie booleana indicando si sus valores son nulos (NaN).

- notnull(): Devuelve una serie booleana indicando si los valores son no nulos.

- unique(): Devuelve un array con los valores únicos de la serie.

- nunique(): Devuelve el número de valores únicos de la serie.

- apply(): Aplica una función a cada elemento de la serie.

- map(): Mapea los valores de la serie a través de una función o diccionario.

- replace(): Reemplaza valores en la serie.

- dropna(): Elimina los valores nulos de la serie.

- fillna(): Rellena los valores nulos con un valor especificado.

- astype(): Convierte el tipo de datos de la serie a uno especificado.

- copy(): Devuelve una copia de la serie.

- sort_index(): Ordena la serie por sus índices.

- sum(): Devuelve la suma de todos los elementos de la serie.

- mean(): Devuelve el promedio de los elementos de la serie.

- median(): Devuelve la mediana de la serie.

- std(): Devuelve la desviación estándar de la serie.

- min(): Devuelve el valor mínimo de la serie.

- max(): Devuelve el valor máximo de la serie.

- count(): Devuelve el nº de elementos no nulos en la serie.

- idxmin(): Devuelve el índice del valor mínimo de la serie.

- idxmax(): Devuelve el índice del valor máximo de la serie.

- cumsum(): Devuelve la suma acumulada de los elementos de la serie.

- cumprod(): Devuelve el producto acumulado de los elementos de la serie.

- pct_change(): Devuelve el cambio porcentual entre los elementos de la serie.

- clip(): Limita los valores de la serie entre un mínimo y un máximo.

- between(): Devuelve una serie booleana indicando si los valores están entre dos límites.

- duplicated(): Devuelve una serie booleana indicando si los valores son duplicados.

- drop_duplicates(): Elimina los valores duplicados de la serie.

- eq(): Devuelve una serie booleana de la comparación de igualdad con otro valor.

- ne(): Devuelve una serie booleana de la comparación de desigualdad.

- gt(): Devuelve una serie booleana de la comparación mayor que.

- lt(): Devuelve una serie booleana de la comparación menor que.

- ge(): Devuelve una serie booleana de la comparación mayor igual que.

- le(): Devuelve una serie booleana de la comparación menor igual que.

- add(): Suma un valor a los elementos de una serie.

- sub(): Resta un valor a los elementos de la serie.

- mul(): Multiplica los elementos de la serie por un valor.

- div(): Divide los elementos de la serie por un valor.

- mod(): Devuelve el resto de la división de los elementos de la serie por un valor.

- pow(): Eleva los elementos de la serie a una potencia.

- append(): Añade elementos al final de la serie.

- combine_first(): Combina dos series, usando los valores no nulos de la primera serie.

- align(): Alinea dos series para que tengan el mismo índice.