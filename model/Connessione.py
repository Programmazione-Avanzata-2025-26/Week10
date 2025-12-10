from dataclasses import dataclass


@dataclass
class Connessione:
    _id_connessione : int
    _id_linea : int
    _id_stazP : int
    _id_stazA : int

    @property
    def id_connessione(self) -> int:
        return self._id_connessione

    @property
    def id_linea(self) -> int:
        return self._id_linea

    @property
    def id_stazP(self) -> int:
        return self._id_stazP

    @property
    def id_stazA(self) -> int:
        return self._id_stazA

    def __str__(self):
        return f"{self._id_connessione}"

