import tkinter as tk
from tkinter import scrolledtext

class PruebaExcepcionesGUI:

    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Manejo de Excepciones")
        self.ventana.geometry("450x300")

        # Crear un widget de texto con scroll
        self.areaTexto = scrolledtext.ScrolledText(self.ventana, width=60, height=20)
        self.areaTexto.pack(padx=10, pady=10)

        # Botón para ejecutar el código
        boton = tk.Button(self.ventana, text="Ejecutar", command=self.main)
        boton.pack(pady=10)

    def escribir(self, mensaje: str):
        self.areaTexto.insert(tk.END, mensaje + "\n")
        self.areaTexto.see(tk.END)

    def main(self):
        self.areaTexto.delete("1.0", tk.END)  # Limpiar texto anterior

        # Primer bloque try donde se captura la excepción aritmética
        try:
            self.escribir("Ingresando al primer try")
            cociente = 10000 / 0
            self.escribir("Después de la división")  # Nunca se ejecuta
        except ArithmeticError as e:
            self.escribir("División por cero")
        finally:
            self.escribir("Ingresando al primer finalmente")

        # Segundo bloque try
        try:
            self.escribir("Ingresando al segundo try")
            objeto = [1,2,3,4,5]
            objeto.__float__()  # Esto lanza una excepción
            self.escribir("Imprimiendo objeto")  # Nunca se ejecuta
        except ArithmeticError:
            self.escribir("División por cero")
        except Exception as e:
            self.escribir("Ocurrió una excepción")
        finally:
            self.escribir("Ingresando al segundo finalmente")


# Código para ejecutar la ventana
if __name__ == "__main__":
    root = tk.Tk()
    app = PruebaExcepcionesGUI(root)
    root.mainloop()
