#un diccionario cada elemanto es un apar llave:valor
# nombre:alicia

diccionario ={
    "usuario":"alicia",
    "correo":"alicia@gmail.com",
    "token":"ffrfrgtgrthhuytjfdfggsffd",
}
print(diccionario)
#print(diccionario["usuario"])
#print(diccionario["correo"])
#print(diccionario["token"])

# for valores in diccionario.values():
#     print("valor")

# for clave in diccionario.keys():
#     print(clave)

diccionario["usuario"] = 'alicia.diaz'
diccionario['telefono'] ='777777'
for clave, valor in diccionario.items():
    print(f"Laclave es: {clave}, valor: {valor}")

print("usuario" in diccionario)
diccionario.clear()
print(diccionario)

del diccionario

print("hola'mundo'", 'hola"mundo"', 'hola \'mundo\'')