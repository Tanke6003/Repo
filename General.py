#funcion to convert a string of hexadecimal to binary
def StringHexaToBinary(strHex):
    return bin(int(strHex,16))[2:].zfill(len(strHex)*4)
def Go(x,y):
    enter = False
    while enter != True:
        if(y == exit):
            opc = input("Introduce 1 para salir o 0 regresar al menu: ")
        else:
            opc = input("Introduce 1 para continuar o 0 regresar al menu: ")
        if(opc.isnumeric()):
            if(int(opc)==1):
                if(y!="continue"):
                    y()
                enter = True
                return
            elif(int(opc)==0):
                x()
            else:
                print("Opcion no valida")
        else:
            print("Opcion no valida")

    