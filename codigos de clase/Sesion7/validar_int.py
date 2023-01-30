def validar_int(numero):
    n = None
    try:
        n = int(numero)
        return n
    except Exception as e:
        # print(e)
        return n

op = input("digite una opcion")

if validar_int(op):
    print("la opcion es entera")
else:
    print('la opcion no es entera')
