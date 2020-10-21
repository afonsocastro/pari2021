class Objeto:
    def __init__(self, volume, area, cor, peso):
        self.volume=volume
        self.area=area
        self.cor=cor
        self.peso=peso
        self.proprietarios= []

    def addProp (self, nome):
        self.proprietarios.append(nome)

    def remProp(self, nome):
        if nome in self.proprietarios:
            #print "o nome existe"
            self.proprietarios.remove(nome)
        else:
            print "erro: o nome inserido nao existe"



    def __str__(self):
        string=""
        for i in self.proprietarios:
             if i == self.proprietarios[-1]:
                string += "Eu sou um vaso. A minha cor: " + i
             else:
                string +="Eu sou um vaso. A minha cor: " + i + " \n"

        return string

