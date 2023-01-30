#
edad = int(input("digite su edad: "))

match edad:
    case 18:
        print("es mayor de edad", edad)
    case 16:
        print("es menor de edad", edad)
    case 68:
        print("es de la tercera edad", edad)
    case _:
        print("error de edad", edad)