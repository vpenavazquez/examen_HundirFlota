class Casilla:
    def __init__(self):
        # Inicializa la casilla vacía: sin nave asignada y sin haber sido atacada
        self.nave = None
        self.visitada = False

    def disparar(self):
        # Método para procesar un disparo en esta casilla.
        # No recibe parámetros (usa el estado de 'self').
        # Devuelve: None (si ya fue visitada), 0 (Agua), o 1/2 (Tocado/Hundido de la Nave).

        # 1. Comprobamos si la casilla ya fue disparada para no descontar vida a la nave dos veces
        if self.visitada:
            print("Ya disparaste aquí")
            return None

        # 2. Si es la primera vez, cambiamos su estado a visitada (hace de 'memoria' de la casilla)
        self.visitada = True

        # 3. Comprobamos si en esta casilla hay cargada una nave
        if self.nave is None:
            print("Agua")
            return 0

        # 4. Si hay nave, le pasamos el disparo para que gestione su propia vida
        return self.nave.recibir_disparo()