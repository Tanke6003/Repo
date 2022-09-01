
def GetEthernetFrame(pframe):
    global frame
    frame = pframe
    print("====Cabecera Ethernet====")
    GetDestination()
    GetSource()
    GetType()
def GetDestination():
    return print("Direccion Mac Destino: "+str.replace(frame[0:17]," ",":"))

def GetSource():
    return print("Direccion Mac Origen: "+str.replace(frame[18:35]," ",":"))

def GetType():
    if (str.replace(frame[36:42]," ","") == "0800"):
        return print("Tipo: PROTOCOLO IPV4 "+"0X"+str.replace(frame[36:42]," ",""))
    else:
        return print("Tipo: PROTOCOLO EN DESARROLLO")

#==============