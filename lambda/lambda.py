class persona:
    def __init__(self, nombre):
        self.nombre=nombre
        
    saludar=lambda self: f"Hola soy {self.nombre}"
    
print(saludar)
    