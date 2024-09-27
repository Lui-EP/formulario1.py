import tkinter as tk
from tkinter import messagebox
import re
import csv

def limpiar_campos():
    entradaNombre.delete(0, tk.END)
    entradaApellido.delete(0, tk.END)
    entradaTelefono.delete(0, tk.END)
    entradaEdad.delete(0, tk.END)
    entradaAltura.delete(0, tk.END)
    var_sexo.set(0)  

def registrar_datos():
    nombre = entradaNombre.get()
    apellido = entradaApellido.get()
    telefono = entradaTelefono.get()
    edad = entradaEdad.get()
    altura = entradaAltura.get()

    if not validar_texto(nombre):
        messagebox.showerror("Error", "Nombre inválido")
        return
    if not validar_texto(apellido):
        messagebox.showerror("Error", "Apellido inválido")
        return
    if not validar_telefono(telefono):
        messagebox.showerror("Error", "Teléfono inválido")
        return
    if not validar_edad(edad):
        messagebox.showerror("Error", "Edad inválida")
        return
    if not validar_altura(altura):
        messagebox.showerror("Error", "Altura inválida (en metros)")
        return

    sexo = "No especificado"
    if var_sexo.get() == 1:
        sexo = "Masculino"
    elif var_sexo.get() == 2:
        sexo = "Femenino"

    # Guardar datos en un archivo CSV
    nombre_archivo = "Datos_Registro.csv"
    with open(nombre_archivo, mode="a", newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow([nombre, apellido, telefono, altura, edad, sexo])

    messagebox.showinfo("Éxito", "Datos guardados correctamente.")

def validar_telefono(valor):
    return valor.isdigit() and len(valor) == 10

def validar_texto(valor):
    return bool(re.match("^[a-zA-Z\s]+$", valor))

def validar_altura(valor):
    try:
        return 0.5 <= float(valor) <= 2.5
    except ValueError:
        return False

def validar_edad(valor):
    return valor.isdigit() and 1 <= int(valor) <= 120 

ventana = tk.Tk()
ventana.geometry("520x500")
ventana.title("Formulario de Registro")

var_sexo = tk.IntVar()

lblNombre = tk.Label(ventana, text="Nombre: ")
lblNombre.pack()
entradaNombre = tk.Entry(ventana)
entradaNombre.pack()

lblApellido = tk.Label(ventana, text="Apellido: ")
lblApellido.pack()
entradaApellido = tk.Entry(ventana)
entradaApellido.pack()

lblTelefono = tk.Label(ventana, text="Teléfono: ")
lblTelefono.pack()
entradaTelefono = tk.Entry(ventana)
entradaTelefono.pack()

lblEdad = tk.Label(ventana, text="Edad: ")
lblEdad.pack()
entradaEdad = tk.Entry(ventana)
entradaEdad.pack()

lblAltura = tk.Label(ventana, text="Altura: ")
lblAltura.pack()
entradaAltura = tk.Entry(ventana)
entradaAltura.pack()

lblSexo = tk.Label(ventana, text="Sexo:")
lblSexo.pack()

rbMasculino = tk.Radiobutton(ventana, text="Masculino", variable=var_sexo, value=1)
rbMasculino.pack()

rbFemenino = tk.Radiobutton(ventana, text="Femenino", variable=var_sexo, value=2)
rbFemenino.pack()

btnLimpiar = tk.Button(ventana, text="Limpiar campos", command=limpiar_campos)
btnLimpiar.pack()

btnRegistrar = tk.Button(ventana, text="Registrar", command=registrar_datos)
btnRegistrar.pack()

ventana.mainloop()