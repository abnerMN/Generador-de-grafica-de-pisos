from os import system,startfile
from tkinter import filedialog, Tk
from xml.etree import ElementTree as et
from ListaPatron import ListaPatron 
from ListaPisos import ListaPisos 

lista_pisos= ListaPisos()  # lista simple donde se almacenara toda la informacion de los pisos


#funcion para obtener los archivos por una ventana emergente
def obtener_archivo(tipo):
    Tk().withdraw()
    archivo = filedialog.askopenfilename(
        title= "Seleccione un archivo",
        initialdir="./",
        filetypes= {
            ("archivos "+tipo, "*."+tipo)
        }
    )
    if archivo:
        return archivo
    else:
        return None

def cargar_archivo():
    global lista_pisos
    archivo= obtener_archivo('xml')
    if archivo != None:
        archivo_xml=et.parse(archivo)
        raiz= archivo_xml.getroot()
        try:
            nombre=''
            r=''
            c=''
            f=''
            s=''
            codigo=''
            patron=''
            bandera1=False
            bandera2=False
            for elemento in raiz:
                for key in elemento.attrib:
                    nombre=elemento.attrib[key]
                for hijo in elemento:
                    a=hijo.text.strip()
                    if hijo.tag == 'R':
                        r=a
                    elif hijo.tag =='C':
                        c=a
                    elif hijo.tag == 'F':
                        f=a
                    elif hijo.tag== 'S':
                        s=a
                    if hijo.tag == 'patrones':
                        patrones = ListaPatron()
                        for patr in hijo:
                            for key in patr.attrib:
                                    codigo=patr.attrib[key]
                            patron=patr.text.strip()
                            patron=patron.upper()
                            for char in patron:
                                if char == 'W' or char == 'B':
                                    bandera2=True
                                else:
                                    bandera2=False
                                    break
                            if bandera2 == True:
                                patrones.agregarPatron(codigo,patron,r,c)
                                bandera1=True
                            else:
                                bandera1=True
                if bandera1==True and bandera2==True:
                    lista_pisos.agregarPiso(nombre,r,c,f,s,patrones)
                else:
                    print('ERROR: *** El patron no tiene las mismas dimensiones que la matriz ***')
        except:
            print('error al leer el archivo xml')
        else:
            print('lectura exitosa')
    else:
        print('ERROR: *** No se ha seleccionado ningun archivo ***')

def buscar():
    global lista_pisos
    nombre= input("ingrese el nombre del piso\n")
    tmp=lista_pisos.buscarPiso(nombre)
    if tmp !=None:
        #tmp.impresionPiso()
        listaPatron = tmp.getListaPatron()
        if listaPatron != None:
            codigo = input("ingrese el codigo del patron del piso\n")
            dato_patron= listaPatron.buscarPatron(codigo)
            #dato_patron.impresionNodoPatron()
            filas=int(tmp.getFila())
            columnas=int(tmp.getColumna())
            patron=dato_patron.getPatron()
            grafica(filas,columnas,patron,codigo)
        else:
            print('*** Patron no registrado ***')
    else:
        print('*** Piso no registrado ***')

