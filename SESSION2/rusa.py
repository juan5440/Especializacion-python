# mdor = input("Ingrese el numero multiplicador: ")
# mdo = input("Ingrese el numero multiplicando: ")

# a = 0
# b = mdor
# c = mdo

# while (c >= 0):

#     if(c % 2 != 0):
#         a = a + b

#         c = c // 2
#         b = b * 2
# print(f"El resutado de la multiplicacion  es: {a} ")

num1 = input("Ingrese el preimer numero a multiplicar: ")
num2 = input("Ingrese segundo numero a multiplicar: ")
suma = 0

try:
    num1 = int(num1)
    num2 = int(num2)
except:
    num1 = False
    num2 = False
if num1 == False or num2 == False:
    print("solo se premite ingrsar numeros enteros")
else:
    while num1 >= 1:
        if num1 % 2 != 0:
            suma = suma + num2
            num1 = num1 // 2
            num2 = num2 * 2

print("el resutado es: ", suma)
