class Libro_modelo:
    def __init__(self, genero):
        self.fecha = "" 
        self.cantidad_hojas = ""
        self.tematica =""
        self.genero = genero
        
         
    
    def get_cantidad_hojas(self):
        return self.cantidad_hojas
        
        
        #hacer responsabilides de la clase libro
        
    def registrar_cantidad_hojas(self):
        mensaje = "Se registraron en la base de datos: "
        return mensaje + "cantidad de hojas del libro."
    
    def registrar_fecha_libro(self):
        mensaje = "Las fechas se registraron en la base de datos: "
        return mensaje + "fecha de publicación del libro."
    
    def Mostrar_cantidad_de_hojas(self):
        mensaje = "El libro tiene la cantidad siguiente de hojas: "
        mensaje = mensaje + self.get_cantidad_hojas()
        return mensaje
    
    def registrar_tematica(self, tematica):
        mensaje = "tematica registrada"
        return mensaje
    
    def mosrtrar_tematica(self):
        mensaje = self.get_tematica()
        return mensaje
    

    

    
    