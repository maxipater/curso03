class Monitor:
    contador_ID_monitor=0

    @classmethod
    def ID_monitor(cls):
        cls.contador_ID_monitor += 1
        return cls.contador_ID_monitor

    def __init__(self,_marca1,_pulgadas):
         self.ID =Monitor.ID_monitor()
         self.marca = _marca1
         self.pulgadas = _pulgadas

#metodo get y set para el encapsulamiento de los los atributos privados (_marca y _pulgadas)

    @property
    def marca(self):  
        return self._marca1

    @marca.setter
    def marca(self, marca):
        self._marca1 = marca


    @property
    def pulgadas(self):  
        return self._pulgadas

    @pulgadas.setter
    def pulgadas(self, pulgadas):
        self._pulgadas = pulgadas



    def __str__(self):
        return f'\nMonitor [ID: {self.ID}] | Marca [{self.marca}] | Pulgadas [{self.pulgadas}]'

 #if __name__ == '__main__':

monitor1 = Monitor('samsung',"24'")
 #   monitor2 = Monitor('LG',"27'")
 #   print(monitor1,monitor2)