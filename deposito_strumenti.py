import csv
from operator import attrgetter

from strumento import Strumento
from prestito import Prestito

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.__nome = nome
        self.__responsabile = responsabile

        self.__strumenti = {} # dizionario id_strumento -> Strumento
        self.__prestiti = {}
        self.__ultimo_id_strumento = 0
        self.__ultimo_id_prestito = 0

    @property
    def nome(self):
        return self.__nome

    @property
    def responsabile(self):
        return self.__responsabile

    @responsabile.setter
    def responsabile(self, nuovo_responsabile):
        self.__responsabile = nuovo_responsabile


    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        with open(file_path, "r", encoding="utf-8") as in_file:
            reader = csv.DictReader(in_file, fieldnames=['id', 'tipo', 'marca', 'anno', 'valore'])
            for riga in reader:
                id_strumento = riga['id']
                strumento = Strumento(
                    id_strumento,
                    riga['tipo'],
                    riga['marca'],
                    int(riga['anno']),
                    float(riga['valore'])
                )
                self.__strumenti[id_strumento] = strumento
                self.__ultimo_id_strumento = int(id_strumento[1:]) # Per tenere traccia dell'ultimo ID

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        self.__ultimo_id_strumento += 1
        id_strumento = f"S{self.__ultimo_id_strumento}"
        nuovo_strumento = Strumento(id_strumento, tipo, marca, anno_acquisto, valore)
        self.__strumenti[id_strumento] = nuovo_strumento

        return nuovo_strumento

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        return sorted(self.__strumenti.values(), key=attrgetter("marca"))

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        if id_strumento not in self.__strumenti:
            raise Exception(f"Errore, strumento {id_strumento} non presente")

        # Controllare se strumento già in prestito
        for prestito in self.__prestiti.values():
            if prestito.id_strumento == id_strumento:
                raise Exception(f"Errore, strumento {id_strumento} già in prestito")

        self.__ultimo_id_prestito += 1
        id_prestito = f'P{self.__ultimo_id_prestito}'
        prestito = Prestito(id_prestito, data, id_strumento, cognome_allievo)
        self.__prestiti[id_prestito] = prestito
        return prestito

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        if id_prestito not in self.__prestiti:
            raise Exception(f"Errore, prestito {id_prestito} non presente")

        del self.__prestiti[id_prestito]