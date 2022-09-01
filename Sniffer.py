import Ethernet
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
    GetIp()

def GetIp():
    print("===========IPV4===========")
    GetVersion()
    GetHeaderLen()
    GetService()
    GetAllLen()
    GetIdentify()
    GetFlags()

def GetVersion():
    return print("Version: "+str.replace(frame[42]," ",""))
def GetHeaderLen():
    return print("Longitud de Cabecera: "+str.replace(frame[42]," ","")+" * "+str.replace(frame[43]," ","")+" = "+str(int(str.replace(frame[42]," ","")) * int(str.replace(frame[43]," ",""))))
def GetService():
    service = General.StringHexaToBinary(frame[45:47])
    GetPrecedencia(service)
    GetTOS(service)
    GetMBZ(service[7])

def GetPrecedencia(data):
    precedencia = data[0:3]
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
    return print("Precedencia: "+ precedencia)
def GetTOS(service):
    GetDelay(service[3])
    GetTroughput(service[4])
    GetReliability(service[5])
    GetCost(service[6])
def GetDelay(data):
    if data == "0":
        return print("Delay: Normal")
    elif data == "1":
        return print("Delay: Low")
def GetTroughput(data):
    if data == "0":
        return print("Troughput: Normal")
    elif data == "1":
        return print("Troughput: High")
def GetReliability(data):
    if data == "0":
        return print("Reliability: Normal")
    elif data == "1":
        return print("Reliability: High")
def GetCost(data):
    if data == "0":
        return print("Cost: Normal")
    elif data == "1":
        return print("Cost: Low")
def GetMBZ(data):
    if data == "0":
        return print("MBZ: 0")
    elif data == "1":
        return print("MBZ: 1 ('Error campo reservado activo')")
def GetAllLen():
    return print("Longitud total del paquete: "+str.replace(frame[48:53]," ","")+"H"+" = "+str(int(str.replace(frame[48:53]," ",""),16))+" bytes")
def GetIdentify():
    return print("Identificacion: "+str.replace(frame[54:59]," ",""))
def GetFlags():
    GetBitReservado(General.StringHexaToBinary(str.replace(frame[60:65]," ","")))
    GetDF(General.StringHexaToBinary(str.replace(frame[60:65]," ","")))
    GetMF(General.StringHexaToBinary(str.replace(frame[60:65]," ","")))
def GetBitReservado(data):
    if data[0] == "0":
        return "Bit reservado: 0"
    elif data[0] == "1":
        return "Bit reservado: 1 ('Error este campo debe ser reservado')"
def GetDF(data):
    if data[1] == "0":
        return "DF: Permite Fragmentacion"
    elif data[1] == "1":
        return "DF: No Permite Fragmentacion"
def GetMF(data):
    if data[2] == "0":
        return "MF: No es el ultimo paquete del datagrama"
    elif data[2] == "1":
        return "MF: Es el ultimo paquete del datagrama"







Main()

