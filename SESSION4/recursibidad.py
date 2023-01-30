# recursividad es una funcion se llama asi misma y existe un caso base que termina las llamadas recusivas
# recursividad es una alternartiva a las estructuras repetitivas (fro, while)
# consume muchos recursos de procesamiento 
# 5! = 5x4x3x2x1 

# def factorial(n):
#     if n==1:
#         return 1
#     return factorial(n-1)*n

# print(factorial(5))

#ejercicio: imprimir los numeros en decendente de n(pedir n)

def desendente(n):
     if n==1:
         return 1
     print(n)
     return desendente(n-1)

print(desendente(5))