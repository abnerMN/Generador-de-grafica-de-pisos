from ListaPatron import ListaPatron as Patron
class ListaPisos:
    class NodoPiso:
        def __init__(self,nombre, fila,columna,precioVolteo,precioIntercambio,patrones):
            self.nombre=nombre
            self.fila=fila
            self.columna=columna
            self.precioVolteo=precioVolteo
            self.precioIntercambio=precioIntercambio
            self.listaPatron=patrones
            self.siguiente=None
    
    def __init__(self):
        self.cabeza = None
        self.cola=None
        self.tamaño=0
    
    def imprimirPisos (self):
        nodo_actual=self.cabeza
        while nodo_actual !=None:
            print("\nNombre: " + nodo_actual.nombre+
                "\nFilas: " + str(nodo_actual.fila) + " - Columnas: " +str(nodo_actual.columna)+'\n'+
                'Precio Volteo: ' +str(nodo_actual.precioVolteo) + 
                ' - Precio Intercambio: '+ str(nodo_actual.precioIntercambio)+'\n')
            print('**** Patrones ****')
            nodo_actual.listaPatron.imprimirPatron()
            nodo_actual=nodo_actual.siguiente
    
    def agregarPiso (self,nombre, fila,columna,precioVolteo,precioIntercambio,patrones):
        nuevo_nodo=self.NodoPiso(nombre,fila,columna,precioVolteo,precioIntercambio,patrones)
        if self.cabeza == None and self.cola ==None:
            self.cabeza=nuevo_nodo
            self.cola=nuevo_nodo
        else:
            self.cola.siguiente=nuevo_nodo
            self.cola = nuevo_nodo
        self.tamaño +=1
    



#list_patron=Patron()
#list_patron.agregarPatron('cod21','WBBBWBWWW')
#list_patron.agregarPatron('cod22','WWWWBWWWB')
#list_patron.agregarPatron('cod31”','WBBBB')
#list_patron.imprimirPatron()


#print('******* lista pisos *****')
#lista_pisos= ListaPisos()
#lista_pisos.agregarPiso('ejemplo02',3,3,1,1,list_patron)
#lista_pisos.imprimirPisos()


#lp.agregar('cod21','WBBBWBWWW')
#lp.agregar('cod22','WWWWBWWWB')
#lp.agregar('cod31”>','WBBBB')

#lp.agregar('ejemplo02',3,3,1,1)
#lp.agregar('ejemplo03',1,5,1000,1)

#lp.imprimirPisos()

