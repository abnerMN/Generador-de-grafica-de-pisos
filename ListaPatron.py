class ListaPatron:
    class NodoPatron:
        def __init__(self, codigo, patron):
            self.codigo=codigo
            self.patron=patron
            self.siguiente=None
    
    def __init__(self):
        self.cabeza = None
        self.cola=None
        self.tamaño=0
    
    def imprimirPatron (self):
        nodo_actual=self.cabeza
        while nodo_actual !=None:
            print("\nCodigo: " + nodo_actual.codigo+
                "\nPatron: " + nodo_actual.patron+'\n')
            nodo_actual=nodo_actual.siguiente
    
    def agregar (self,codigo,patron):
        nuevo_nodo=self.NodoPatron(codigo,patron)
        if self.cabeza == None and self.cola ==None:
            self.cabeza=nuevo_nodo
            self.cola=nuevo_nodo
        else:
            self.cola.siguiente=nuevo_nodo
            self.cola = nuevo_nodo
        self.tamaño +=1


lp=ListaPatron()
lp.agregar('cod21','WBBBWBWWW')
lp.agregar('cod22','WWWWBWWWB')
lp.agregar('cod31”>','WBBBB')
lp.imprimirPatron()