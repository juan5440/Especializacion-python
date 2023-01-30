# programa para deciciones if elif

edad = int(input("digite su edad: "))

if edad>=18:
    print("Es mayor de edad")
elif edad>=60 and edad <=90:
    print("Es de la tercera edad")
elif edad >90:
    print("Es de la cuarta edad")
else:
    print("Es menor de edad")