from tkinter import filedialog, Tk
from xml.etree import ElementTree as et


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
    archivo= obtener_archivo('xml')
    if archivo != None:
        archivo_xml=et.parse(archivo)
        raiz= archivo_xml.getroot()
        
        try:
            for elemento in raiz:
                print(elemento.attrib)
                for hijo in elemento:
                    print(hijo.tag)
                    if hijo.tag == 'patrones':
                        for patr in hijo:
                            print(patr.attrib)
        except:
            print('error al leer el archivo xml')
        else:
            print('lectura exitosa')
    else:
        print('ERROR: *** No se ha seleccionado ningun archivo ***')


def menu ():
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
    #menu()
    list =[]
    list.append(2)
    list.append(3)
    list.append(4)
    list.append(5)
    for a in list:
        print(a)
