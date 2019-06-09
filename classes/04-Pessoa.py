class Pessoa:

    def __init__(self, nome, idade, peso, altura):
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura

    def get_altura(self):
        return self.__altura

    def get_idade(self):
        return self.__idade

    def envelhecer(self):
        self.__idade+=1
        if self.__idade < 21 :
            self.__altura += 0.5
        
    
    def engordar(self, peso):
        self.__peso += peso

    def emagrecer(self, peso):
        self.__peso -= peso

    def crescer(self, altura):
        self.__altura += altura


#Teste
joao = Pessoa('joao', 19, 80, 180)
joao.envelhecer()
assert joao.get_idade() == 20
assert joao.get_altura() == 180.5