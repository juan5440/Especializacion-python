# python 3.10
numero = int(input("digite numero: "))
match numero:
    case 1:
        print("numero is 1")
    case 2:
        print("numero is 2")
    case 3:
        print("numero is 3")
    case _:
        print("numero is not 1, 2 or 3")