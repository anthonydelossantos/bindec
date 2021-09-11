
GUIDE = [128,64,32,16,8,4,2,1]


#funcion que convierte de binario a decimal

def binary_to_decimal(sentence):
    count = 0
    #convertimos el numero binario a una cadena de caracteres
    sentence = str(sentence)
    #luego dividimos cada caracter en un elemento de una lista 
    sentence = list(sentence)
    '''iteramos la lista en un rango de 0 a 8 donde si dentro de la lista del 
    binario el item es igual a 1 se procedera a sumar el valor de count mas el valor respectivo dentro de la constante GUIDE'''
    for i in range(0,8):
        if sentence[i] == "1":
            count+=GUIDE[i]
    return count


#funcion que convierte de decimal a binario

def decimal_to_binary(sentence):
    #declaramos str1 para guardar el binario final
    str1 = ''
    result = []
    guide_copy = GUIDE[:]
    x = True
    count = 0
    while x:
        for i in GUIDE:
            #TODO convertir a switch
            if count == sentence:
                x = False
            if count < sentence:
                #si count es menor al numero introducido 
                if count != i:
                    #y si es diferente a i 
                    #se ;e suma el valor de i a count
                    count += i
                    #y se agrega el valor de i a la lista result
                    result.append(i)
                else:
                    #de lo contraio se rompe el bucle 
                    x = False
            #si count es mayor que el numero introducido         
            if count > sentence:
                #se resta el ultimo numero de la lista result a count
                count -= result[-1] 
                # y se elimina ese mismo numero de la lista result
                del result[-1]
                continue
    #lo que se hace aqui es generar una lista de binarios 
    for binary in range(0,len(GUIDE)-1):
        guide_copy[binary] = '0'
        for result_decimal in result:
            if result_decimal == GUIDE[binary]:
                guide_copy[binary] = '1'


    for char in guide_copy:
       str1 += str(char)
            
    
    return str1


                

    


print(binary_to_decimal(10101000))
print(decimal_to_binary(253))

