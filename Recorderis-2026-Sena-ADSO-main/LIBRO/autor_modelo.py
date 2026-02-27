class Autor_modelo:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    
    def registrar_nombre(self):
        mensaje = "Autor: "
        return mensaje + "el nombre del autor registrado."

    def registrar_edad(self):
        mensaje = ", Edad: "
        return mensaje + "la edad del autor registrado."

    def registrar_nacionalidad(self):
        mensaje = ", Nacionalidad: "
        return mensaje + "la nacionalidad del autor registrado."
    
    def dar_baja_autor(self):
        mensaje = "Autor dado de baja: "
        return mensaje + "Autor dado de baja de la base de datos."

    # Responsabilidades (verbos)
    def registrar_autor(self):
        return "Autor registrado en la base de datos."
