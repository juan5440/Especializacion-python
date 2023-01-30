menu = "[1] Agregar Empleados\n"
menu += "[2] Mostrar el listado\n"
menu += "[#] Salir\n"

print(menu)
op = int(input("digite una opcion: "))

lista = []
while op == 1 or op == 2:
    if op == 1:
        nombre = input("Digite nombre: ")
        sueldo = float(input("Digite sueldo: "))
        e = {
            "nombre": nombre,
            "sueldo": sueldo,
        }
        lista.append(e)
    else:
        for e in lista:
            print("nombre:", e["nombre"])
            print("sueldo", e["sueldo"])
            print("**************************************************")

            input()
            print(menu)
            op = int(input("digite una opcion: "))
