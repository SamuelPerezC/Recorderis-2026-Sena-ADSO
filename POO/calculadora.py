class Hacer_operaciones:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def suma(self):
        return self.numero1.get_numero() + self.numero2.get_numero()

    def resta(self):
        return self.numero1.get_numero() - self.numero2.get_numero()        

    def multiplicacion(self):
        return self.numero1.get_numero() * self.numero2.get_numero()

    def division(self):
        if self.numero2.get_numero() != 0:
            return self.numero1.get_numero() / self.numero2.get_numero()    
        else:
            return "Error: No se puede dividir por cero"
    def mostrar_info(self):
        print(f"Numero 1: {self.numero1}")
        print(f"Numero 2: {self.numero2}")
    #-------------------------HACER OPERACIONES-------------------------#
    
    def tomar_fecha(self, fecha):
        self.fecha = fecha  
        
    def get_fecha(self):
        return self.fecha   
    
    def mostrar_fecha(self):
        print(f"Fecha: {self.fecha}")
        
    #-------------------------TOMAR FECHA-------------------------#
    
    def guardar_info_tabla(self, tabla):
        self.tabla = tabla  
        
    def get_tabla(self):
        return self.tabla   
    
    def mostrar_tabla(self):    
        print(f"Tabla: {self.tabla}")
        
        