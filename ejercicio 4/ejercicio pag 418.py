import tkinter as tk
from tkinter import messagebox


class Programador:
    def __init__(self, nombre: str, apellidos: str):
        self.nombre = nombre
        self.apellidos = apellidos


class EquipoMaratonProgramacion:
    def __init__(self, nombre_equipo: str, universidad: str, lenguaje_programacion: str):
        self.nombre_equipo = nombre_equipo
        self.universidad = universidad
        self.lenguaje_programacion = lenguaje_programacion
        self.tamaño_equipo = 0
        self.programadores = [None] * 3

    def esta_lleno(self) -> bool:
        return self.tamaño_equipo == len(self.programadores)

    def añadir(self, programador: Programador):
        if self.esta_lleno():
            raise Exception("El equipo está completo. No se puede agregar más programadores.")
        self.programadores[self.tamaño_equipo] = programador
        self.tamaño_equipo += 1

    @staticmethod
    def validar_campo(campo: str):
        if any(c.isdigit() for c in campo):
            raise Exception("El nombre no puede tener dígitos.")
        if len(campo) > 20:
            raise Exception("La longitud no debe ser superior a 20 caracteres.")


class Aplicacion:
    def __init__(self, master):
        self.master = master
        master.title("Equipo Maratón de Programación")
        master.geometry("400x350")

        self.equipo = None

        # Entrada datos del equipo
        tk.Label(master, text="Nombre del equipo").pack()
        self.entry_nombre_equipo = tk.Entry(master)
        self.entry_nombre_equipo.pack()

        tk.Label(master, text="Universidad").pack()
        self.entry_universidad = tk.Entry(master)
        self.entry_universidad.pack()

        tk.Label(master, text="Lenguaje de programación").pack()
        self.entry_lenguaje = tk.Entry(master)
        self.entry_lenguaje.pack()

        tk.Button(master, text="Crear equipo", command=self.crear_equipo).pack(pady=5)

        # Entrada datos del programador
        tk.Label(master, text="Nombre del programador").pack()
        self.entry_nombre_programador = tk.Entry(master)
        self.entry_nombre_programador.pack()

        tk.Label(master, text="Apellidos del programador").pack()
        self.entry_apellidos_programador = tk.Entry(master)
        self.entry_apellidos_programador.pack()

        tk.Button(master, text="Añadir programador", command=self.agregar_programador).pack(pady=10)

        self.label_estado = tk.Label(master, text="", fg="blue")
        self.label_estado.pack()

    def crear_equipo(self):
        try:
            nombre = self.entry_nombre_equipo.get()
            universidad = self.entry_universidad.get()
            lenguaje = self.entry_lenguaje.get()

            EquipoMaratonProgramacion.validar_campo(nombre)
            EquipoMaratonProgramacion.validar_campo(universidad)
            EquipoMaratonProgramacion.validar_campo(lenguaje)

            self.equipo = EquipoMaratonProgramacion(nombre, universidad, lenguaje)
            self.label_estado.config(text="Equipo creado correctamente.", fg="green")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def agregar_programador(self):
        if not self.equipo:
            messagebox.showwarning("Atención", "Primero crea el equipo.")
            return

        try:
            nombre = self.entry_nombre_programador.get()
            apellidos = self.entry_apellidos_programador.get()

            EquipoMaratonProgramacion.validar_campo(nombre)
            EquipoMaratonProgramacion.validar_campo(apellidos)

            programador = Programador(nombre, apellidos)
            self.equipo.añadir(programador)

            self.label_estado.config(text=f"Programador añadido ({self.equipo.tamaño_equipo}/3).", fg="blue")

            if self.equipo.esta_lleno():
                messagebox.showinfo("Completo", "¡El equipo ya está completo!")
        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()
