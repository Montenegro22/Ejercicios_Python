print ("Bienvenido al Ejercicio 3")
print ("Este programa está diseñado para que el usuario pueda calcular el descuento de un producto dependiendo el día de la semana ")
print ("Let´s do it!")

input("Digite el nombre del producto que desea comprar -> ")
valor = int(input("Digite el valor del producto que desea comprar -> "))

print ("A continuación deberá digitar el día de la semana para hacer efectivo el descuento de la siguiente manera: Si es lunes digitar ""l"", si es martes digitar ""m"", miercoles ""M"", jueves ""j"", viernes ""v"", sabado ""s"", domingo ""d""... respectivamente  ")

dia = input ("Digite el día de la semana -> ")

if dia == "l":
    des1 = ((valor *10)/100)
    descuento_l = (valor-des1)
    print ("Su producto tiene un descuento de 10% ")
    print ("El valor final de su producto es de -> ", descuento_l , "pesos")
    
if dia == "m":
    des2 = ((valor *5)/100)
    descuento_m = (valor-des2)
    print ("Su producto tiene un descuento de 5% ")
    print ("El valor final de su producto es de -> ", descuento_m , "pesos")

if dia == "M":
    des3 = ((valor *3)/100)
    descuento_M = (valor-des3)
    print ("Su producto tiene un descuento de 3% ")
    print ("El valor final de su producto es de -> ", descuento_M , "pesos")

if dia == "j":
    des4 = ((valor *1)/100)
    descuento_j = (valor-des4)
    print ("Su producto tiene un descuento de 1% ")
    print ("El valor final de su producto es de -> ", descuento_j , "pesos")

if dia == "v":
    des5 = ((valor *7)/100)
    descuento_v = (valor-des5)
    print ("Su producto tiene un descuento de 7% ")
    print ("El valor final de su producto es de -> ", descuento_v , "pesos")

if dia == "s":
    print ("Su producto el día de hoy no tiene ningun descuento")
    print ("El valor final de su producto es de -> ", valor, "pesos")

if dia == "d":
    des7 = ((valor *1)/100)
    descuento_d = (valor-des7)
    print ("Su producto tiene un descuento de 1% ")
    print ("El valor final de su producto es de -> ", descuento_d , "pesos")
    
print ("Gracias por utilizar este programa")    
            
