from dispositivo_entrada import DispositivosDeEntrada
from monitor import Monitor


class Computadora(Monitor,DispositivosDeEntrada):

    contador_ID_computadora = 0

#contador de cantidad de computadoras 

    @classmethod
    def ID_computadora(cls):
        cls.contador_ID_computadora += 1
        return cls.contador_ID_computadora


    def __init__(self,nombre):
        Monitor.__init__(self)
        DispositivosDeEntrada.__init__(self)
        self.ID = Computadora.ID_computadora()
        self.nombre = nombre
    

    def __Str__():
        return f'computadora: [{self.nombre}]{Monitor.__str__()}{DispositivosDeEntrada.__str__()}'

if __name__ == '__main__':
# atributos de las clases padre Dispositivos de entrada y monitor

#    dispositivo1 = DispositivosDeEntrada('teclado','asus','USB')
#    dispositivo2 = DispositivosDeEntrada('mouse','RedDragon','Bluetooth')
#    monitor1 = Monitor('Samsung',"24'")

    Computadora1 = Computadora('compu1')
    print(Computadora1)