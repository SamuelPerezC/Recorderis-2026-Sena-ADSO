"""
PRINCIPAL.PY - SISTEMA DE GESTIÓN DE BIBLIOTECA
Este archivo crea y manipula instancias de objetos de las clases definidas.
"""

# ==============================================
# IMPORTACIÓN DE CLASES (NO SON INSTANCIAS)
# ==============================================
# Estas son solo las DEFINICIONES de las clases
# No son objetos aún, solo los "moldes"
from libro_modelo import Libro_modelo      # Clase Libro_modelo (molde)
from Autores import autor                  # Clase autor (molde)
from libro_bd import base_datos_libro      # Clase base_datos_libro (molde)
from api_datos_autores import Api_lista_autores  # Clase Api_lista_autores (molde)

# ==============================================
# 1. CREACIÓN DE INSTANCIAS/OBJETOS PRINCIPALES
# ==============================================

# ================= INSTANCIA 1 =================
# obj_api_autores ES UNA INSTANCIA/OBJETO de la clase Api_lista_autores
# Esta instancia TIENE UN ARREGLO/LISTA interno llamado: self.Api_lista_autores
obj_api_autores = Api_lista_autores()  # ← ESTO ES UN OBJETO
# Dentro tiene: self.Api_lista_autores = [] (ARREGLO/LISTA VACÍO INICIALMENTE)

# ================= INSTANCIA 2 =================
# obj_bd ES UNA INSTANCIA/OBJETO de la clase base_datos_libro  
# Esta instancia TIENE UN ARREGLO/LISTA interno llamado: self.base_datos_libro
obj_bd = base_datos_libro()  # ← ESTO ES UN OBJETO
# Dentro tiene: self.base_datos_libro = [] (ARREGLO/LISTA VACÍO INICIALMENTE)

# ==============================================
# 2. CREACIÓN DE INSTANCIAS/OBJETOS DE AUTORES
# ==============================================

# ================= INSTANCIA 3 =================
# autor1 ES UNA INSTANCIA/OBJETO de la clase autor
# NO contiene listas internas, solo atributos simples
autor1 = autor("Masculino", "Samuel Perez", "28 años", "14/08/1995")  # ← ESTO ES UN OBJETO

# ================= INSTANCIA 4 =================
# autor2 ES OTRA INSTANCIA/OBJETO de la clase autor (diferente a autor1)
# NO contiene listas internas, solo atributos simples
autor2 = autor("Femenino", "Kelly Contreras", "25 años", "01/12/1998")  # ← ESTO ES UN OBJETO

# ================= INSTANCIA 5 =================
# autor3 ES OTRA INSTANCIA/OBJETO de la clase autor (diferente a las anteriores)
# NO contiene listas internas, solo atributos simples
obj_autor = autor("genero masculino", "juan perez", "45 años", "12 de marzo de 1978")  # ← ESTO ES UN OBJETO

# ==============================================
# 3. LISTA DE DATOS (ES UN ARREGLO/LISTA 2D)
# ==============================================
# ¡¡¡IMPORTANTE!!!: ESTO ES UN ARREGLO/LISTA de Python
# NO es una instancia de nuestras clases, es una LISTA 2D (lista de listas)
lista_datos_autor = [  # ← ¡¡¡ESTO ES UN ARREGLO/LISTA 2D!!!
    # Elemento 0: ARREGLO/LISTA con 4 elementos
    ["Kelly", "Contreras", "01/12/1998", "Colombiana"], 
    # Elemento 1: ARREGLO/LISTA con 4 elementos
    ["Samuel", "Perez", "14/08/1995", "Colombiano"]
]
# Estructura de esta LISTA 2D:
# Índice 0: ["Kelly", "Contreras", "01/12/1998", "Colombiana"] ← LISTA INTERNA
# Índice 1: ["Samuel", "Perez", "14/08/1995", "Colombiano"]    ← LISTA INTERNA

# ==============================================
# 4. CREACIÓN DE INSTANCIAS/OBJETOS DE LIBROS
# ==============================================

