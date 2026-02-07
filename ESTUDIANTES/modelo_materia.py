class Materia:
    def __init__(self, id_m, nombre,cantidad_niños):
        self.lista_niños=[]
        self.id_m=id_m
        self.nombre=nombre
        self.cantidad_niños=cantidad_niños
    
    def get_id_m(self):
        return self.id_m

    def get_nombre(self):
        return self.nombre   

    def get_cantidad(self):
        return self.cantidad_niños

    #----------------------------#

    def set_id_m(self, id_nuevo):
        self.id_m= id_nuevo

    def set_nombre(self, nombre_nuevo):
        self.nombre= nombre_nuevo  

    def set_cantidad(self, cantidad_nueva):
        self.cantidad_niños=cantidad_nueva

    #---------------------------#

    def imprimir_info(self):
        print(f"id_materia:{self.id_m} - nombre: {self.nombre} - cantidad de niños: {self.cantidad_niños}")
    