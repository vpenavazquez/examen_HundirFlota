from Tablero import Tablero

class Juego:
    def __init__(self):
        self.tablero = Tablero()

    # Constructor que inicializa el controlador principal del juego
    # creando una instancia del Tablero.
    def mostrar_resultado(self, resultado):

        # Muestra por consola un mensaje al jugador según el número recibido.
        # Parámetros: resultado (int o None).

        if resultado == 0:
            print("Agua")
        elif resultado == 1:
            print("Tocado")
        elif resultado == 2:
            print("Hundido")
        elif resultado is None:
            print("Ya disparaste aquí")

    def lanzar_ataque(self):

        # Pide las coordenadas al jugador, se las pasa al tablero y muestra el resultado.
        # Parámetros: Ninguno. Devuelve: Nada.
        x = int(input("x: "))
        y = int(input("y: "))
        print(f"\nAtaque en ({x},{y})")

        resultado = self.tablero.comprobar_impacto(x, y)

        self.mostrar_resultado(resultado)

    def menu(self):

        # Bucle principal que mantiene viva la ejecución del juego interactivo.
        while True:
            print("\n=== MENÚ ===")
            print("1. Colocar barco")
            print("2. Atacar")
            print("3. Salir")

            opcion = input("Seleciona una oción: ")

            if opcion == "1":
                self.tablero.colocar_barco()

            elif opcion == "2":
                self.lanzar_ataque()

            elif opcion == "3":
                break

            else:
                print("Opción inválida")
# Punto de entrada de la aplicación
if __name__ == "__main__":
    juego = Juego()
    juego.menu()