class Mouse:
#atributo de clase para contador 
    contador_ID_mouse=0
    
    @classmethod
    def ID_mouse(cls):
        cls.contador_ID_mouse += 1
        return cls.contador_ID_mouse

    def __init__(self,tipo):
        if tipo == 'mouse':
            self.ID =Mouse.ID_mouse()
            self.entrada = tipo
        else:
            return

    def __str__(self) :
        return f'Mouse [ID:{self.ID}]'
    
