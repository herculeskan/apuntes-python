# 1. Python: datos, tipos de datos y cómo manejarlos :car:
 
![python](img/python.png)
 
Antes de empezar me gustaría repasar el concepto de constante y variable.
 
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
 
A diferencia de las variables que pueden cambiar a lo largo del código, existen las constantes que no pueden cambiar ni reasignarse
```python
CONSTANTE = 1
#CONSTANTE siempre será 1 a lo largo del código
#Estos siempre serán escritos en mayúsculas.
```
 
 
|Palabras reservadas en python|
| :---------------------------|
| and, assert, break, continue, def, del, elif, else, except, exec, finally, for, from, global, if, import, in, is, lambda, not, or, pass, print, raise, return, try, while |
---
Estas palabras no se pueden usar como nombres de variables porque ya cumplen una función.
Ya una vez aclarado todo lo que quise aclarar.
Acá están los tipos de datos
 
| Nombre común | Nombre en Python |  Descripción|
| ----------- | ----------- | ------------------|
| Números enteros | int() | son todos los números decimales, positivos o negativos, ejemplo -5, 10 etc
| Números largos | Long() | números largos como 249842034, pero se especifican con una "L" al final, Ejemplo: 24L
| Números flotantes |float() | Son números racionales de expresión decimal, ejemplo 2,24213 |
| Números complejos | complex | números realmente extraños diseñados para resolver las raíces de números negativos. Se marcan con una j. Por ejemplo: 5j |
| Notaciones |"" | números binarios, hexadecimales, etc |
| valores booleanos | bool | los valores de true o false|
|Cadenas de strings | str() | cadenas de texto, todo lo que esté en medio de '' |
|none | '' | ausencia de valor
 
---
### Manipulación de datos
Manejar datos en Python es lo más sencillo del mundo. simplemente hay que poner el tipo entre paréntesis y luego el dato que deseas transformar. acá dejaré una serie de ejemplos:
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
 
 
#### Estructura de datos :books:
 
Al igual que muchos lenguajes de programación, python también suple la necesidad de meter varios objetos en una variable o constante, a esto se le llama *array* o *arreglo*
 
##### listas
```python
numeros = [1, 2, 3, 4, 5, 6]
#también pueden
# contener arreglos
# de diferente tipo
cosas = ['saludos',1, 2,0.432, True]
```
para acceder a los objetos de una lista (estas van de 0 a 100), usamos simplemente [ ]. por ejemplo:
 
```python
cosas[0]
#esto accederá al arreglo "saludos"
```
###### Agregar y borrar elementos de las listas.
para esto usamos métodos. Estas son funciones especiales ligadas a un tipo de dato en particular.
Empezamos con el método **append()** el cuál se usa para agregar cosas al array, acá un ejemplo
 
```python
cosas.append(False)
#a esto agrega el elemento "False" al final
```
para borrar cosas de la lista usamos el método **pop()**:
```python
cosas.pop(3)#dentro del parentesis metemos
# el índice de lo que queremos borrar
#acá se borra el objeto 0.432
```
***nota:*** *también podemos recorrer la lista con el ciclo for (el cuál tomaré apuntes próximamente)*
```python
for objetos in cosas:
   print(objetos)
```
* en caso de que quiera tener la lista al revés puedo usar el [::-1]. el :: nos sirve para viajar entre elementos y objetos, como si fuera un carro. Esto se le conoce como *slice*
```python
cosas[1:3]
#esto retornará: [0.432,True]
```
##### Tuplas :ghost:
A diferencia de las listas, las tulpas no se pueden modificar a través del tiempo.
La estructura es igual a la de las listas. Solo que en vez de usar *[ ]* usamos paréntesis *( )*
 
```python
tupla = (1, 2, 3, 4, 5)
tupla
#esto retornará lo que está dentro de la
#  tupla, en este caso: (1, 2, 3, 4, 5)
```
**No** se puede llamar ninguno de esos elementos con, por ejemplo: tupla(4) porque son objetos **inmutables o estáticos**. A diferencia de las listas que son objetos **mutables o dinámicos** los cuáles si se pueden alterar y llamar individualmente.
la ventaja de esto es que:
*  para hacer iteraciones( recorrer la lista con el ciclo for) se tiene una ejecución mucho más rápida que en las listas
 
##### Diccionarios :bookmark_tabs:
 
A diferencia de las listas y las tulpas los  diccionarios se encierran entre llaves {}. Un diccionario es una estructura de datos de llaves y valores.
A diferencia de las listas, no se accede a cada elemento del diccionario a través de su índice
 
```python
diccionario(2)
#Mala práctica, error
```
sino a través de llaves.
* Las llaves a diferencia de los indices no son números que van de 0 al límite.* En los diccionarios le ponemos nombre al índice al cual le llamamos llave.
```Python
def run():
   mi_diccionario= {
       'llave1':1,
       'llave2':2,
       'llave3':3,
   }
   print(mi_diccionario)
#Retornará {'llave1':1, 'llave2': 2,'llave3':3}
if __name__ == '__main__':
   run()
```
Para imprimirlos de manera individual simplemente los llamamos por el nombre que está en entrecomillas:
```python
print(diccionario['llave1'])
print(diccionario1['llave2'])
print(diccionario['llave3'])
#Esto retornará:
#1
#2
#3
```
###### Métodos más relevantes del diccionario.
 
* .keys() obtiene objetos claves de un diccionario:
  ```python
  Prenda = {'color': 'rosa', 'marca': 'Zara', 'talle': 'U'}
 
 for clave in valor.keys():
  print(clave)
 #esto imprimirá ['color', 'marca', 'talle']
 ```
 Ejemplo sacado de [uniwebsidad.com](https://uniwebsidad.com/libros/python/capitulo-8/metodos-de-retorno)
 
* value() obtiene valores de un diccionario
```python
diccionario = {'color': 'rosa', 'marca': 'Zara', 'talle': 'U'}
for clave in valor.value():
    print(valores)
#esto imprimirá ['rosa', 'Zara', 'U']
```
 
* items() devuelve ambos valores, la llave y el valor
 ```python
 diccionario = {'color': 'rosa', 'marca': 'Zara', 'talle': 'U'}
 for clave, valor in diccionario.items():
    print('de '+ str(clave) + str(valor))
    #ee color rosa, de marca Zara, de talleU
 
 ```
 Plus xd
 * **len()** obtener la cantidad de elementos que tiene un diccionario
 ```python
   diccionario = {'color': 'rosa', 'marca': 'Zara', 'talle': 'U'}
   len(diccionario)
   #Esto retornará 3
 
 ```
---
#### sets()
un conjunto no ordenado de elementos, se declara con {}, a diferencia del directorio no tiene relaciones clave-valor
```python
    cubiertos = {"tenedor", "cuchillo", "cuchara"}
    vajilla =set("tasa","plato", "olla")

print(cubiertos)
print(vajillas)
# (["tenedor", "cuchillo", "cuchara"])
#(["tasa","plato", "olla"])
```
un
ambos mostrarán sus valores, a diferencia de 
los directorios, los set son inmutablez


![ending](img/bucle.jpg) 
 *Bueno,  es el final de python, tipos de datos y cómo manejarlos. :car:*
 >nunca pares de aprender
 
###### El siguiente apunte es a cerca de: [Estructuras de control y bucles](/bucles.md) :smoking: 