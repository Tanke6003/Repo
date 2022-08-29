
def Main():
    enter = False
    while enter != True:
        print("======Bienvenido a AxoSniffer======\n=         Alumno:Ruben Farias     =\n=         Maestro:Gorge Anaya     =")
        print("=               Menu              =\n=      1.-Cargar desde Archivo    =\n=      2.-Utilizar una Interfaz   =\n=      0.-salir                   =")
        print("===================================")
        opc = input("Elige una Opcion: ")
        if(opc.isnumeric()):
            if(int(opc)==1):
                Archivo()
                Go()
            elif(int(opc)==0):
                exit()
            else:
                print("Opcion en desarrollo")
        else:
            print("Opcion no valida")

def Go():
    enter = False
    while enter != True:
        opc = input("Introduce 1 para continuar o 0 para salir del programa: ")
        if(opc.isnumeric()):
            if(int(opc)==1):
                Main()
                enter = True
            elif(int(opc)==0):
                exit()
            else:
                print("Opcion no valida")
        else:
            print("Opcion no valida")

def Archivo():
    archivo = open("tramaenhexdump.txt")
    data = ""
    for l in archivo:
        data +=l[6:54]
    archivo.close()
    destination = GetDestination(data)
    print("Destino: ",destination)
    source = GetSource(data)
    print("Origen: ",source)
    type = getType(data)
    print("Tipo: ",type)

def GetDestination(data):
    return str.replace(data[0:17]," ",":")

def GetSource(data):
    return str.replace(data[18:35]," ",":")

def getType(data):
    if (str.replace(data[36:42]," ","") == "0800"):
        return "PROTOCOLO IPV4 "+"0X"+str.replace(data[36:42]," ","")
    else:
        return "PROTOCOLO EN DESARROLLO"


Main()