# ================= INSTANCIA 6 =================
# obj_libro1 ES UNA INSTANCIA/OBJETO de la clase Libro_modelo
# NO contiene listas internas, solo atributos simples
obj_libro1 = Libro_modelo("10 de febrero", "250 hojas", "ciencia ficcion", "ficcion")  # ← ESTO ES UN OBJETO

# ================= INSTANCIA 7 =================
# obj_libro2 ES OTRA INSTANCIA/OBJETO de la clase Libro_modelo
# NO contiene listas internas, solo atributos simples
obj_libro2 = Libro_modelo("12 de febrero", "60 hojas", "ciencia", "Voler al futuro")  # ← ESTO ES UN OBJETO

# ================= INSTANCIA 8 =================
# obj_libro3 ES OTRA INSTANCIA/OBJETO de la clase Libro_modelo
# NO contiene listas internas, solo atributos simples
obj_libro3 = Libro_modelo("10 de marzo", "50 hojas", "Goku", "DragonBallz")  # ← ESTO ES UN OBJETO

# ==============================================
# 5. OPERACIONES CON LA INSTANCIA obj_api_autores
# (QUE CONTIENE EL ARREGLO/LISTA self.Api_lista_autores)
# ==============================================

print("=== GUARDANDO AUTORES EN API ===")
# Llamando métodos del OBJETO obj_api_autores (instancia 1)
# Estos métodos modifican el ARREGLO/LISTA interno: self.Api_lista_autores
obj_api_autores.guardar_autores(autor1)  # ← Agrega a self.Api_lista_autores
obj_api_autores.guardar_autores(autor2)  # ← Agrega a self.Api_lista_autores
obj_api_autores.guardar_autores(obj_autor)  # ← Agrega a self.Api_lista_autores
# Ahora self.Api_lista_autores contiene 3 elementos (listas de 2 strings)

print("\n=== INSERTANDO AUTOR ===")
# Insertar autor en el ARREGLO/LISTA self.Api_lista_autores en posición 0
obj_api_autores.insertar_autor(autor1, 0)  # ← Modifica self.Api_lista_autores

print("\n=== ORDENANDO AUTORES ===")
# Ordena el ARREGLO/LISTA self.Api_lista_autores alfabéticamente
obj_api_autores.ordenar_autores()  # ← Ordena self.Api_lista_autores

print("\n=== INVIRTIENDO AUTORES ===")
# Invierte el orden del ARREGLO/LISTA self.Api_lista_autores
obj_api_autores.invertir_autores()  # ← Invierte self.Api_lista_autores

print("\n=== ELIMINANDO AUTOR (POP) ===")
# Elimina elemento en posición 1 del ARREGLO/LISTA self.Api_lista_autores
obj_api_autores.eliminar_autor(1)  # ← Elimina de self.Api_lista_autores

print("\n=== EXTENDIENDO CON LISTA MANUAL ===")
# Extiende el ARREGLO/LISTA self.Api_lista_autores con otra lista
# Agrega los 2 elementos de lista_datos_autor (que es una LISTA 2D)
obj_api_autores.extender_autores(lista_datos_autor)  # ← Extiende self.Api_lista_autores

print("\n=== BUSCANDO AUTOR (INDEX) ===")
# Busca posición en el ARREGLO/LISTA self.Api_lista_autores
try:
    obj_api_autores.buscar_autor(["Samuel Perez", "28 años"])
except ValueError as e:
    print("Autor no encontrado:", e)

print("\n=== CONTANDO AUTOR (COUNT) ===")
# Cuenta ocurrencias en el ARREGLO/LISTA self.Api_lista_autores
obj_api_autores.contar_autor(["Samuel Perez", "14/08/1995"])

print("\n=== LISTA FINAL DE AUTORES ===")
# Muestra todo el contenido del ARREGLO/LISTA self.Api_lista_autores
obj_api_autores.mostrar_lista_autores()  # ← Muestra self.Api_lista_autores

# ==============================================
# 6. OPERACIONES CON LA INSTANCIA obj_bd
# (QUE CONTIENE EL ARREGLO/LISTA self.base_datos_libro)
# ==============================================

