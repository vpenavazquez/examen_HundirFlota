class Nave:
    # Constantes de clase para devolver los estados tras un impacto
    TOCADO = 1
    HUNDIDO = 2

    def __init__(self, nombre, tipo, vida):
        # Constructor de la Nave.
        # Parámetros: nombre (str), tipo (str), vida (int)
        self.nombre = nombre
        self.tipo = tipo
        self.vida = vida
        self.hundido = False  # Al crearse, la nave está a flote

    def recibir_disparo(self):
        # Método para aplicar daño a la nave y calcular su estado vital.
        # No recibe parámetros (usa el estado de 'self').
        # Devuelve: constante TOCADO (1) o HUNDIDO (2).

        # 1. Si la nave ya estaba hundida antes del disparo, devolvemos el estado directamente
        if self.hundido:
            return self.HUNDIDO

        # 2. Si no estaba hundida, le restamos 1 punto de vida
        self.vida -= 1

        # 3. Comprobamos si la vida ha llegado a 0 tras este impacto
        if self.vida <= 0:
            self.vida = 0  # Evitamos que la vida sea un número negativo
            self.hundido = True  # Modificamos el estado a hundido
            print(f"{self.nombre} hundido")
            return self.HUNDIDO
        else:
            # Si le queda vida, simplemente está tocada
            print(f"{self.nombre} tocado. Vida restante: {self.vida}")
            return self.TOCADO