def grafica(filas,columnas,patron,codigo):
    posicion = 0

    graphviz='''
digraph L{
    node [shape = box fillcolor ="#FFEDBB" style =filled]
    subgraph cluster_p{
        label ='''+codigo+'''
        bgcolor = "#398D9C"
edge[dir = "none" color ="#398D9C"]
'''
    for i in  range(filas):
        for j in range(columnas):
            if i==0:
                if j ==0:
                    if patron[posicion]=='W':
                        graphviz+='''raiz[label = "",fillcolor =white]'''
                    else:
                        graphviz+='''raiz[label = "",fillcolor =black]'''
                else:
                    if j ==1:
                        if patron[posicion]=='W':
                            graphviz+='''\nColumna'''+str(j)+'''[label= "", group=2,fillcolor =white];
raiz-> Columna'''+str(j)+''';
{rank=same;raiz;Columna'''+str(j)+'''}'''
                        else:
                            graphviz+='''\nColumna'''+str(j)+'''[label= "", group=2,fillcolor =black];
raiz-> Columna'''+str(j)+''';
{rank=same;raiz;Columna'''+str(j)+'''}'''
                    else:
                        if patron[posicion]=='W':
                            graphviz+='''\nColumna'''+str(j)+'''[label= "", group=3,fillcolor =white];
Columna'''+str(j-1)+'''->Columna'''+str(j)+''';
{rank=same;raiz;Columna'''+str(j)+'''}'''
                        else:
                            graphviz+='''\nColumna'''+str(j)+'''[label= "", group=3,fillcolor =black];
Columna'''+str(j-1)+'''->Columna'''+str(j)+''';
{rank=same;raiz;Columna'''+str(j)+'''}'''
            else:
                if j==0:
                    if i==1:
                        if patron[posicion]=='W':
                            graphviz+='''\nFila'''+str(i)+'''[label="", group=1,fillcolor =white];
raiz->Fila'''+str(i)+''';'''
                        else:
                            graphviz+='''\nFila'''+str(i)+'''[label="", group=1,fillcolor =black];
raiz->Fila'''+str(i)+''';'''
                    else:
                        if patron[posicion]=='W':
                            graphviz+='''\nFila'''+str(i)+'''[label="", group=1,fillcolor =white];
Fila'''+str(i-1)+'''-> Fila'''+str(i)+''';'''
                        else:
                            graphviz+='''\nFila'''+str(i)+'''[label="", group=1,fillcolor =black];
Fila'''+str(i-1)+'''-> Fila'''+str(i)+''';'''
                else:
                    if j==1:
                        if patron[posicion]=='W':
                            graphviz+='''\nnodo'''+str(i)+'''_fila'''+str(j)+'''[label ="", fillcolor =white, group=2]
Fila'''+str(i)+'''->nodo'''+str(i)+'''_fila'''+str(j)+''';
{rank=same;Fila'''+str(i)+''';nodo'''+str(i)+'''_fila'''+str(j)+'''}
                    '''
                        else:
                            graphviz+='''\nnodo'''+str(i)+'''_fila'''+str(j)+'''[label ="", fillcolor =black, group=2]
Fila'''+str(i)+'''->nodo'''+str(i)+'''_fila'''+str(j)+''';
{rank=same;Fila'''+str(i)+''';nodo'''+str(i)+'''_fila'''+str(j)+'''}
                    '''
                    else:
                        if patron[posicion]=='W':
                            graphviz+='''\nnodo'''+str(i)+'''_fila'''+str(j)+'''[label ="", fillcolor =white, group=2]
nodo'''+str(i)+'''_fila'''+str(j-1)+'''->nodo'''+str(i)+'''_fila'''+str(j)+'''
{rank=same;Fila'''+str(i)+''';nodo'''+str(i)+'''_fila'''+str(j)+'''}
                    '''
                        else:
                            graphviz+='''\nnodo'''+str(i)+'''_fila'''+str(j)+'''[label ="", fillcolor =black, group=2]
nodo'''+str(i)+'''_fila'''+str(j-1)+'''->nodo'''+str(i)+'''_fila'''+str(j)+'''
{rank=same;Fila'''+str(i)+''';nodo'''+str(i)+'''_fila'''+str(j)+'''}
                    '''
            posicion+=1
    graphviz+='''
    }
}
'''

    generar_grafica = open('graphviz.dot','w')
    generar_grafica.write(graphviz)
    generar_grafica.close()
    system('dot -Tpng graphviz.dot -o graphviz.png')
    system('cd ./graphviz.png')
    startfile('graphviz.png')

def menu ():
    global lista_pisos
    seleccion= 0
    while (seleccion !=4):

        print ('\n**************************')
        print ('\n          Menu')
        print ('\n**************************')
        print('1. Cargar Archivo')
        print('2. Obtener grafica')
        print('3. Reportes')
        print('4. Salir')
        print ('**************************\n')

        try:
            seleccion = int(input('Seleccione una opcion: \n'))
            if seleccion == 1:
                cargar_archivo()
                lista_pisos.imprimirPisos()
            elif seleccion ==2:
                buscar()
            elif seleccion == 3:
                pass
            elif seleccion == 4:
                print ("*** Adios ***")            
            else:
                print ('*** Opcion no disponible ***')
        except:
            print('*** Por favor seleccione una opcion valida ***')


#main
if __name__=='__main__':
    menu()
