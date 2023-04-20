from __future__ import annotations
from abc import ABC
from typing import List

#from game.juego import Juego

class Persona(ABC):

    def __init__(self, nombre: str) -> None:
        self._nombre = nombre


class Juez(Persona):

    def __init__(self, nombre: str, edad: int) -> None:
        super().__init__(nombre)
        self.__edad = edad
        self.__juegos: List["Juego"] = []

    def add_juego(self, juego: "Juego") -> bool:
        self.__juegos.append(juego)
        return True


class Jugador(Persona):

    def __init__(self, nombre: str, sueldo: int) -> None:
        super().__init__(nombre)
        self.__sueldo = sueldo
        self.__juegos: List["Juego"] = []

    def add_juego(self, juego: "Juego") -> bool:
        self.__juegos.append(juego)
        return True