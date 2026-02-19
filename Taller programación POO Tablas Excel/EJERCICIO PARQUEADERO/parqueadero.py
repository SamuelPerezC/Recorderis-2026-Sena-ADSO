class parqueadero:
    def __init__(self,puesto,fecha_entrada,hora_entrada,hora_salida,estado):
        self.puesto=puesto
        self.fecha_entrada=None
        self.hora_entrada=None
        self.hora_salida=None
        self.estado=estado
        
    def get_puesto(self):
        return self.puesto
    
    def set_puesto(self,nuevo_puesto):
        self.puesto=nuevo_puesto
        
    def get_fecha_entrada(self):
        return self.fecha_entrada
    
    def set_fecha_entrada(self,nueva_fecha_entrada):
        self.fecha_entrada=nueva_fecha_entrada
        
    def get_hora_salida(self,):
        return self.hora_salida
    
    def set_hora_salida(self,nueva_hora_salida):
        self.hora_salida=nueva_hora_salida
        
    def get_estado(self):
        return self.estado
    
    def set_estado(self,nuevo_estado):
        self.estado=nuevo_estado  
        
    #----------RESPONSABILIDADES-----------#
    
    def mostrar_info(self):
        return(f"Puesto: {self.puesto.get_puesto()}"
               f"Fecha Entrada: {self.fecha_entrada.get_fecha_entrada()}"
               f"Hora Entrada: {self.hora_entrada.get_hora_entrada()}"
               f"Hora Salida: {self.hora_salida.get_hora_salida()}"
               f"Estado: {self.estado.get_estado()}")
    
