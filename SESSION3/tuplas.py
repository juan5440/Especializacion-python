lenguajes = ("python","c++", "java", "php")
print(lenguajes)
#son de taño estatico
#este tipo de lista no se puede modificar sus elementos.
# solo permite funciones de lectura y no de escritura. 

print(len(lenguajes))
for lenguaje in lenguajes:
    print(lenguaje)

print(lenguajes.count("php"))

del lenguajes