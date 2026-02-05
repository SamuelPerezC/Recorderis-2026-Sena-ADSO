class base_datos_libro:
    def __init__(self):
        self.base_datos_libro= []

    def guardar_libros(self, obj_libro):
        self.base_datos_libro.append(obj_libro)
        print("libro guardado en la base de datos", self.base_datos_libro[0].get_tematica())
    
    def extender_libros(self, nueva_lista):
        self.base_datos_libro.extend(nueva_lista)

    def insertar_libros(self, obj_libro, pos_index):
        self.base_datos_libro.insert(pos_index, obj_libro)

    def remover_libros(self, obj_libro):
        self.base_datos_libro.remove(obj_libro)

    def eliminar_libros(self, pos_index):
        self.base_datos_libro.pop(pos_index)

    def buscar_libros(self, Nombre_obj):
        self.base_datos_libro.index(Nombre_obj)

    def contar_libros(self, valor):
        self.base_datos_libro.count(valor)
    
    def ordenar_libros(self):
        self.base_datos_libro.sort()

    def invertir_libros(self):
        self.base_datos_libro.reverse()

    

    def mostrar_info(self):
        for i in range(len(self.base_datos_libro)):
            tematica= self.base_datos_libro[i].get_tematica()
            fecha= self.base_datos_libro[i].get_fecha()
            print(f"tematica libro: {tematica} - fecha libro: {fecha}")
            
        