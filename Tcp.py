import os
import General
def GetTcp(pframe):
    global frame
    frame = pframe
    print("===========TCP===========")
    GetOrigenDirecctionPort(str.replace(frame[102:107]," ",""))
    GetDestinationDirecctionPort(str.replace(frame[108:113]," ",""))
    GetSecuenceNumber(str.replace(frame[114:125]," ",""))
    GetConfirmationNumber(str.replace(frame[126:138]," ",""))
def GetOrigenDirecctionPort(porthex):
    print("Direccion de Puerto Origen: ",int(porthex,16))
def GetDestinationDirecctionPort(porthex):
    print("Direccion de Puerto Destino: ",int(porthex,16))
def GetSecuenceNumber(porthex):
    print("Numero de Secuencia: ",int(porthex,16))
def GetConfirmationNumber(porthex):
    print("Numero de Confirmacion: ",int(porthex,16))