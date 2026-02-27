from modelo_profesor import Profesor
from modelo_estudiante import Estudiante
from modelo_materia import Materia
from base_de_datos import Base_datos


obj_profesor_1=Profesor("1", "Julian")
obj_estudiante=Estudiante("2", "Maria")
obj_materia=Materia("32", "Mate", "22")
obj_base_datos=Base_datos()

obj_base_datos.guardar_datos(obj_estudiante,obj_profesor_1,obj_materia)
obj_base_datos.imprimir()



