class Teclado:
#atributo de clase para un contador

    contador_ID_teclado=0
    
    @classmethod
    def ID_teclado(cls):
        cls.contador_ID_teclado += 1
        return cls.contador_ID_teclado

    def __init__(self,tipo):
        if tipo == 'teclado':
            self.ID_tec =Teclado.ID_teclado()
            self.entrada = tipo
        else:
            return 


    def __str__(self) :
        return f'Teclado [ID:{self.ID_tec}]'
    
