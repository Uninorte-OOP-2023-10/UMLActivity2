from __future__ import annotations

from core.liga import LigaTenis
from game.campeonato import Campeonato
from game.juego import Juego, Set
from person.persona import Juez, Jugador

def main() -> None:
    liga = LigaTenis()

    liga.add_juez(Juez('Pedro Perez', 35))
    liga.add_juez(Juez('Alejandro Fernandez', 29))
    liga.add_juez(Juez('Mercedez', 54))

    liga.add_jugador(Jugador('Rafael Nadal', 1250))
    liga.add_jugador(Jugador('Martina Hingis', 980))
    liga.add_jugador(Jugador('Roger Federer', 1420))
    liga.add_jugador(Jugador('Monica Seles', 1120))
    liga.add_jugador(Jugador('Novak Djokovic', 1030))
    liga.add_jugador(Jugador('Venus Williams', 1390))
    liga.add_jugador(Jugador('Andre Agassi', 940))
    liga.add_jugador(Jugador('Martina Navratilova', 1080))

    liga.add_campeonato(Campeonato())

    # Todos los juegos de la primera ronda se crean en este punto
    for i in range(0, 8, 2):
        liga.get_campeonato(0).add_juego(Juego(
            jugador_1 = liga.get_jugador(i), 
            jugador_2 = liga.get_jugador(i + 1),
            juez = liga.get_juez((i // 2) % 2)
        ))

    liga.get_campeonato(0).get_juego(0).add_sets(Set(6, 4), Set(1, 6), Set(6, 3))
    liga.get_campeonato(0).get_juego(1).add_sets(Set(6, 1), Set(5, 7), Set(3, 6))
    liga.get_campeonato(0).get_juego(2).add_sets(Set(1, 6), Set(4, 6))
    liga.get_campeonato(0).get_juego(3).add_sets(Set(6, 2), Set(6, 0))

    # Semifinal
    for i in range(0, 4, 2):
        liga.get_campeonato(0).add_juego(Juego(
            juego_previo_1 = liga.get_campeonato(0).get_juego(i),
            juego_previo_2 = liga.get_campeonato(0).get_juego(i + 1),
            juez = liga.get_juez((i // 2) % 2)
        ))

    liga.get_campeonato(0).get_juego(4).add_sets(Set(6, 4), Set(4, 6), Set(3, 6))
    liga.get_campeonato(0).get_juego(5).add_sets(Set(7, 5), Set(2, 6), Set(1, 6))

    # Final
    liga.get_campeonato(0).add_juego(Juego(
        juego_previo_1 = liga.get_campeonato(0).get_juego(4),
        juego_previo_2 = liga.get_campeonato(0).get_juego(5),
        juez = liga.get_juez(0)
    ))

    liga.get_campeonato(0).get_juego(6).add_sets(Set(6, 2), Set(3, 6), Set(7, 9))

    liga.get_campeonato(0).show_resumen()
    liga.calc_sets_ganados_jugadores_campeonato(0)


if __name__ == '__main__':
    main()


"""
-------------- Resultados --------------
Jugador 1: Rafael Nadal
Jugador 2: Martina Hingis
Juez: Pedro Perez
Set 1: 6 - 4
Set 2: 1 - 6
Set 3: 6 - 3
Ganador: Rafael Nadal

Jugador 1: Roger Federer
Jugador 2: Monica Seles
Juez: Alejandro Fernandez
Set 1: 6 - 1
Set 2: 5 - 7
Set 3: 3 - 6
Ganador: Monica Seles

Jugador 1: Novak Djokovic
Jugador 2: Venus Williams
Juez: Pedro Perez
Set 1: 1 - 6
Set 2: 4 - 6
Ganador: Venus Williams

Jugador 1: Andre Agassi
Jugador 2: Martina Navratilova
Juez: Alejandro Fernandez
Set 1: 6 - 2
Set 2: 6 - 0
Ganador: Andre Agassi

Jugador 1: Rafael Nadal
Jugador 2: Monica Seles
Juez: Pedro Perez
Set 1: 6 - 4
Set 2: 4 - 6
Set 3: 3 - 6
Ganador: Monica Seles

Jugador 1: Venus Williams
Jugador 2: Andre Agassi
Juez: Alejandro Fernandez
Set 1: 7 - 5
Set 2: 2 - 6
Set 3: 1 - 6
Ganador: Andre Agassi

Jugador 1: Monica Seles
Jugador 2: Andre Agassi
Juez: Pedro Perez
Set 1: 6 - 2
Set 2: 3 - 6
Set 3: 7 - 9
Ganador: Andre Agassi

El ganador del campeonato es: Andre Agassi

El jugador: Rafael Nadal gano 3 sets en el campeonato
El jugador: Martina Hingis gano 1 sets en el campeonato
El jugador: Roger Federer gano 1 sets en el campeonato
El jugador: Monica Seles gano 5 sets en el campeonato
El jugador: Novak Djokovic gano 0 sets en el campeonato
El jugador: Venus Williams gano 3 sets en el campeonato
El jugador: Andre Agassi gano 6 sets en el campeonato
El jugador: Martina Navratilova gano 0 sets en el campeonato
"""