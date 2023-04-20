from __future__ import annotations
from typing import List

from game.juego import Juego

class Campeonato:

    def __init__(self) -> None:
        self.__juegos: List["Juego"] = []

    def add_juego(self, juego: "Juego") -> bool:
        self.__juegos.append(juego)
        return True
    
    def get_juego(self, index: int) -> "Juego":
        return self.__juegos[index]

    def show_resumen(self) -> None:
        pass