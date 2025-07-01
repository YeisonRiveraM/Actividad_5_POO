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
        self.programadores = [None] * 3  # máximo 3 programadores

    def esta_lleno(self) -> bool:
        return self.tamaño_equipo == len(self.programadores)

    def añadir(self, programador: Programador):
        if self.esta_lleno():
            raise Exception("El equipo está completo. No se pudo agregar programador.")
        self.programadores[self.tamaño_equipo] = programador
        self.tamaño_equipo += 1

    @staticmethod
    def validar_campo(campo: str):
        if any(c.isdigit() for c in campo):
            raise Exception("El nombre no puede tener dígitos.")
        if len(campo) > 20:
            raise Exception("La longitud no debe ser superior a 20 caracteres.")


def main():
    print("Nombre del equipo:")
    nombre_equipo = input()

    print("Universidad:")
    universidad = input()

    print("Lenguaje de programación:")
    lenguaje = input()

    equipo = EquipoMaratonProgramacion(nombre_equipo, universidad, lenguaje)

    print("\nDatos de los integrantes del equipo:")
    for i in range(3):
        try:
            print(f"\nIntegrante #{i + 1}")
            nombre = input("Nombre del integrante: ")
            EquipoMaratonProgramacion.validar_campo(nombre)

            apellidos = input("Apellidos del integrante: ")
            EquipoMaratonProgramacion.validar_campo(apellidos)

            programador = Programador(nombre, apellidos)
            equipo.añadir(programador)

        except Exception as e:
            print("Error:", e)
            break


if __name__ == "__main__":
    main()
