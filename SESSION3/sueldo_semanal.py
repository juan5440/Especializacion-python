nombre = input("Digite el nombre: ")
dui = input("Digite DUI: ")
ht = int(input("Digite las horas trabajadas: "))

sueldo = 0
if ht<=40:
    sueldo = ht*10
else:
    he = ht - 40
    sueldo = 400+he*20
print(f"Nombre: {nombre}\nDUI: {dui}\nSueldo a pagar: $ {sueldo:.2f}")