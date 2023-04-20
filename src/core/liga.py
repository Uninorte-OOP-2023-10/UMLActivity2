from __future__ import annotations
from typing import List

from game.campeonato import Campeonato
from person.persona import Juez, Jugador

class LigaTenis:

    def __init__(self) -> None:
        self.__campeonatos: List["Campeonato"] = []
        self.__jueces: List["Juez"] = []
        self.__jugadores: List["Jugador"] = []

    def add_campeonato(self, campeonato: "Campeonato") -> bool:
        self.__campeonatos.append(campeonato)
        return True
    
    def add_juez(self, juez: "Juez") -> bool:
        self.__jueces.append(juez)
        return True
    
    def add_jugador(self, jugador: "Jugador") -> bool:
        self.__jugadores.append(jugador)
        return True
    
    def get_campeonato(self, index: int) -> "Campeonato":
        return self.__campeonatos[index]
    
    def get_juez(self, index: int) -> "Juez":
        return self.__jueces[index]
    
    def get_jugador(self, index: int) -> "Jugador":
        return self.__jugadores[index]
    
    def calc_sets_ganados_jugadores_campeonato(self, index: int) -> None:
        pass