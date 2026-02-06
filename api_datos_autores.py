class Api_lista_autores:
    #Creamos el constructor
    def __init__(self):
        #Creamos el atributo
        self.Api_lista_autores=[]
        
    #METODO APPEND
    def guardar_autores(self, nuevo_autor):
        datos = [nuevo_autor.get_nombre(), nuevo_autor.get_fecha()]
        self.Api_lista_autores.append(datos)
        print("APPEND ejecutado")
        print(self.Api_lista_autores)
        
    #METODO EXTEND
    def extender_autores(self, lista_autores):
        self.Api_lista_autores.extend(lista_autores)
        print("EXTEND ejecutado")
        print(self.Api_lista_autores)
        
    #METODO INSERT
    def insertar_autor(self, autor, posicion):
        datos = [autor.get_nombre(), autor.get_fecha()]
        self.Api_lista_autores.insert(posicion, datos)
        print("INSERT ejecutado")
        print(self.Api_lista_autores)
    
    #METODO REMOVE
    def remover_autor(self, datos_autor):
        self.Api_lista_autores.remove(datos_autor)
        print("REMOVE ejecutado")
        print(self.Api_lista_autores)
        
    #METODO POP
    def eliminar_autor(self, posicion):
        eliminado = self.Api_lista_autores.pop(posicion)
        print("POP ejecutado - eliminado:", eliminado)
        print(self.Api_lista_autores)

    #METODO INDEX
    def buscar_autor(self, datos_autor):
        posicion = self.Api_lista_autores.index(datos_autor)
        print("INDEX ejecutado")
        print("Posición:", posicion)
        return posicion

    #METODO COUNT
    def contar_autor(self, datos_autor):
        cantidad = self.Api_lista_autores.count(datos_autor)
        print("COUNT ejecutado")
        print("Cantidad:", cantidad)
        return cantidad

    #METODO SORT
    def ordenar_autores(self):
        self.Api_lista_autores.sort()
        print("SORT ejecutado")
        print(self.Api_lista_autores)

    #METODO REVERSE
    def invertir_autores(self):
        self.Api_lista_autores.reverse()
        print("REVERSE ejecutado")
        print(self.Api_lista_autores)

    #MOSTRAMOS
    def mostrar_lista_autores(self):
        print("LISTA FINAL DE AUTORES:")
        for fila in self.Api_lista_autores:
            print(fila)

    # def mostrar_lista_autores(self):
    #     print(self.Api_lista_autores)

    #     for i in range(len(self.Api_lista_autores)):
    #         print("imprime por posicion MOSTRAMOS LAS FILAS")
    #         print(self.Api_lista_autores[i])

    #         for j in range (len(self.Api_lista_autores[i])):
    #             print("imprime por posicion de las hijas MOSTRAMOS LAS COLUMNAS")
    #             print(self.Api_lista_autores[i][j])

