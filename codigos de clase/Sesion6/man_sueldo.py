# from calculos.isr import saludo
# saludo()

#from calculos import isr
# isr.saludo()

# from calculos.isr import *
# saludo()

# import modos
# modos.main()

# import calculos.isr
# calculos.isr.saludo()
from calculos import isr
def main():
    print("""
***************************************************
Elija una opcion: 
[1] ISSS
[2] AFP
[3] ISR
[4] Descuentos
[5] Sueldo Gravable
[6] Sueldo a pagar
[#] Salir
***************************************************
    """)
    op = int(input("digite opcion: "))
    if op>=1 and op <=6:
        sueldo = float(input("digite el sueldo: "))
        if op==1:
            isss = isr.isss(sueldo)
            print(f"El isss es: $ {isss:.2f}")
        elif op==2:
            afp = isr.afp(sueldo)
            print(f"El afp es: $ {afp:.2f}")
        elif op==3:
            ISR = isr.isr(sueldo)
            print(f"El isr es: $ {ISR:.2f}")
        elif op==4:
            des = isr.descuentos(sueldo)
            print(f"El descuento total es: ${des:.2f}")
        elif op==5:
            sg = isr.sueldo_gravable(sueldo)
            print(f"El sueldo grabable es: $ {sg:.2f}")
        elif op==6:
            sp = isr.sueldo_pagar(sueldo)
            print(f"El sueldo a pagar es: $ {sp:.2f}")
if __name__=="__main__":
    main()
