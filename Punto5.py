import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext

def leer_archivo_y_mostrar():
    nombre_archivo = "C:/Users/ADMIN/Desktop/d/prueba.txt"  
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            texto_area.delete("1.0", tk.END)
            texto_area.insert(tk.END, contenido)
    except FileNotFoundError:
        messagebox.showerror("Error", "El archivo 'prueba.txt' no fue encontrado en la ruta C:/.")
        texto_area.delete("1.0", tk.END)
    except IOError as e:
        messagebox.showerror("Error", f"No se pudo leer el archivo: {e}")
        texto_area.delete("1.0", tk.END)


ventana = tk.Tk()
ventana.title("Contenido del Archivo")
ventana.geometry("400x300")

etiqueta_titulo = tk.Label(ventana, text="Contenido del Archivo", font=("Arial", 14))
etiqueta_titulo.pack(pady=10)

texto_area = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, width=40, height=10, font=("Arial", 10))
texto_area.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

boton_ver_contenido = tk.Button(ventana, text="Ver Contenido", command=leer_archivo_y_mostrar, font=("Arial", 12))
boton_ver_contenido.pack(pady=10)

ventana.mainloop()