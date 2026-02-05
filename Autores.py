class autor:
    def __init__(self,genero, nombre, edad, fecha):
        self.genero= genero
        self.nombre=nombre
        self.edad= edad
        self.fecha=fecha
        self.nacionalidad= ""
        
    def get_nombre(self):
        return self.nombre
    
    def get_edad(self):
        return self.edad
    
    def get_fecha(self):
        return self.edad
    
    def get_nacionalidad(self):
        return self.nacionalidad
    
    def set_nombre(self, nombre):
        self.nombre=nombre
        
    def set_edad(self, edad):
        self.edad=edad

    def set_nacionalidad(self, nacionalidad):
        self.nacionalidad = nacionalidad
        
    def registrar_datos(self):
        mensaje="se registraron los datos"
        return mensaje
    def buscar_autor (self, dato_buscar):
        mensaje="autor existe en las bases de datos"+ dato_buscar
        return mensaje
    def dar_baj_autor(self, dato):
        mensaje="el autor esta inactivo"+ dato
        return mensaje
    def ver_info(self):
        print(f"Nombre: {self.nombre} | Fecha: {self.fecha}")