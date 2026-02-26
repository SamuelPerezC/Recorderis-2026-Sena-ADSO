import tkinter as tk
from tkinter import messagebox

from usuario import Usuario
from numero import Numero
from calculadora import Calculadora

# ===============================
# INTERFAZ GRÁFICA
# ===============================
ventana = tk.Tk()
ventana.title("Calculadora con toma de informacion")
ventana.geometry("400x500")

tk.Label(ventana, text="CALCULADORA + TOMA DE INFORMACION", font=("Arial", 14, "bold")).pack(pady=10)


#toma de informacion para los campos
def calcular(tipo_de_operacion):
    # 1️⃣ Obtener TODOS los datos
    # el metodo debe tomar la informacion y de guaradarla y mostrarla en la tabla, que quede de forma acumulador
    nombre = entry_nombre.get()
    cedula = entry_cedula.get()
    valor1 = entry_numero1.get()
    valor2 = entry_numero2.get()

    # 2️⃣ Convertir números
    valor1 = int(valor1)
    valor2 = int(valor2)

    # 3️⃣ Crear objetos
    usuario = Usuario(nombre, cedula)
    numero1 = Numero(valor1)
    numero2 = Numero(valor2)

    # 4️⃣ Crear calculadora
    operacion = Calculadora(numero1, numero2)

    #CONDICIONAL PARA ESCOGER EL TIPO DE OPERACION
    if tipo_de_operacion == "suma":
        resultado = operacion.suma()
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, resultado)

    elif tipo_de_operacion == "resta":
        resultado = operacion.resta()
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, resultado)
        

#CREAMOS LOS CAMPOS DE TOMA DE INFORMACION
tk.Label(ventana,text="Nombre").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Id").pack()
entry_cedula = tk.Entry(ventana)
entry_cedula.pack()

tk.Label(ventana, text="Numero 1").pack()
entry_numero1= tk.Entry(ventana)
entry_numero1.pack()

tk.Label(ventana,text="numero 2").pack()
entry_numero2 = tk.Entry(ventana)
entry_numero2.pack()

tk.Label(ventana,text="CALCULO TIPO DE OPERACION").pack()
entry_resultado = tk.Entry(ventana)
entry_resultado.pack()

#se utiliza para crear la tala, estoy llamando a tabla_texto del codigo calculadora.py
tabla_texto = tk.Text(ventana, height=10, width=40)
tabla_texto.pack()

# tk.Label(ventana,text="Resultado para RESTA").pack()
# entry_resta = tk.Entry(ventana)
# entry_resta.pack()


#Botones
tk.Button(ventana, text="Calcular Suma", command=lambda: calcular("suma"), bg="green", fg="white").pack(pady=5)

tk.Button(ventana, text="Calcular Resta", command=lambda: calcular("resta"), bg="blue", fg="white").pack(pady=5)

tk.Button(ventana, text="Mostrar Historial", command=mostrar_historial,bg="orange", fg="white").pack(pady=5)

tk.Button(ventana, text="Guardar en Historial",command=guardar_en_historial, bg="purple", fg="white").pack(pady=5)


ventana.mainloop()