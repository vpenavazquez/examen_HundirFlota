# Examen COD: Hundir la Flota

Este repositorio contiene la resolución de la prueba de evaluación para el juego "Hundir la Flota" en Python. 

El objetivo principal de esta versión es aplicar los principios de la **Programación Orientada a Objetos (POO)** para solucionar el problema de los "disparos repetidos", implementando una memoria en el tablero a través de la clase `Casilla`.

## Arquitectura del Proyecto

El juego está dividido en 4 clases principales, cada una con una responsabilidad única:

* **`Nave.py`**: Representa un barco. Conoce su nombre, tipo, puntos de vida y si está a flote o hundido.
* **`Casilla.py`**: Representa una coordenada en el tablero. Sabe si ya ha sido `visitada` (bombardeada) y si contiene una `Nave`. Evita que se reste vida a un barco si se dispara dos veces al mismo sitio.
* **`Tablero.py`**: Contiene una matriz de 10x10 de objetos `Casilla`. Se encarga de instanciar las naves y colocarlas en sus posiciones iniciales.
* **`Juego.py`**: Es el controlador principal. Contiene el menú interactivo, pide las coordenadas al jugador por consola y muestra los resultados en pantalla.

## Ejemplo 1: Disparo al agua

=== MENÚ ===
1. Colocar barco
2. Atacar
3. Salir
Seleciona una oción: 2
x: 0
y: 0

Ataque en (0,0)
Impacto en (0,0)
Agua

## Ejemplo 2: Impacto y hundido

Seleciona una oción: 2
x: 4
y: 6

Ataque en (4,6)
Impacto en (4,6)
U-47 hundido
Hundido

## Ejemplo 3: Memoria de casilla (Prevencion de bugs)

Seleciona una oción: 2
x: 4
y: 6

Ataque en (4,6)
Impacto en (4,6)
Ya disparaste aquí