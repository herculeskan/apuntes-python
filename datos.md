#1. Tipos de datos en Python

![python](img/python.png)

Antes de empezar me gustaría repasar el cencepto de constante y variable.

La definición de *variable* es todo lo que ocupa un espacio en la memoria. Este se le puede reasignar un valor

a diferencia de JavaScript las variables no se marcan con var:
```JavaScript
var = 1
```
sino que se escribe sola
```python
esto_es_una_variable = 1
#Como buena práctica se espera escribir todo en minuscula
#y separado con guión bajo
```

A diferencia de las variables que pueden cambiar a lo largo del código, existen las constantes que no pueden cambiar ni re-asignarse
```python
CONSTANTE = 1
#CONSTANTE siempre será 1 a lo largo del código
#Estos siempre serán escritos en mayúsculas.
```


|Palabras reservadas en python|
| :---------------------------|
| and, assert, break, continue, def, del, elif, else, except, exec, finally, for, from, global, if, import, in, is, lambda, not, or, pass, print, raise, return, try, while |
---
Estas palabras no pueden usar como nombres de variables porque ya cumplen una función.
Ya una vez aclarado todo lo que quise aclarar.
Acá están los tipos de datos

| Nombre común | Nombre en Python |  Descripción|
| ----------- | ----------- | ------------------|
| Numeros enteros | int() | son todos los números decimales, positivos o negativos, ejemplo -5, 10 etc
| Numeros largos | Long() | números largos como 249842034, pero se especifican con una "L" al final, Ejemplo: 24L
| Números flotantes |float() | Son números racionales de expresión decimal, ejemplo 2,24213 |
| Números complejos | complex | números realmente extraños diseñados para resolver las raíces de números negativos. Se marcan con una j. Por ejemplo: 5j |
| Notaciones |"" | números binarios, hexagesimales, etc |
| valores booleanos | bool | los valores de true o false|
|Cadenas de strings | str() | cadenas de texto, todo lo que esté en medio de '' |
|none | '' | ausencia de valor

---
###Manipulación de datos
 manipular datos en Python es lo más sencillo del mundo. simplemente hay que poner el tipo entre paréntesis y luego el dato que deseas transformar. acá dejaré una serie de ejemplos:
 ```python
 texto = '10'
 print type(texto)
 #esto imprimirá: <type 'str>
 #también existe el atributo type que nos
 #ayuda a saber que tipo de dato estamos
 #manejando
 ```
 Otro ejemplo para entender el type
 ```python
 texto = "10"
 decimal = 21.5
 un_entero = int(texto)
 print type(texto)
 print type(decimal)
 print type(un_entero)
 print type (int(decimal))
 ### la salida del programa será:
 #<type 'str'>
 #<type 'init'>
 #<·type 'float'>
 #<type 'init'>
 ```
 ```python
 #convertir un número o cadena en un número largo
 corto =10
 largo = long(corto)

 #convertir un número en un número flotante:
 flotante = float(4)

 #convertir un número o cadena de valores a números enteros
 flotante = 4.234233
 entero = int(flotante)
 ```
 ### Operadores

|normales | de asignación |
| ------- | ------------- |
| suma(+) | +=            |
| resta(-) | -=           |
| división(/) | /=        |
|exponente(**) | **=      |
| división entera(//) | //= | //= |
| modulo(%) | %=          |
----------------------------
### Operadores de comparación
* igualdad(==)   
* desigualdad(!=)
* mayor que (>)
* menor que  (<) 
* mayor o igual que (>=)
* menor o igual que (<=)

***Operadores de cadena***
más(+) concatenar...... (*) multiplicar

---
### Operadores lógicos
* and (&)
* or (|)
* not (!=)
*nota:* a diferencia de otros lenguajes python puede presentar los operadores lógicos con palabras textuales

***Tabla de operador and***
| primer operando | segundo operando | resultado |
| --------------- |------------------| --------- |
| true           | true        | true |
|true        | false    | false |
|false | true | false
|false | false | false
-----
***Tabla de operador or***
| primer operando | segundo operando | resultado |
| --------------- |------------------| --------- |
|true | true | true |
|true | false | true |
|false | true | true |
|false | false | false |

### Operadores

|normales | de asignación |
| ------- | ------------- |
| suma(+) | +=            |
| resta(-) | -=           |
| división(/) | /=        |
|exponente(**) | **=      |
| división entera(//) | //= | //= |
| modulo(%) | %=          |
----------------------------
###Operadores de comparación
* igualdad(==)   
* desigualdad(!=)
* mayor que (>)
* menor que  (<) 
* mayor o igual que (>=)
* menor o igual que (<=)

***Operadores de cadena***
más(+) concatenar...... (*) multiplicar

---
###Operadores lógicos
* and (&)
* or (|)
* not (!=)
*nota:* a diferencia de otros lenguajes python puede presentar los operadores lógicos con palabras textuales

***Tabla de operador and***
| primer operando | segundo operando | resultado |
| --------------- |------------------| --------- |
| true           | true        | true |
|true        | false    | false |
|false | true | false
|false | false | false
-----
***Tabla de operador not***

| Operador | resultado |
| --------------- |------------------ |
|true | false |
|false | true |


#### Estructura de datos

A diferencia