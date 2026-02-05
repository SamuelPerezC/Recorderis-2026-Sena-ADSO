class Api_lista_autores:
    def __init__(self):
        self.Api_lista_autores=[]

    def guardar_autores(self, nuevo_autor):
        datos_nuevos = [nuevo_autor.get_nombre(),nuevo_autor.get_fecha()]
        self.Api_lista_autores.append(datos_nuevos)

    def mostrar_lista_autores(self):
        print(self.Api_lista_autores)

        for i in range(len(self.Api_lista_autores)):
            print("imprime por posicion")
            print(self.Api_lista_autores[i])

            for j in range (len(self.Api_lista_autores[i])):
                print("imprime por posicion de las hijas")
                print(self.Api_lista_autores[i][j])

