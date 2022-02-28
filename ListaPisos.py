from ListaPatron import ListaPatron

class ListaPisos:
    class NodoPiso:
        def __init__(self,nombre, fila,columna,precioVolteo,precioIntercambio):
            self.nombre=nombre
            self.fila=fila
            self.columna=columna
            self.precioVolteo=precioVolteo
            self.precioIntercambio=precioIntercambio
            self.patrones=ListaPatron()
            self.siguiente=None
    
    def __init__(self):
        self.cabeza = None
        self.cola=None
        self.tamaño=0
    
    def imprimirPatron (self):
        nodo_actual=self.cabeza
        while nodo_actual !=None:
            print("\nNombre: " + nodo_actual.nombre+
                "\nFilas: " + str(nodo_actual.fila) + " - Columnas: " +str(nodo_actual.columna)+'\n'+
                'Precio Volteo: ' +str(nodo_actual.precioVolteo) + 
                ' - Precio Intercambio: '+ str(nodo_actual.precioIntercambio))
            nodo_actual=nodo_actual.siguiente
    
    def agregar (self,nombre, fila,columna,precioVolteo,precioIntercambio):
        nuevo_nodo=self.NodoPiso(nombre,fila,columna,precioVolteo,precioIntercambio)
        if self.cabeza == None and self.cola ==None:
            self.cabeza=nuevo_nodo
            self.cola=nuevo_nodo
        else:
            self.cola.siguiente=nuevo_nodo
            self.cola = nuevo_nodo
        self.tamaño +=1
    
    
        

lp = ListaPisos()
lp.agregar('ejemplo01',2,4,1,1)
lp.agregar('ejemplo02',3,3,1,1)
lp.agregar('ejemplo03',1,5,1000,1)
lp.imprimirPatron()

