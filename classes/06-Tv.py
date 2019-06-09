class Tv:

    def __init__(self, volume, canal, limiteVolume=100, limiteCanal=30):
        self.__volume = volume
        self.__canal = canal 
        self.__limiteVolume = limiteVolume
        self.__limiteCanal = limiteCanal

    def get_volume(self):
        return self.__volume

    def get_canal(self):
        return self.__canal

    def aumentaVolume(self):
        if self.__volume + 1 < self.__limiteVolume:
            self.__volume += 1
    
    def diminuiVolume(self):
        if self.__volume -1 > 0:
            self.__volume -= 1
        
    def set_canal(self, canal):
        if (canal >= 0) and (canal <= self.__limiteCanal):
            self.__canal = canal
    
    def aumentaCanal(self):
        if self.__canal + 1 < self.__limiteCanal:
            self.__canal += 1
    
    def diminuiCanal(self):
        if self.__canal - 1 > 0:
            self.__canal -= 1
    
    
        
#Teste
smartTv = Tv(30, 4)
smartTv.aumentaVolume()
smartTv.aumentaCanal()
assert smartTv.get_volume() == 31
assert smartTv.get_canal() == 5
smartTv.set_canal(7)
assert smartTv.get_canal() == 7


    