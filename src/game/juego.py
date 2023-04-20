from __future__ import annotations
from typing import List, Optional

from person.persona import Juez, Jugador

class Juego:

    def __init__(
        self,
        jugador_1: Optional["Jugador"] = None,
        jugador_2: Optional["Jugador"] = None,
        juez: Optional["Juez"] = None,
        juego_previo_1: Optional["Juego"] = None,
        juego_previo_2: Optional["Juego"] = None
    ) -> None:
        self.__jugador_1 = jugador_1
        self.__jugador_2 = jugador_2
        self.__juez = juez
        self.__juego_previo_1 = juego_previo_1
        self.__juego_previo_2 = juego_previo_2
        self.__juego_siguiente: Optional["Juego"] = None
        self.__sets: List["Set"] = []

        if not self.__juego_previo_1 is None:
            self.__jugador_1 = self.__juego_previo_1.get_winner()
            self.__juego_previo_1.set_juego_siguiente(self)

        if not self.__juego_previo_2 is None:
            self.__jugador_2 = self.__juego_previo_2.get_winner()
            self.__juego_previo_2.set_juego_siguiente(self)

        self.__jugador_1.add_juego(self)
        self.__jugador_2.add_juego(self)
        self.__juez.add_juego(self)

    def set_juego_siguiente(self, juego: "Juego") -> bool:
        self.__juego_siguiente = juego
        return True

    def add_sets(self, set_1: "Set", set_2: "Set", set_3: Optional["Set"] = None) -> bool:
        self.__sets.append(set_1)
        self.__sets.append(set_2)
        if not set_3 is None:
            self.__sets.append(set_3)
        return True
    
    def get_winner(self) -> Optional["Jugador"]:
        last_set = self.__sets[-1]
        if last_set.get_puntos_jugador_1() > last_set.get_puntos_jugador_2():
            return self.__jugador_1
        elif last_set.get_puntos_jugador_1() < last_set.get_puntos_jugador_2():
            return self.__jugador_2
        
        return None


class Set:

    def __init__(self, puntos_jugador_1: int, puntos_jugador_2: int) -> None:
        self.__puntos_jugador_1 = puntos_jugador_1
        self.__puntos_jugador_2 = puntos_jugador_2

    def get_puntos_jugador_1(self) -> int:
        return self.__puntos_jugador_1
    
    def get_puntos_jugador_2(self) -> int:
        return self.__puntos_jugador_2