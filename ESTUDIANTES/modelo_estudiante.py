class Estudiante:
    def __init__(self,id, nombre):
       self.id=id
       self.nombre=nombre

    #el get devuelve NO ASIGNA
    def get_id(self):
        return self.id
    
    def get_nombre(self):
        return self.nombre
    
    #el set ASIGNA
    def set_id(self, id_nueva):
        self.id=id_nueva

    def set_nombre(self, nombre_nuevo):
        self.nombre=nombre_nuevo

    def imprimir_info(self):
        print(f"id: {self.id}nombre: {self.nombre}")
