# Programa que calcule el impuesto sobre la renta a pagar basado en la tabla de retención del ISR
# (mensual) de SV. Pedir el sueldo por teclado. Considerar la tabla de retenciones siguiente:

sueldo = float(input("Digite el salario para cálculo del impuesto: "))
if sueldo<1000:
    isss = sueldo*0.03
else:
    isss = 1000*0.03

afp = sueldo*0.0725

sg = sueldo - isss - afp

if sg >= 0.01 and sg<=472:
    isr = 0
elif sg>=472.01 and sg<=895.24:
    isr = (sg-472)*0.1 + 17.67

if sg <= 895.24 and sg<=2038.24:
    isr=(895.24 - 472) * 0.10 + 17.67
else:
 if sg<= 2038.10:
    isr=(sg - 895.24) * 0.20 + 60
 else:
     isr = (sg- 2038.10) * 0.03 + 288.57

print(f"el resultado isr es: " + str(isr)) 
print(f"el resultado isss es: " + str(isss))
print(f"el resultado afp es: " + str(afp))
