# valores por defoult en una funcion 
#valores opcionales, pueden ir o no ir

def calculo_desc(sueldo, isss=0.03, afp=0.0725):
    dsc = sueldo*isss + sueldo*afp
    return desc

descuentos = calculo_desc(800)
print(f"Los descuentos del isss y afp son: {descuentos}")

descuentos2 = calculo_desc(800, 0.04)
descuentos3 = calculo_desc(800, 0.04, 0.06)
descuentos4 = calculo_desc(800, afp=0.06)
descuentos5 = calculo_desc(800, isss=0.03)
descuentos6 = calculo_desc(800, afp=0.06, isss=0.03)

#argumentos variables con una lista
print("alicia", "berto", "carlos", 12 , True)

def listar_nombres(nombres):
    for nombre in nombres:
        print(nombre)

listar_nombres("alicia", "beto", "carlos", 12, True, "eva")

#argumentos variables clave:valor (diccionario)

def listar_diccionarios(**terminos):
    for k, v in terminos.items():
        print(k, v)

listar_diccionarios(PK="primery key", FK="Foreing key", UQ="unique")