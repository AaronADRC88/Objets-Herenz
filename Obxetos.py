__author__ = 'aferreiradominguez'


class Persoa:
    """Clase que definae unha persoa """

    def __init__(self, nome):
        self.nome = nome

    def sauda(self):
        print("Ola " + self.nome)


persona = Persoa("aaron")
persona.sauda()


class Oficio:
    """Clase que define oficio"""

    def __init__(self, oficio):
        self.oficio = oficio

    def mostraOfi(self):
        print("O oficio e: " + self.oficio)


class Traballador(Persoa, Oficio):
    """Herdanza multiple"""

    def __init__(self, nome, oficio, soldo):
        Persoa.__init__(self, nome)
        Oficio.__init__(self, oficio)
        self.soldo = soldo

    def mostraSoldo(self):
        print("O soldo e: " + str(self.soldo))

    # class Traballador(Persoa):
    """Herencia simple"""
    #   def __init__(self,nome,traballo):
    # super(Traballador,self).__init__(nome)
    """Otra opcion"""
    #      Persoa.__init__(self,nome)
    #     self.traballo=traballo


t = Traballador("Pepinho", "Canteiro", 1000)

t.sauda()
t.mostraOfi()
t.mostraSoldo()
