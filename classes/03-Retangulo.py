class Retangulo:

    def __init__(self, comprimento, largura):
        self.__comprimento = comprimento
        self.__largura = largura
    
    def alteraComprimento(self, novoComprimento):
        self.__comprimento = novoComprimento
    
    def retornaComprimento(self):
        return self.__comprimento
    
    def alteraLargura(self, novaLargura):
        self.__largura = novaLargura
    
    def retornaLargura(self):
        return self.__largura
    
    def area(self):
        return self.__largura * self.__comprimento
    
    def perimetro(self):
        return (self.__largura + self.__comprimento) * 2
    

retangulo = Retangulo(2,3)
assert retangulo.area() == 6
assert retangulo.perimetro() == 10
