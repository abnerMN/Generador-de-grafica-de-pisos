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
        
        def getNombre(self):
            return self.nombre

        def getFila(self):
            return self.fila
        
        def getColumna(self):
            return self.columna
        
        def getPrecioVolteo(self):
            return self.precioVolteo
        
        def getPrecioIntercambio(self):
            return self.precioIntercambio
        
        def getListaPatron(self):
            return self.listaPatron
        
        def impresionPiso (self):
            print("\nnombre: " + str(self.nombre) + "\nfila: " + str(self.fila)+
            "\ncolumna: " + str(self.columna) +"\nprecio volteo: " +str(self.precioVolteo)+
            "\nprecio Intercambio: " + str(self.precioIntercambio) +"\n**** Patrones ****")
            self.listaPatron.imprimirPatron()

    def __init__(self):
        self.cabeza = None
        self.cola=None
        self.tamaño=0
    
    def imprimirPisos (self):
        nodo_actual=self.cabeza
        while nodo_actual !=None:
            nodo_actual.impresionPiso()
            nodo_actual=nodo_actual.siguiente
           # print("\nNombre: " + nodo_actual.nombre+
           #     "\nFilas: " + str(nodo_actual.fila) + " - Columnas: " +str(nodo_actual.columna)+'\n'+
           #     'Precio Volteo: ' +str(nodo_actual.precioVolteo) + 
           #     ' - Precio Intercambio: '+ str(nodo_actual.precioIntercambio)+'\n')
           # print('**** Patrones ****')
           # nodo_actual.listaPatron.imprimirPatron()
           # nodo_actual=nodo_actual.siguiente
    
    def agregarPiso (self,nombre, fila,columna,precioVolteo,precioIntercambio,patrones):
        nuevo_nodo=self.NodoPiso(nombre,fila,columna,precioVolteo,precioIntercambio,patrones)
        if self.cabeza == None and self.cola ==None:
            self.cabeza=nuevo_nodo
            self.cola=nuevo_nodo
            self.tamaño +=1
        else:
            res=self.buscarPiso(nombre)
            if res == None:
                self.cola.siguiente=nuevo_nodo
                self.cola = nuevo_nodo
                self.tamaño +=1
            else:
                pass
    
    def buscarPiso(self,nombre):
        actual = self.cabeza
        respuesta=None
        while(actual!=None):
            if actual.getNombre() == nombre:
                respuesta= actual
                break
            else:
                actual = actual.siguiente
        
        return respuesta



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

