# Estructuras de control y bucles :smoking:
![cangrejo](img/bucle.jpg)



### Conceptos a tener en cuenta:
Para lo siguiente tenemos que tener en claro que el código se ejecuta en orden 1 a 1.

```python
print('hola') ; print('hola') ; print('hola')
```
también y super importante tener en claro el concepto de ***INDENTACIÓN***.

A diferencia de otros lenguajes que *anidan* el contenido de sus datos, funciones o algoritmos en bloques de código encerrados en corchetes. Python lo hace solamente usando espacios, haciendo que su sintáxis sea mucho más fácil de leer. Una vez que te acostumbras. En los siguientes lenguajes de programación que prendas, notarás que escribes de forma más limpia.

acá dejo un ejemplo de indentación:
```python
instruccion_principal:
    instrucción_anidada
    otra instruccion_anidada
instruccion_independiente
```
>En el bloque anterior podemos apreciar que la instrucción principal anida dentro dos instrucciones. Podemos intuir que la instruicción independiente que está  al nivel de la instrucción principal es otro bloque de código y funciona fuera de la instrucción principal. Lo que significa que sin importar que pase dentro de la función principal; la independiente seguirá su camino


----
#### Indentación :smoking:

Para sacarle provecho a lo anterior aprendido sobre la indentación. Trataré de explicar los bucles.
Estas son una especie de factores o requisitos para que se pueda ejecutar. Lo que nos permite manipular mejor la lógica del código

#### Salto condicional if
La función de este es sencillo. Si la condición es verdadera, el código ejecutara, de lo contrario no.
acá una breve sintax 
```python
if condicion_verdadera:
    hara_esto
```
¿fácil verdad?
ahora veamos un pequeño ejemplo:
```python
a = 1
b = 2
if a < b:
    print('a es más pequeño que b')
```
*output*
```python
 a es más pequeño que b
```
En el ejemplo anterior tenemos dos variables, if verificó si la condición que teníamos era correcta y al ser esta cierta, imprimió "*a es más pequeño que b*"


#### Else... if
Si queremos agregar una condición si nuestro if no se cumple, le agregamos el else. esto significaría algo como: "*si esta condición no se cumple, haz lo otro*".
La sintaxis sería algo asi:
```
if condición:
    ejecuta esto si la condición es True
else:
    ejecuta esto si la condición es false
```
Como hablamos anteriormente de la indentación. El else tiene que estar al nivel del if para que funcione. porque  si esta al nivel de la condición podría crear un problema.

otro ejemplo para que te des una idea de como funciona el else if
```python
a=1 
b=2
if a > b:
    print('a es mayor que b')
else:
    print('a no es mayor que b')
```
*el output sería:*
```
a no es mayor que b
```
para agregar, se sabe que no se puede meter un bloque de código entre el else y el if porque esto causaría error
```python
if 1 > 2:
   print("1 es mayor que 2")
print("hola mundo")
else:
   print("1 es menor que 2")
```
*output*
```
File "<stdin>", line 3
print("hola mundo")
^
SyntaxError: invalid syntax
```
---
#### elif

Entender elif es más sencillo que lo anterior. Elif es lo que pasa si if tiene más de dos caminos o opciones a escoger, como si el código dijera: *"si la primera opción es verdadera, sino has esto, y si no resulta has aquello"*.
Le explicaré con una sintaxis:
```
if primera condición:
    ejecutar sentencia
elif segunda condición:
    ejecutrar otra sentencia
else: ejecutar esta sentencia 
si las anteriores no sirven
```
podemos usar los elif que queramos:

```python
x = 1
if x > 10
    print(" x es mayor que 10)
elif x < 10:
    print("x es menor que 10)
elif x < 20:
    print("x es menor que 20")

else:
    print(" es igual a 10")
```
output
>x es menor que 10!


---
### Bucle
Un bucle (loop) es un código que se ejecuta multiples veces.

