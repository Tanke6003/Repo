data =""
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
                GoMenu()
            elif(int(opc)==0):
                exit()
            else:
                print("Opcion en desarrollo")
        else:
            print("Opcion no valida")
def GoMenu():
    enter = False
    while enter != True:
        opc = input("Introduce 1 para continuar o 0 para volver al menu: ")
        if(opc.isnumeric()):
            if(int(opc)==1):
                Ip()
                enter = True
            elif(int(opc)==0):
                Main()
            else:
                print("Opcion no valida")
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
    global data
    archivo = open("tramaenhexdump.txt")
    for l in archivo:
        data +=l[6:54]
    archivo.close()
    print("====Cabecera Ethernet====")
    destination = GetDestination(data)
    print(destination)
    source = GetSource(data)
    print(source)
    type = getType(data)
    print(type)


#=========Ethernet Header
def GetDestination(data):
    return "Direccion Mac Destino: "+str.replace(data[0:17]," ",":")

def GetSource(data):
    return "Direccion Mac Origen: "+str.replace(data[18:35]," ",":")

def getType(data):
    if (str.replace(data[36:42]," ","") == "0800"):
        return "Tipo: PROTOCOLO IPV4 "+"0X"+str.replace(data[36:42]," ","")
    else:
        return "Tipo: PROTOCOLO EN DESARROLLO"

#==============
def Ip():
    global data
    print("====IP====")
    print(getVersion(data))
    print(getHeaderLen(data))
    getService(data)
    print(getAllLen(data))
    Go()


def getVersion(data):
    return "Version: "+str.replace(data[42]," ","")
def getHeaderLen(data):
    return "Longitud de Cabecera: "+str.replace(data[42]," ","")+" * "+str.replace(data[43]," ","")+" = "+str(int(str.replace(data[42]," ","")) * int(str.replace(data[43]," ","")))
def getService(data):
    service = bin(int(data[45:47],16))[2:].zfill(8)
    print(getPrecedencia(service))
    print(getTOS(service))
    print("MBZ: "+service[0])

def getPrecedencia(service):
    precedencia = service[4:8]
    precedencia = precedencia[1:]
    if precedencia == "000":
        precedencia= "Rutina"
    elif precedencia == "001":
        precedencia="prioridad"
    elif precedencia == "010":
        precedencia="inmediato"
    elif precedencia == "011":
        precedencia="Flash"
    elif precedencia == "100":
        precedencia="Flash override"
    elif precedencia == "101":
        precedencia="critico"
    elif precedencia == "110":
        precedencia="Control de red ('internetwork control')"
    elif precedencia == "111":
        precedencia="Control de red ('network control')"
    else :
        precedencia="No valido"
    return "Precedencia: "+ precedencia
def getTOS(service):
    TOS = service[1:5]
    if TOS == "1000":
        TOS = "Minimizar retardo"
    elif TOS == "0100":
        TOS = "Maximizar la densidad de flujo"
    elif TOS == "0010":
        TOS = "Maximizar la fiabilidad"
    elif TOS == "0001":
        TOS = "Minimizar el coste monetario"
    elif TOS == "0000":
        TOS = "servicio normal"
    else:
        TOS = "No valido"
    return "TOS(TIPO DE SERVICIO): "+TOS
    
def getAllLen(data):
    PackageLen = str.replace(data[48:53]," ","")
    PackageLendec = int(PackageLen,16)
    PackageLen = str.replace(data[47:53]," ","")
    return "Longitud total del paquete= "+PackageLen[3:]+"H"+" = "+str(PackageLendec)+" bytes"

    




Main()