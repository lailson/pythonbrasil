class Quadrado:

    def __init__(self, lado):
        self.__lado = lado 

    def get_lado(self):
        return self.__lado
    
    def set_lado(self, novoLado):
        self.__lado = novoLado
    
    def area(self):
        return self.__lado * self.__lado

#teste
quadrado = Quadrado(3)
assert quadrado.get_lado() == 3
quadrado.set_lado(4)
assert quadrado.area() == 16

