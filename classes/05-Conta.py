class Conta:

    def __init__(self, numero, nomeDoCorrentista, saldo=0.0):
        self.__numero = numero
        self.__nome = nomeDoCorrentista
        self.__saldo = saldo

    def alteraNome(self, novoNome):
        self.__nome = novoNome
    
    def deposito(self, valor):
        self.__saldo += valor
    
    def saque(self, valor):
        self.__saldo -= valor

    def get_saldo(self):
        return self.__saldo


#Teste
contaDoJoao = Conta(1, 'Joao')
assert contaDoJoao.get_saldo() == 0
contaDoJoao.deposito(50)
assert contaDoJoao.get_saldo() == 50
contaDoJoao.saque(10)
assert contaDoJoao.get_saldo() == 40
