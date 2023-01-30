nombres = ["alicia","beto","carlos"]
print(len(nombres))
print(nombres[3])

nombres[3] = "eva" # se agrega en la lista el nombre eva

print(nombres)

nombres.append("fran") # se agrega en la lista el nombre fran
print(nombres)

for nombre in nombres:
    print(nombre)

nombres.append("eva")#
print(nombres)

nombres.remove("beto")# remover de la lista el nombre beto
print(nombres)

nombres.insert(2, "gabriela") #inserta un nombre dentro de la lista y corre un nombre para que gabriela ocupe la pocicion 2 en la lista
print(nombres)

nombres.sort()
print(nombres)

nombres.reverse()
print(nombres)

print("eva" in nombres)# pregunta se el nombre eva esta en la lista

nombres.clear() #linpia el listado.
print(nombres)

numeros =[1,2,3,4]
print(min(numeros))

for numero in numeros:
    if numero < 2:
        print("menor")

lista =[n for n in numeros if n<3]
print(lista)



del nombres #elimina la lista de memoria


