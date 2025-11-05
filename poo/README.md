# Ejercicios propuestos de objetos y herencia

## Ejercicios resueltos de objetos simples

- [Ejercicios de objetos simples](result.py)

## Enunciados Objetos

Clase Libro 
 Crea una clase Libro con atributos como título, autor, número de páginas, 
editorial y año de publicación. 
 Implementa métodos para: 
o Mostrar información del libro. 
o Indicar si el libro tiene más de 300 páginas (es largo) o menos (es corto). 

Clase Persona 
 Define una clase Persona con atributos como nombre, edad, género y altura. 
 Implementa métodos que permitan: 
o Saludar a otras personas. 
o Verificar si la persona es mayor de edad. 
o Mostrar su edad en 5 años. 

Clase CuentaBancaria 
 Crea una clase CuentaBancaria con atributos como titular, saldo, y tipo 
de cuenta (ahorros, corriente). 
 Métodos para: 
o Depositar dinero. 
o Retirar dinero (asegúrate de no permitir retiros si el saldo es 
insuficiente). 
o Mostrar el saldo actual. 

Clase Cafetera 
 Implementa una clase Cafetera con atributos como marca, capacidad máxima 
(en litros) y nivel actual de café. 
 Métodos para: 
o Servir café (disminuye el nivel de café disponible). 
o Rellenar la cafetera a su capacidad máxima. 
o Indicar si la cafetera está vacía o llena. 

Clase Restaurante 
 Crea una clase Restaurante con atributos como nombre, tipo de cocina (ej. 
mexicana, italiana), y menú (una lista de platos). 
 Métodos que permitan: 
o Añadir un plato al menú. 
o Mostrar el menú completo. 
o Tomar un pedido y mostrar el plato elegido. 

Clase Estudiante 
 Define una clase Estudiante con atributos como nombre, curso, notas (una 
lista de calificaciones) y promedio de notas. 
 Métodos para: 
o Añadir una nueva nota. 
o Calcular el promedio de las notas. 
o Indicar si el estudiante aprobó (promedio >= 5). 

Clase Pelota 
 Crea una clase Pelota con atributos como tipo de deporte (fútbol, 
baloncesto, etc.), tamaño, y presión de aire. 
 Métodos para: 
o Inflar la pelota (aumentar la presión de aire). 
o Desinflar la pelota. 
o Mostrar el estado de la presión actual (normal, baja, alta). 

Clase Smartphone 
 Implementa una clase Smartphone con atributos como marca, modelo, memoria, 
batería, y nivel de batería actual. 
 Métodos para: 
o Llamar a un contacto (reduce el nivel de batería). 
o Cargar el teléfono (incrementa el nivel de batería). 
o Mostrar el nivel de batería actual. 

Clase Mascota 
 Crea una clase Mascota con atributos como nombre, tipo de animal (perro, 
gato, pez), y edad. 
 Métodos para: 
o Alimentar a la mascota (incrementa su energía). 
o Jugar con la mascota (disminuye su energía). 
o Mostrar la energía de la mascota y si está cansada o llena de energía. 

Clase Reloj 
 Define una clase Reloj con atributos como hora actual, minuto actual, y 
segundo actual. 
 Métodos que permitan: 
o Ajustar la hora. 
o Avanzar un minuto o un segundo. 
o Mostrar la hora actual en formato hh:mm:ss.

## Enunciados Herencia

Sistema de Transporte 
 Crea una clase base Vehiculo con atributos comunes como marca, modelo y año. 
 Luego, define clases derivadas como Coche, Motocicleta y Bicicleta. 
 Agrega métodos a las clases derivadas que simulen acciones específicas, como 
acelerar, frenar, o tocar_claxon. 
 Ejemplo de método adicional para la bicicleta: pedalear. 

Sistema de Animales 
 Define una clase base Animal con atributos como nombre y edad, y un método 
común hacer_sonido. 
 Crea clases derivadas como Perro, Gato y Pájaro. 
 Cada clase derivada debe sobrescribir el método hacer_sonido para producir el 
sonido específico de ese animal (ejemplo: el perro ladra, el gato maúlla). 
 Añade métodos específicos, como correr para el perro o volar para el pájaro.

Jerarquía de Figuras Geométricas 
 Crea una clase base Figura con atributos como color y tipo. 
 Define clases derivadas como Circulo, Cuadrado y Triangulo. 
 Cada clase derivada debe tener un método calcular_area que calcule el área según 
la figura. 
 Agrega otro método calcular_perimetro para cada figura geométrica. 

Sistema de Facturación 
 Crea una clase base Producto con atributos como nombre, precio y cantidad. 
 Define clases derivadas como Electrodomestico, Ropa y Alimento, cada una con 
un atributo específico (por ejemplo, consumo_energetico para los 
electrodomésticos, talla para la ropa, y fecha_de_vencimiento para los 
alimentos). 
 Crea un método en cada clase derivada que calcule el costo total basado en la cantidad 
y agregue alguna condición especial, como descuentos para ropa o fechas de 
caducidad para alimentos. 

Sistema de Institución Educativa 
 Crea una clase base Persona con atributos como nombre, edad y género. 
 Define clases derivadas como Estudiante, Profesor y Director. 
 Añade métodos para acciones específicas de cada rol: por ejemplo, enseñar() para el 
profesor, estudiar() para el estudiante y supervisar() para el director. 
 Implementa en cada clase derivada un método informacion() que sobrescriba el de 
la clase base para mostrar detalles específicos de cada rol (por ejemplo, el curso del 
estudiante, la asignatura del profesor, etc.).