from NodoPiso import Piso

class Lista_Simple():
    def __init__(self):
        self.primero=None
        self.ultimo=None
        self.tamaño=0
    
    def agregar (self):
        nuevo_nodo = Piso(1,2,3,4)
        if self.primero is None:
            self.primero=nuevo_nodo
    
    def imprimir(self):
        
