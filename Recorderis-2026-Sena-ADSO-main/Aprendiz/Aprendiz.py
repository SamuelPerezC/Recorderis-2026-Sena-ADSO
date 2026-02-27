#1. Crear la clase
class Aprendiz:
    #2. Crear el constructor
    def __init__(self, dato_nombre,dato_edad,dato_id):
        #3. Crrar los atributos - constructor
        #analizar adjetivos en español, para identificar como atributos de la clase adjetivo son las cualidades
        self.nombre_aprendiz=dato_nombre
        self.edad_aprendiz=dato_edad
        self.id_aprendiz=dato_id
        
                
 # Crear los matodos (encapsulamiento - responsabilidades)       
#RESPONSABILIDADES
    def set_id_aprendiz(self,nuevo_id):
        self.id_aprendiz=nuevo_id

    def get_id_aprendiz(self):
        return self.id_aprendiz

    def imprimir_info(self):
        info = f "Id aprendiz: {self.id_aprendiz} - Nombre Aprendiz: {self.nombre_aprendiz}"
        return info
    