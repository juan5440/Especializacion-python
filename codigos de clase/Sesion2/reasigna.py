# operadores de reasignacion

n = input("digite un numero: ")
print("el numero captura es: "+n)
print("el tipo de n es: ", type(n))

n = int(n)
n +=10 # n = n + 10
print("el resultado es: ", n)
print("el resultado es: " +  str(n))
m = 5
print(f"el resultado es: {n},\n y m vale {m}")
print(f"el resultado es: {n}", f"y m vale {m}", sep="\n")
print("""primera linea
segunda linea
""")