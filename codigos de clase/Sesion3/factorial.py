# programa para estructuras repetitivas
# for para determinadas repeticiones
# while para indeterminadas repeticiones

# 5! = 5x4x3x2x1 = 120
n = int(input("digite un numero: "))
f = 1
# for i in range(1,n+1):
#     f *=i
#     print(i)

i = 1
while(i<n+1):
    f *=i
    i+=1
print(f"el factorial de {n} es: {f}")

cadena = "hola mundo"
for c in cadena:
    print(c, end="-")

