es_par=lambda X: "par" if X % 2 == 0 else "impar"
print(es_par(4))

#lambam debe estar asignada a una variable, se usa para ahoorar codigo

#-----------------------------------------------------

#metodos funcionales para lambda: map(hace ejecutar por ibligacion una funcion, el map ejecuta una funcion por cada posicion del array), map tiene un orden, primera funcion es: primera posicion es la funcion que quiera ejecutar segunda funcion es el objeto iterable  

#map()
numeros = [1,2,3,4]
duplicados = list(map(lambda x:x *2, numeros))
print(duplicados)

#----------------------------------------------------
#filter() es una función que sirve para sacar de una lista solo los elementos que cumplen una condición, (verdadero / falso)

numeros = [1, 2, 3, 4, 5, 6]

def es_par(n):
    return n % 2 == 0

resultado = filter(es_par, numeros)

print(list(resultado))

#FUNCION CALLBACK
def saludar(nombre):
    return "Hola " + nombre

def procesar(funcion, dato):
    return funcion(dato)

print(procesar(saludar, "Ana"))

# Concepto	Significado
# filter()	filtra una lista usando una condición
# callback	función que se pasa a otra función
# filter & map      usa callback	✅ Sí, la función que le pasas es un callback

#-------------------------------------------------------
#SORTED  👉 sorted() toma la lista, la ordena y devuelve una nueva lista.

numeros = [5, 1, 8, 3, 2]
ordenados = sorted(numeros)
print(ordenados)
#----
personas = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Luis", "edad": 20},
    {"nombre": "Pedro", "edad": 30}
]

ordenadas = sorted(personas, key=lambda persona: persona["edad"])

print(ordenadas)
#---- ordena alfabeticmente tambien
palabras = ["banana", "uva", "manzana", "pera"]
ordenadas = sorted(palabras)
print(ordenadas)


#-----ESTRUCTURA LAMBDA------

"""
-si lambda retorna implicitamente debe haber almacenamiento de datos

variable = lambda parametro: expresion

Estructura callback: funciones que esperan funciones con retorno implicito

map(funcion, objeto iterable) map retorna una copia del iterable con la modificacion que haga la funcion que enviamos

filter(estructura una funcion, objeto iterable)retorna un nuevo iterable aplicando el filtro de la funcion"""

