# python 3.10
thing = int(input("digite thing: "))
match thing:
    case 1:
        print("thing is 1")
    case 2:
        print("thing is 2")
    case 3:
        print("thing is 3")
    case _:
        print("thing is not 1, 2 or 3")