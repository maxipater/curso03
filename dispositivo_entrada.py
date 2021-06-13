from teclado import Teclado
from mouse import Mouse


class DispositivosDeEntrada(Mouse,Teclado):
    def __init__(self,tipo,_marca,_conector):
        Teclado.__init__(self,tipo)
        Mouse.__init__(self,tipo)

# atributos de instacia
        self.marca = _marca
        self.conector = _conector
        self.tipo= tipo

# metodos get y set para el encapsulamiento de los atributos privados de la clase(_marca y _conector)
    @property
    def marca(self):  
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca


    @property
    def conector(self):  
        return self._conector

    @conector.setter
    def conector(self, conector):
        self._conector = conector

#metodo str con un condicional para imprimir mouse o teclado

    def __str__(self):
        if self.tipo == "mouse":
            x=Mouse
        else:
            x=Teclado
        return f'\n{x.__str__(self)} | Marca [{self.marca}] | Tipo [{self.conector}]'


 #if __name__ == '__main__':

dispositivo1 = DispositivosDeEntrada('mouse','asus','USB')
 #   dispositivo2 = DispositivosDeEntrada('mouse','logitec','bluetooth')
 #   dispositivo3 = DispositivosDeEntrada('teclado','HDC','USB')
 #   print( dispositivo1 ,dispositivo2,dispositivo3)