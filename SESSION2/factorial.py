# programa para calcular el factorial

# 5! = 5*4*3*2*1 = 120

# for se usa para repeticiones determinadas
#while repeticiones sin determinar o determinadas

# n = int(input("digite un numero: "))

# f = 1

# for i in range(1, n+1): #n-1
#     f  *= i

# print(f"el factorial es: {f}")

# contador con while
n = int(input("digite un numero: "))

f = 1

i = 1
while(i<n+1):
    f *= i
    i += 1

print(f"el factorial es: {f}")
