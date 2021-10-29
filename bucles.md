# Estructuras de control y bucles :smoking:
![cangrejo](img/bucle.jpg)



### Conceptos a tener en cuenta:
Para lo siguiente tenemos que tener en claro que el código se ejecuta en orden 1 a 1.

```python
print('hola') ; print('hola') ; print('hola')
```
también y super importante tener en claro el concepto de ***INDENTACIÓN***.

A diferencia de otros lenguajes que *anidan* el contenido de sus datos, funciones o algoritmos en bloques de código con corchetes. Python lo hace solamente usando espacios, haciendo que su sintáxis sea mucho más fácil de leer. Una vez que te acostumbras. En otros lenguajes de programación que aprendas, notarás que tu código se ve más limpio.

acá dejo un ejemplo de indentación:
```python
instruccion_principal:
    instrucción_anidada
    otra instruccion_anidada
instruccion_independiente
```
En el anterior bloque de código está claro que la instrucción principal tiene dos instrucciones dentro. La instrucción independiente esta fuera del bloque de código lo que significa que pase lo que pase dentro de instrucción principal, la instrucción independiente se cumplirá su función igual.

----
### Bucles :smoking:

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


##### Else... if
Si queremos agregar una condición si nuestro if no se cumple, le agregamos el else. esto significaría algo como: "*si esta condición no se cumple, haz lo otro*"


<!-- ## Ideas principales
###### estos conceptos se escribirán preonto

- [x] Saltos de condicional if
* bucle while
* bucle for
* control de excepciones --> 