from tkinter import filedialog, Tk
from xml.etree import ElementTree as et
from ListaPatron import ListaPatron 
from ListaPisos import ListaPisos 

lista_pisos= ListaPisos()  # lista simple donde se almacenara toda la informacion de los pisos
patrones = ListaPatron()


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
                            patrones.agregarPatron(codigo,patron)
                lista_pisos.agregarPiso(nombre,r,c,f,s,patrones)
        except:
            print('error al leer el archivo xml')
        else:
            print('lectura exitosa')
    else:
        print('ERROR: *** No se ha seleccionado ningun archivo ***')

def menu ():
    global lista_pisos
    seleccion= 0
    while (seleccion !=4):

        print ('\n**************************')
        print ('\n          Menu')
        print ('\n**************************')
        print('1. Cargar Archivo')
        print('2. Convertir Patron')
        print('3. Reportes')
        print('4. Salir')
        print ('**************************\n')

        try:
            seleccion = int(input('Seleccione una opcion: \n'))
            if seleccion == 1:
                cargar_archivo()
                lista_pisos.imprimirPisos()
            elif seleccion ==2:
                pass
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