#### Bucle while
En cierto caso, el bucle while te va a permitir hacer bucles con tu código mientras una condicion sea cierta; cuando se vuelve falsa se termina el bucle.
La sintáxis básica es:
```
a = 0

while a < 10
    ejecuta esto mientras sea 10
```
Par entenderlo mejor, aquí va un ejemplo:
```python
saludo = 0
gente = ['paula', 'pepe', 'jose', 'robertina' ]
while saludo < 4:
    print("saludos a "+ gente[personas])
    saludo +=1

```
>mientras que saludo sea menor a 4 imprimirá  "saludos gente[persona dentro del arrelgo]" 

*El output sería*
>saludos a  paula
>saludos a pepe
>saludos a jode
>saludos a robertina 
Te lo explico para que quede más claro:
1. La variable "saludo" tiene el valor de 0
2. la variable gente es asignada en una lista con 4 perdonas
3. el bucle while comienza
4. el bloque de código se ejecutará hasta que la condición deje de cumplirse
5. la condición es 'saludo < 4' lo que significa que el  bucle se cumplirá mientras saludo sea menor a 4
6. la variable saludo se actualiza en cada iteración
7. cuando vuelve el bucle while ejecuta por primera vez la linea "saludos a paula" se imprime en la consola que saludo es igual a 1
8. Continúa sumandose de 1 en 1 hasta llegar a 4



[Articulo de apoyo](https://www.freecodecamp.org/espanol/news/explicacion-del-bucle-while-de-while/)

---

#### Bucle for

A diferencia del bucle *while* que tiene que cumplir una condición, el
bucle *for* no necesita ningún tipo de condición, se traduciría algo como "*por cada valor que tenga tu objeto hará x cosa".
acá les dejaré un ejemplo:

```
for valor in lista_de_valores:
    usar variable dentro de este bloque de código

```
* "*for, in*" son palabras reservadas dentro del bucle for
* se pueden interpretar de la siguiente forma:
  * "*por cada <valor> en <listas>

por lo general se usa cualquier cosa como valor del iterador, estos serán asignadds al objeto *iterar*. Un ejemplo de esto:
```python
lista_tulpas = [(1,2), (3,4)]

for a, b in lista_tulpas:
    print("a:"a,"b:",b)
    
```
- a,b: son los valores a iterar
- lista_tulpas: el objeto a iterar

***output***
```
a: 1 b:2
a:3 b:4
```
---

#####Diferentes formas de usar bucles for:

###### 1. range()-rango
´´´python
for i in range(10)
print(i)
´´´
*output*
>0 
>1
> 2
 > 3
  > 4
   > 5
    > 6
     > 7
      > 8
       > 9


La función range es un tipo de secuencia inmutable. Se mostrarán todos los números del 0 al 9 porque el rango son 10.

Es como un contador. pero se le pueden agregar variaciones:

```python
for i in range(4,10,2)
    print(i)
```
*output*
>4
>6
>8

el primer parámetro(4) es donde se inicia el rango, el segundo es donde termina(10) y el tercero (2) es como sigue los pasos, en este caso de 2 en 2

###### 2. zip()
itera sobre doslistas del mismo tamaño en una sola función

```python
A = ["a", "b", "c"]
B = ["a", "d", "e"]
for a,b in zip(A,B):
    print a,b === b
```
*output*
´´´
a a True
d b False
c e Fals
´´´
>nota: parece que también sirve para comparar

###### 3. enumerate()
Iterar sobre una lista y obtener el índice correspondiente 

```python
A = ["esto", "es", "algo" "divertido"]

for indice.palabra in enumerate(A):
    print(indice, palabra)
```
*output*
```
0 esto
1 es
2 algo
3 divertido
```
>_nota_: si necesita acceder al índice de uan iteración. Nunca se utiliza range(len(iterble)). Esto es una mala practica, al contrario se debe usar enumerate():



<!-- 

 * [x] Saltos de condicional if
* [x] bucle while
* bucle for
* control de excepciones --> 