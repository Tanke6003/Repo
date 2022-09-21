
def StringHexaToBinary(strHex):
    return bin(int(strHex,16))[2:].zfill(len(strHex)*4)
def StringBinToBinary(strBin):
    return bin(int(strBin,2))[2:].zfill(len(strBin))
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
def Continue():
    enter = False
    while enter != True:
        opc = input("Introduce 1 para continuar o 0 regresar al menu: ")
        if(opc.isnumeric()):
            if(int(opc)==1):
                return
            elif(int(opc)==0):
                exit()
            else:
                print("Opcion no valida")
        else:
            print("Opcion no valida")
def ComplementOne(bitnumber):
    length = len(bitnumber)
    bit = ""
    i = 0
    for i in range(length):
        if bitnumber[i] == "0":
            bit += "1"
        else:
            bit += "0"
    return bit
def suma_binaria(numero_binario_1, numero_binario_2):
    
    carry = '0'
    lista_resultado_suma = numero_binario_1
    lista_resultado_suma = list(lista_resultado_suma)

    for e in range(len(numero_binario_1)):
        
        if carry == '1':
            if numero_binario_1[e] == '1' and numero_binario_2[e] == '1': 
                lista_resultado_suma[e] == '1'
                carry = '1'                                                       
            elif numero_binario_1[e] == '1' and numero_binario_2[e] == '0': 
                lista_resultado_suma[e] = '0'                              
                carry = '1'                                                            
            elif numero_binario_1[e] =='0' and numero_binario_2[e] == '1': 
                lista_resultado_suma[e] = '0'
                carry = '1'
            elif numero_binario_1[e] == '0' and numero_binario_2[e] == '0':
                lista_resultado_suma[e] = '1'
                carry = '0'

        if carry == '0':
            if numero_binario_1[e] == '1' and numero_binario_2[e] == '1':
                lista_resultado_suma[e] = '0'
                carry = '1'
            elif numero_binario_1[e] == '1' and numero_binario_2[e] == '0':
                lista_resultado_suma[e] = '1'
                carry = '0'
            elif numero_binario_1[e] =='0' and numero_binario_2[e] == '1':
                lista_resultado_suma[e] = '1'
                carry = '0'
            elif numero_binario_1[e] == '0' and numero_binario_2[e] == '0':
                lista_resultado_suma[e] = '0'
                carry = '0'

    for e in range(len(lista_resultado_suma)):
        if carry == '1':
            lista_resultado_suma[0] = '1'

    ComplementOne(lista_resultado_suma)
    return lista_resultado_suma


    