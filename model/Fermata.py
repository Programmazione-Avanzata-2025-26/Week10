from dataclasses import dataclass

@dataclass
class Fermata:
    _id_fermata : int
    _nome : str

    @property
    def id_fermata(self): #-> int
        return self._id_fermata

    @property
    def nome(self): # -> str
        return self._nome

    def __str__(self):
        return f"Fermata: {self._id_fermata} {self._nome}"

    def __hash__(self):
        return hash(self._id_fermata)