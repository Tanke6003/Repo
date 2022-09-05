import Ethernet
import Ip
import General
frame =""
def Main():
    global frame
    enter = False
    while enter != True:
        frame = ""
        print("======Bienvenido a AxoSniffer======\n=         Maestro:Gorge Anaya     =")
        print("=               Menu              =\n=      1.-Cargar desde Archivo    =")
        print("=      2.-Utilizar una Interfaz   =\n=      0.-salir                   =")
        print("===================================")
        opc = input("Elige una Opcion: ")
        if(opc.isnumeric()):
            if(int(opc)==1):
                Archivo()
            elif(int(opc)==0):
                exit()
            else:
                print("Opcion en desarrollo")
        else:
            print("Opcion no valida")
def Archivo():
    global frame
    archivo = open("tramaenhexdump.txt")
    for l in archivo:
        frame +=l[6:54]
    archivo.close()
    frame = str.replace(frame,"  "," ")
    Ethernet.GetEthernetFrame(frame)
    General.Go(Main)
    Ip.GetIp(frame)


Main()
