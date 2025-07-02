import tkinter as tk
from tkinter import messagebox

class Vendedor:
    # Constructor de Vendedor
    def __init__(self, nombre, apellidos, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.verificar_edad(edad)  # Verifica la edad antes de asignar
        self.edad = edad

    # Método que verifica que la edad de un vendedor es apropiada
    def verificar_edad(self, edad):
        # ValueError es el equivalente a IllegalArgumentException
        # raise es el equivalente a throw
        if edad < 0 or edad > 120:
            raise ValueError("La edad no puede ser negativa ni mayor a 120.")
        if edad < 18:
            raise ValueError("El vendedor debe ser mayor de 18 años.")

    # Método que muestra los datos del vendedor
    def imprimir(self):
        return (f"Nombre del vendedor: {self.nombre}\n"
                f"Apellidos del vendedor: {self.apellidos}\n"
                f"Edad del vendedor: {self.edad}")

# Función que se ejecuta al presionar el botón
def procesar():
    try:
        nombre = entry_nombre.get()
        apellidos = entry_apellidos.get()
        edad = int(entry_edad.get())

        vendedor = Vendedor(nombre, apellidos, edad)
        messagebox.showinfo("Vendedor válido", vendedor.imprimir())

    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Ventana principal
ventana = tk.Tk()
ventana.title("Registro de Vendedor")
ventana.geometry("300x200")

# Nombres y entradas
tk.Label(ventana, text="Nombre:").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Apellidos:").pack()
entry_apellidos = tk.Entry(ventana)
entry_apellidos.pack()

tk.Label(ventana, text="Edad:").pack()
entry_edad = tk.Entry(ventana)
entry_edad.pack()

# Botón para procesar los datos
tk.Button(ventana, text="Registrar", command=procesar).pack(pady=10)

# Iniciar el bucle de la interfaz
ventana.mainloop()
