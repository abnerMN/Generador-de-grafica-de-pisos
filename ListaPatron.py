class ListaPatron:
    class NodoPatron:
        def __init__(self, codigo, patron):
            self.codigo=codigo
            self.patron=patron
            self.siguiente=None
        
        def getCodigo(self):
            return self.codigo
        
        def getPatron(self):
            return self.patron
        
        def impresionNodoPatron(self):
            print("Codigo: " + str(self.codigo)+
            "\nPatron: " +str(self.patron)
            )
    
    def __init__(self):
        self.cabeza = None
        self.cola=None
        self.tamaño=0
    
    def imprimirPatron (self):
        nodo_actual=self.cabeza
        while nodo_actual !=None:
            nodo_actual.impresionNodoPatron()
            #print("\nCodigo: " + nodo_actual.codigo+
            #    "\nPatron: " + nodo_actual.patron+'\n')
            nodo_actual=nodo_actual.siguiente
    
    def agregarPatron (self,codigo,patron,r,c):
        nuevo_nodo=self.NodoPatron(codigo,patron)
        if self.cabeza == None and self.cola ==None:
            self.cabeza=nuevo_nodo
            self.cola=nuevo_nodo
            self.tamaño +=1
        else:
            total = int(r)*int(c)
            if len(patron)==total:
                self.cola.siguiente=nuevo_nodo
                self.cola = nuevo_nodo
                self.tamaño +=1
            else:
                pass
    
    def buscarPatron(self,codigo):
        actual = self.cabeza
        respuesta=None
        while(actual!=None):
            if actual.getCodigo() == codigo:
                respuesta= actual
                break
            else:
                actual = actual.siguiente
        
        return respuesta


#lp.agregar('cod21','WBBBWBWWW')
#lp.agregar('cod22','WWWWBWWWB')
#lp.agregar('cod31”>','WBBBB')
