class Base_datos:
    def __init__(self):
        self.base_datos_profesor=[]
        self.base_datos_estudiante=[]
        self.base_datos_materia=[]

    def guardar_datos(self,obj_profesor,obj_estudiante,obj_materia):
        self.base_datos_profe.append(obj_profesor)
        self.base_datos_estudiante.append(obj_estudiante)
        self.base_datos_materia.append(obj_materia)
    
    def imprimir(self):
        for i in range(len(self.base_datos_profe)):
        print(f"{self.base_datos_profe[i].imprimir_info()}")
        print(f"{self.base_datos_estudiante[i].imprimir_info()}")
        print(f"{self.base_datos_materia[i].imprimir_info()}")

