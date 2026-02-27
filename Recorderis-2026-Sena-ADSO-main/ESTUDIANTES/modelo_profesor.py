class Profesor:
    def __init__(self, id_p, nombre):
        self.id_p=id_p
        self.nombre=nombre

    def get_id_p(self):
        return self.id_p
    
    def get_nombre(self):
        return self.nombre

    def set_id_p(self, id_nuevo):
        self.id_p=id_nuevo

    def set_nombre(self, nombre_nuevo):
        self.nombre=nombre_nuevo

    def imprimir_info(self):
        print(f"id: {self.id_p} - nombre:{self.nombre}")        