class Libro_modelo:
    def __init__(self, fecha,cant_hojas,tematica,genero):
        self.fecha= fecha
        self.cantida_hojas= cant_hojas
        self.tematica= tematica
        self.genero=genero
    
    def get_cantidad_hojas(self):
        return self.cantida_hojas
    
    def get_fecha(self):
        return self.fecha
    
    def get_tematica(self):
        return self.tematica
    
    def get_genero(self):
        return self.genero
    
    def set_cantidad_hojas(self, cantidad):
        self.cantida_hojas = cantidad

    def set_fecha(self, fecha):
       self.fecha = fecha

    def set_tematica(self, tematica):
         self.tematica = tematica

    def set_genero(self, genero):
        self.genero = genero
    
    # responsabilida de la clase          
            
    def registrar_cantidahojas(self):
        mensaje="se registraron en la base de datos"
        return mensaje
    
    def registar_fecha_libro(self):
        mensaje="las fechas se registraron en la bd"
        return mensaje
    
    def mostar_cantidad_hojas(self):
        mensaje= "el libro tien la siguiente cantidad:"
        mensaje= mensaje + self.get_cantidad_hojas()
        return mensaje
    
    def registrar_tematica(self):
        mensaje= "tematica registrada"
        return mensaje
    
    def mostar_tematica(self):
         mensaje= mensaje + self.get_tematica()
         return mensaje
    
    def info_autor(self, obj_autor):
         obj_autor.ver_info()
         
        
        