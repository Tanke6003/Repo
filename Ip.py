import General
def GetIp(pframe):
    global frame
    frame = pframe
    print("===========IPV4===========")
    GetVersion()
    GetHeaderLen()
    GetService()
    GetAllLen()
    GetIdentify()
    GetFlags()
    GetDesplazamiento()
    GetTimeLife()
    #Getprotocolo()
    


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
    GetBitReservado(General.StringHexaToBinary(str.replace(frame[60:62]," ","")))
    GetDF(General.StringHexaToBinary(str.replace(frame[60:62]," ","")))
    GetMF(General.StringHexaToBinary(str.replace(frame[60:62]," ","")))
def GetBitReservado(data):
    if data[0] == "0":
        return print("Bit reservado: 0")
    elif data[0] == "1":
        return print("Bit reservado: 1 ('Error este campo debe ser reservado')")
def GetDF(data):
    if data[1] == "0":
        return print("DF: Permite Fragmentacion")
    elif data[1] == "1":
        return print("DF: No Permite Fragmentacion")
def GetMF(data):
    if data[2] == "0":
        return print("MF: Es el ultimo paquete del datagrama")
    elif data[2] == "1":
        return print("MF: No es el ultimo paquete del datagrama")
def GetDesplazamiento():
    desplazamiento = General.StringHexaToBinary(str.replace(frame[60:65]," ","a"))
    desplazamiento = desplazamiento[4:]
    print("Desplazamiento de la fragmentacion: " + str(int(desplazamiento,2)))
def GetTimeLife():
    return print("Tiempo de vida en segundos: " +str(int(str.replace(frame[66:68]," ",""),16)))
def Getprotocolo():
    return print(str.replace(frame[69:71]," ",""))