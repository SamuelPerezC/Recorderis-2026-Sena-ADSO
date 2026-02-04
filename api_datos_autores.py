class Api_lista_autores:
    def __init__(self):
        self.Api_lista_autores=[]

    def guardar_autores(self, lista_autor):
        self.Api_lista_autores.append(lista_autor)
        print(self.Api_lista_autores)

