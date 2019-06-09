# Crie uma classe bola que modele uma bola:
class Bola:
    def __init__(self, cor, circunferencia, material):
        self.__cor = cor
        self.__circunferencia = circunferencia
        self.__material = material
    
    def trocaCor(self, novaCor):
        self.__cor = novaCor
    
    def mostraCor(self):
        return self.__cor


#Test
bola1 = Bola('Azul', 2, 'plastico')
assert bola1.mostraCor() == 'Azul'
bola1.trocaCor('branca')
assert bola1.mostraCor() == 'branca'

