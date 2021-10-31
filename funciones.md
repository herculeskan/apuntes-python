#Funciones en Python :gun:
---
![Funciones](/img/funciones.gif)

### Definición de función

así como *print()* y *input()* cumplen una *función* nosotros también podemos crear nuestras funciones, las cuales nos sirven para meterles bloques de código hacer más corto y legible nuestro trabajo.

###### La sintaxis de la función

```python
def nombre_funcion(parametro):
    #lo que la función haga
    return result
```
1. podemos notar que el nombre de tu función viene luego de la palabra reservada *def*
2. luego del nombre de la función, usamos unos paréntesis donde metemos los parámetros de la función
3. una vez asignado el parámetro, le ponemos dos puntos y empezamos a crear el cuerpo de nuestra función. Este cuerpo es todo lo que queremos que haga cada vez que la invoquemos
***Nota a tener en cuénta:*** tenemos que tener en cuenta la identación para que funcione bien, no es obligatorio usar algo dentro de los parametros o asignarles un return; se puede llamar desde cualquier parte del código simplemente escribiendo su  nombre:
>nombre_función
<!-- * se necesita la palabra reservada *def* para definir tu función, seguida la palabra que quieras usar y el paréntesis que indica el parámetro, al final un :
>def funcion(parametro):

* los argumentos que consume la función se les llama parámetros
* cuando llamas a la función con valores específicos para los parametros. Estos se les llama argumentos o parametros reales. Esto se debe a que los argumentos en la llamada a la función son los valores usados para los parámetros de la función.
* luego empieza la indentación, debajo se le asigna un cuerpo que describe lo que hace tu función. 
* Hay una declaración de retorno que devuelve el resultado de la operción en los argumentos. La declaración de retorno devuelve el control al punto donde se llamó originalmente la función
*  Tener en cuenta que los argumentos  la declarariones de retorno son opcionales. Esto significa que podría tener una función que no acepte argumentos y que tampoco devuelva nada. -->
<!-- ###### temas a tratar:
* [ ] ÁMBITO DE LAS VARIABLES 
* [ ] DOCSTRINGS
* [ ] GENERADORES
* [ ] FUNCIONES LAMBDA -->