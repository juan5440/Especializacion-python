# Elaborar un programa que permita realizar una conversión de monedas, sea esta de dólar a colon o
# viceversa, considere al menos 3 monedas (Bitcoin) diferentes y permita al usuario seleccionar que
# conversión desea hacer mediante un menú.

print("1 de dolares a colon salvadoreño: ")
print("2 de colon a dolares: ")
print("3 de dolares a quetzal: ")
print("4 de bintcoins a dolares: ")
print("5 dolares a bintcoins: ")
print ("")
opl=int(input("coloque aqui opcion: "))
print ("")
if opl==1:
    dol1=int(input("introdusca cantidad en dolar: "))
    colon=dol1*8.77
    print ("")
    print ("pesos chilenos=", colon)
if opl==2:
    colon=float(input("introdusca colon salvadoreño: "))
    dol2=colon/0.0016
    print("")
    print("cantidad en dolar: ", dol2)
if opl==3:
    dol3=float(input("introdusca cantidad en dolares:"))
    quetzal=dol3*7.75
    print("")
    print("cantidad en quetzales:", quetzal)
if opl==4:
    dolar=float(input("introduzca dolares:"))
    bintcoint=dolar*0.000016
    print("")
    print("Cantidad en bintcoin es: ", bintcoint)
if opl==5:
    bit=float(input("coloque cantidad en bitcoin: "))
    dol5=bit/63883,60
    print("")
    print("cantidad en dolar es: ", dol5)