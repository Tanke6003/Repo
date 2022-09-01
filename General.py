#funcion to convert a string of hexadecimal to binary
def StringHexaToBinary(strHex):
    return bin(int(strHex,16))[2:].zfill(len(strHex)*4)
def Go(x):
    enter = False
    while enter != True:
        opc = input("Introduce 1 para continuar o 0 regresar al menu: ")
        if(opc.isnumeric()):
            if(int(opc)==1):
                enter = True
                return
            elif(int(opc)==0):
                x()
            else:
                print("Opcion no valida")
        else:
            print("Opcion no valida")

    