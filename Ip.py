import os
import General
def GetIp(pframe):
    global frame
    frame = pframe
    print("===========IPV4 pt 1===========")
    GetVersion()
    GetHeaderLen()
    GetService()
    GetAllLen()
    GetIdentify()
    GetFlags()
    GetDesplazamiento()
    General.Continue()
    print("===========IPV4 pt 2===========")
    GetTimeLife()
    Getprotocolo()
    GetCheckSum()
    GetIpOrigin()
    GetIpDestino()

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
    protocolo = int(str.replace(frame[69:71]," ",""),16)
    if protocolo == 0:
        return print("Protocolo: Reservado")
    elif protocolo == 1:
        return print("Protocolo: ICMP(\"Internet Control Message Protocol\")")
    elif protocolo == 2:
        return print("Protocolo: IGMP(\"Internet Group Management Protocol\")")
    elif protocolo == 3:
        return print("Protocolo: GGP(\"Gateway-to-Gateway Protocol\")")
    elif protocolo == 4:
        return print("Protocolo: IP(IP encapsulation)")
    elif protocolo == 5:
        return print("Protocolo: Flujo(\"Stream\")")
    elif protocolo == 6:
        return print("Protocolo: TCP(\"Transmission Control\")")
    elif protocolo == 8:
        return print("Protocolo: EGP (\“Exterior Gateway Protocol\”)")
    elif protocolo == 9:
        return print("Protocolo: PIRP (“Private Interior Routing Protocol”)")
    elif protocolo == 17:
        return print("Protocolo: UDP (“User Datagram”)")
    elif protocolo == 89:
        return print("Protocolo: OSPF (“Open Shortest Path First”)")
    else:
        return print("Protocolo: no reconocido")
def GetCheckSum():
    ipbody = str.replace(str.replace(frame[42:101]," ",""),"\n","")
    limitInf = 0
    limitSup = 4
    res = "0000000000000000"
    iplenght = len(ipbody)
    i=0
    while(limitSup <= iplenght):
        i=i+1
        ##print("HEXA: ",ipbody[limitInf:limitSup]," BIN: ", General.StringHexaToBinary(ipbody[limitInf:limitSup]))
        ##print("BIN: ", General.StringHexaToBinary(ipbody[limitInf:limitSup]))
        ##print("complemento",General.ComplementOne(General.StringHexaToBinary(ipbody[limitInf:limitSup])))
        if( limitInf != 20):
            ##print("numhexa",ipbody[limitInf:limitSup])
            numhexa = General.StringHexaToBinary(ipbody[limitInf:limitSup])
            ##print("numhexa convert to bin ",numhexa)
            ##numbin = General.StringBinToBinary(numhexa)
            numbin = General.ComplementOne(numhexa)
            
            ##res = General.suma_binaria(list(res),list(numbin))
            res = General.sumarry(res,numbin)
            ##print("strin bin convert to bin: ",numbin ,"LONG: ",len(numbin) )
            ##if(res==""):
            ##    res = numbin
            ##else:
            ##    res = bin(int(res,2)+int(numbin,2))[2:]
            ##print("res: ",res," Long: ", len(res),"carry: ",res[0],"reswithoutcarry: ",res[1:] )
            ##if(len(res)>16 and res[0]=='1'):
            ##    carry = res[0]
            ##    print("carry ",carry)
            ##    res = bin(int(res[1:],2)+int(carry,2))[2:]
            ##    print("res: ",res," Long: ", len(res),"carry: ",res[0],"reswithoutcarry: ",res[1:] )
            ##res = General.ComplementOne(res)
        limitInf = limitSup
        limitSup += 4
    ##print(res)
    check =  General.sumarry(res,General.ComplementOne(General.StringHexaToBinary(ipbody[20:24])))
    check = hex(int(check,2))
    if(check != "0xffff"):
        return print("checksum: incorrecto")
    return print("checksum: correcto ",check) 

def GetIpOrigin():
    Iphexa = str.replace(frame[78:89]," ","")
    liminf =0
    limsup= 2
    ipdecimal = ""
    while(limsup <= len(Iphexa)):
        ipdecimal += str(int(Iphexa[liminf:limsup],16))+"."
        liminf = limsup
        limsup = limsup + 2
    ipdecimal = ipdecimal[0:len(ipdecimal)-1]
    return print("Direccion IP Origen: "+ ipdecimal)
def GetIpDestino():
    Iphexa = str.replace(str.replace(frame[89:101]," ",""),"\n","")
    liminf =0
    limsup= 2
    ipdecimal = ""
    while(limsup <= len(Iphexa)):
        ipdecimal += str(int(Iphexa[liminf:limsup],16))+"."
        liminf = limsup
        limsup = limsup + 2
    ipdecimal = ipdecimal[0:len(ipdecimal)-1]
    return print("Direccion IP Origen: "+ ipdecimal)