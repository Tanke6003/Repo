
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
def sumarry(a,b):
    carry = "0"
    res =""
    for i in range(len(a)):
        turn = 0
        pos = (len(a)-1) - i
        if carry == "1" and turn == 0:
            turn =1
            if a[pos]=="1" and b[pos]=="1":
                res = "1"+res
                carry = "1"
            elif a[pos]=="1" and b[pos]=="0":
                res = "0"+res
                carry ="1"
            elif a[pos]=="0" and b[pos]=="1":
                res = "0"+res
                carry ="1"
            elif a[pos]=="0" and b[pos]=="0":
                res = "1"+res
                carry ="0"
        if carry == "0"and turn == 0:
            turn = 1
            if a[pos]=="1" and b[pos]=="1":
                res = "0"+res
                carry = "1"
            elif a[pos]=="1" and b[pos]=="0":
                res = "1"+res
                carry ="0"
            elif a[pos]=="0" and b[pos]=="1":
                res = "1"+res
                carry ="0"
            elif a[pos]=="0" and b[pos]=="0":
                res = "0"+res
                carry ="0"
        ##print("pos:",pos,"a:",a[pos],"b:",b[pos])
    if carry == "1":
        carry = "0"
        res2 = sumarry(res,"0000000000000001")
        res= ""
        res = res2
    """ print("a:",a)
    print("b:",b)
    print("c:",res)
    print("------------------------") """
    return res
""" def suma_binaria(numero_binario_1, numero_binario_2):
    lista_resultado_suma = numero_binario_1
<<<<<<< HEAD
    lista_resultado_suma = list(lista_resultado_suma)

=======
    carry = '0'
>>>>>>> 3a058a1f4029051b0fef6844e3796840860587ad
    for e in range(len(numero_binario_1)):
        if carry == '1' and e == len(numero_binario_1):
            if numero_binario_1[e] == '1' and numero_binario_2[e] == '1': 
                lista_resultado_suma[e] == '11'                                                  
            elif numero_binario_1[e] == '1' and numero_binario_2[e] == '0': 
                lista_resultado_suma[e] = '10'                                                                                 
            elif numero_binario_1[e] =='0' and numero_binario_2[e] == '1': 
                lista_resultado_suma[e] = '10'
            elif numero_binario_1[e] == '0' and numero_binario_2[e] == '0':
                lista_resultado_suma[e] = '1'
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


    strres = ""
    return strres.join(lista_resultado_suma)
 """