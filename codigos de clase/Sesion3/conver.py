# programa de conversiones de bitcoin a dolar

menu = "****************** MENU *****************\n"
menu += "1. Bitcoin a Dolar\n"
menu += "2. Dolar a Bitcoin\n"
menu += "*****************************************\n"


print(menu)
op = int(input("Digite opcion: "))
while(op>=1 and op <=2):
    monto = float(input("digite monto: "))
    conver = 0
    if op == 1:
        conver = monto * 61908.60
    else:
        conver = monto / 61908.60
    
    print(f"el resultado es: {conver}\n")
    input()
    print(menu)
    op = int(input("Digite opcion: "))
    