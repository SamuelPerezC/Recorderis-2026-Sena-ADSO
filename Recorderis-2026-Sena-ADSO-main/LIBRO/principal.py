from Libro_modelo import Libro_modelo

obj_libro = Libro_modelo("accion")
dato_cant = input("Ingrese la cantidad de hojas del libro: ")
obj_libro.set_cantidad_hojas(dato_cant)
cant_hojas = obj_libro.Mostrar_cantidad_de_hojas()



