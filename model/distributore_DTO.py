from dataclasses import dataclass
from database.prezzo_DAO import PrezzoDAO

'''
    DTO (Data Transfer Object) dell'entità Distributore
'''

@dataclass()
class Distributore:
    id: int
    nome: str
    indirizzo: str

    # RELAZIONI
    lista_prezzi: list = None

    #Ricostrusico all'interno del programma la relazione tra la tabella dei distributori
    #e quella dei prezzi presente nel database tramite la chiave esterna id_distributore.
    #Associo a ogni distributore i propri prezzi

    def get_prezzi(self):
        """ Aggiorna e Restituisce la lista di prezzi (self.lista_prezzi) associati al distributore"""
        lista_prezzi = PrezzoDAO.get_prezzi(self.id)

        if lista_prezzi is None:
            return []

        self.lista_prezzi = lista_prezzi

        return self.lista_prezzi


    def __eq__(self, other):
        return isinstance(other, Distributore) and self.id == other.id

    def __str__(self):
        return f"{self.id} | {self.nome} | Indirizzo: {self.indirizzo}"

    def __repr__(self):
        return f"{self.id} | {self.nome} | Indirizzo: {self.indirizzo}"