print("\n\n=== OPERACIONES CON LIBROS ===")

print("\n=== GUARDANDO LIBROS EN BD ===")
# Llamando métodos del OBJETO obj_bd (instancia 2)
# Estos métodos modifican el ARREGLO/LISTA interno: self.base_datos_libro
obj_bd.guardar_libros(obj_libro1)  # ← Agrega a self.base_datos_libro
obj_bd.guardar_libros(obj_libro2)  # ← Agrega a self.base_datos_libro  
obj_bd.guardar_libros(obj_libro3)  # ← Agrega a self.base_datos_libro
# Ahora self.base_datos_libro contiene 3 elementos (objetos Libro_modelo)

print("\n=== INFORMACIÓN DE LIBROS EN BD ===")
# Muestra información de todos los objetos en el ARREGLO/LISTA self.base_datos_libro
obj_bd.mostrar_info()  # ← Recorre self.base_datos_libro

# ==============================================
# 7. DEMOSTRACIÓN DE RELACIÓN ENTRE OBJETOS
# ==============================================

print("\n=== DEMOSTRACIÓN RELACIÓN LIBRO-AUTOR ===")
# obj_libro1 (instancia 6) llama a un método pasándole obj_autor (instancia 5)
print("Mostrando información del autor desde el libro:")
obj_libro1.info_autor(obj_autor)  # ← obj_libro1 ES UN OBJETO, obj_autor ES UN OBJETO

print("\n=== PROGRAMA FINALIZADO ===")

# ==============================================
# RESUMEN DE ARREGLOS/LISTAS EN EL SISTEMA:
# ==============================================
# TENEMOS 3 ARREGLOS/LISTAS PRINCIPALES:
#
# 1. self.Api_lista_autores  → ARREGLO/LISTA dentro de obj_api_autores
#    - Ubicación: Dentro del objeto obj_api_autores
#    - Tipo: Lista de listas (2D)
#    - Contiene: [["nombre", "fecha"], ["nombre", "fecha"], ...]
#    - Se modifica con: guardar_autores(), insertar_autor(), etc.
#
# 2. self.base_datos_libro   → ARREGLO/LISTA dentro de obj_bd
#    - Ubicación: Dentro del objeto obj_bd
#    - Tipo: Lista de objetos
#    - Contiene: [obj_libro1, obj_libro2, obj_libro3, ...]
#    - Se modifica con: guardar_libros(), insertar_libros(), etc.
#
# 3. lista_datos_autor       → ARREGLO/LISTA 2D en principal.py
#    - Ubicación: Variable global en principal.py
#    - Tipo: Lista 2D (lista de listas)
#    - Contiene: [["Kelly", "Contreras", ...], ["Samuel", "Perez", ...]]
#    - Se usa para: Pruebas y extensión de datos
#
# 8 OBJETOS CREADOS en total
# ==============================================

# ==============================================
# EJEMPLO VISUAL DEL CONTENIDO DE LOS ARREGLOS:
# ==============================================
# DESPUÉS DE EJECUTAR ESTE CÓDIGO:
#
# ARREGLO 1 (self.Api_lista_autores):
# [
#   ["Samuel Perez", "28 años"],
#   ["Kelly Contreras", "25 años"], 
#   ["juan perez", "45 años"],
#   ["Kelly", "Contreras", "01/12/1998", "Colombiana"],
#   ["Samuel", "Perez", "14/08/1995", "Colombiano"]
# ]
#
# ARREGLO 2 (self.base_datos_libro):
# [
#   <objeto Libro_modelo: "ciencia ficcion">,
#   <objeto Libro_modelo: "ciencia">,
#   <objeto Libro_modelo: "Goku">
# ]
#
# ARREGLO 3 (lista_datos_autor) NO cambia:
# [
#   ["Kelly", "Contreras", "01/12/1998", "Colombiana"],
#   ["Samuel", "Perez", "14/08/1995", "Colombiano"]
# ]
# ==============================================