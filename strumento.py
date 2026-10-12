class Strumento:
    def __init__(self, id_strumento, tipo, marca, anno_acquisto, valore):
        self.__id_strumento = id_strumento
        self.__tipo = tipo
        self.__marca = marca
        self.__anno_acquisto = anno_acquisto
        self.__valore = valore

    # Getter

    @property
    def id_strumento(self):
        return self.__id_strumento

    @property
    def tipo(self):
        return self.__tipo

    @property
    def marca(self):
        return self.__marca




    @property
    def anno_acquisto(self):
        return self.__anno_acquisto

    @property
    def valore(self):
        return self.__valore

    def __str__(self):
        return f"{self.__id_strumento} - {self.__tipo} {self.__marca} (acquistato nel {self.__anno_acquisto}, valore: {self.__valore:.2f} €)"
