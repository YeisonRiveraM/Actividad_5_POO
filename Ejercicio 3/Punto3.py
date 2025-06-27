import tkinter as tk
from tkinter import messagebox
import math

class CalculosNumericosGUI:
    def __init__(self, master):
        self.master = master
        master.title("Cálculos Numéricos")
        master.geometry("400x300") # Tamaño inicial de la ventana

        # Etiqueta para la entrada de valor
        self.label_valor = tk.Label(master, text="Valor numérico:")
        self.label_valor.pack(pady=10)

        # Campo de entrada para el valor numérico
        self.entry_valor = tk.Entry(master)
        self.entry_valor.pack(pady=5)
        self.entry_valor.focus_set() # Pone el foco en el campo de entrada al iniciar

        # Botón para calcular
        self.btn_calcular = tk.Button(master, text="Calcular", command=self.realizar_calculos)
        self.btn_calcular.pack(pady=10)

        # Etiqueta para mostrar el resultado del logaritmo
        self.label_resultado_log = tk.Label(master, text="Logaritmo Neperiano: ")
        self.label_resultado_log.pack(pady=5)

        # Etiqueta para mostrar el resultado de la raíz cuadrada
        self.label_resultado_raiz = tk.Label(master, text="Raíz Cuadrada: ")
        self.label_resultado_raiz.pack(pady=5)

        # Etiqueta para mostrar mensajes de error o validación
        self.label_error = tk.Label(master, text="", fg="red")
        self.label_error.pack(pady=5)

    def realizar_calculos(self):
        """
        Método que se ejecuta al presionar el botón 'Calcular'.
        Obtiene el valor de la entrada, realiza los cálculos y muestra los resultados o errores.
        """
        self.label_error.config(text="") # Limpia mensajes de error previos
        self.label_resultado_log.config(text="Logaritmo Neperiano: ")
        self.label_resultado_raiz.config(text="Raíz Cuadrada: ")

        valor_str = self.entry_valor.get()

        try:
            valor = float(valor_str)
        except ValueError:
            self.label_error.config(text="Error: El valor debe ser numérico.")
            return

        # Calcular Logaritmo Neperiano
        try:
            if valor < 0:
                raise ValueError("El valor para el logaritmo debe ser positivo.")
            resultado_log = math.log(valor)
            self.label_resultado_log.config(text=f"Logaritmo Neperiano: {resultado_log:.4f}")
        except ValueError as e:
            self.label_resultado_log.config(text="Logaritmo Neperiano: " + str(e), fg="red")
        except Exception as e:
            self.label_resultado_log.config(text=f"Logaritmo Neperiano: Error inesperado ({e})", fg="red")

        # Calcular Raíz Cuadrada
        try:
            if valor < 0:
                raise ValueError("El valor para la raíz cuadrada debe ser positivo.")
            resultado_raiz = math.sqrt(valor)
            self.label_resultado_raiz.config(text=f"Raíz Cuadrada: {resultado_raiz:.4f}")
        except ValueError as e:
            self.label_resultado_raiz.config(text="Raíz Cuadrada: " + str(e), fg="red")
        except Exception as e:
            self.label_resultado_raiz.config(text=f"Raíz Cuadrada: Error inesperado ({e})", fg="red")

# Crear la ventana principal y ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculosNumericosGUI(root)
    root.mainloop()
