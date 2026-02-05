from libro_modelo import Libro_modelo
from Autores import autor
from libro_bd import base_datos_libro
from api_datos_autores import Api_lista_autores

obj_api_autores=Api_lista_autores()
obj_bd=base_datos_libro()

#CON ESTE CREAMOS UN AUTOR COMO UN OBJETO
autor1 = autor("Masculino", "Samuel Perez", "28 años", "14/08/1995")
autor2 = autor("Femenino", "Kelly Contreras", "25 años", "01/12/1998")

#CON EST SE GUARDA EN LA API
obj_api_autores.guardar_autores(autor1)
obj_api_autores.guardar_autores(autor2)

#CON ESTE MOSTRAMOS LA LISTA
obj_api_autores.mostrar_lista_autores()

obj_autor=autor("genero masculino", "juan perez", "45 años", "12 de marzo de 1978")
lista_datos_autor=["Samuel", "Perez", "14/08/1995", "Colombiano"]
lista_datos_autor1=["Kelly", "Contreras", "01/12/1998", "Colombiana"]

#CREAMOS UN LIBRO COMO OBJETO
obj_libro1=Libro_modelo("10 de febrero", "250 hojas", "ciencia ficcion", "ficcion")
obj_libro2=Libro_modelo("12 de febrero", "60 hojas", "ciencia", "Voler al futuro")
obj_libro3=Libro_modelo("10 de marzo", "50 hojas", "Goku", "DragonBallz")

#GUARDAMOS EL LIBRO EN LA BASE DE DATOS
obj_bd.guardar_libros(obj_libro1)
obj_bd.guardar_libros(obj_libro2)
obj_bd.guardar_libros(obj_libro3)

#MOSTRAMOS LA INFORMACION DEL BASE DE DATOS
obj_bd.mostrar_info()





