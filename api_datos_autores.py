class Api_lista_autores:
    #Creamos el constructor
    def __init__(self):
        #Creamos el atributo
        self.Api_lista_autores=[]
        
    #METODO APPEND
    def guardar_autores(self, nuevo_autor):
        datos_nuevos = [nuevo_autor.get_nombre(),nuevo_autor.get_fecha()]
        self.Api_lista_autores.append(datos_nuevos)
        print("Se esta utilizando el metodo Append")
        
    #METODO EXTEND
    def extender_autores(self,lista_autores):
        self.Api_lista_autores.extend(lista_autores)
        print("Se esta utilizando el metodo Extend" , self.Api_lista_autores)
        
    #METODO INSERT
    def insertar_autor(self, autor, posicion):
        datos_autor = [autor.get_nombre(), autor.get_fecha()]
        self.Api_lista_autores.insert(posicion, datos_autor)
        print("Se esta utilizando el metodo insert")
    
    #METODO REMOVE
    def remover_autor(self, datos_autor):
        self.Api_lista_autores.remove(datos_autor)
        print("Se esta utilizando el metodo Remove")
        
    #METODO POP
    def eliminar_autor(self, posicion):
        self.Api_lista_autores.pop(posicion)
        print("Se esta utilizando el metodo Pop")

    #METODO INDEX
    def buscar_autor(self, datos_autor):
        return self.Api_lista_autores.index(datos_autor)
        print("Se esta utilizando el metodo index")

    #METODO COUNT
    def contar_autor(self, datos_autor):
        return self.Api_lista_autores.count(datos_autor)
        print("se esta utilizando el metodo count")

    #METODO SORT
    def ordenar_autores(self):
        self.Api_lista_autores.sort()
        print("se esta utilizando el metodo sort")

    #METODO REVERSE
    def invertir_autores(self):
        self.Api_lista_autores.reverse()
        print("se esta utilizando el metodo reverse")


    def mostrar_lista_autores(self):
        print(self.Api_lista_autores)

        for i in range(len(self.Api_lista_autores)):
            print("imprime por posicion MOSTRAMOS LAS FILAS")
            print(self.Api_lista_autores[i])

            for j in range (len(self.Api_lista_autores[i])):
                print("imprime por posicion de las hijas MOSTRAMOS LAS COLUMNAS")
                print(self.Api_lista_autores[i][j])

