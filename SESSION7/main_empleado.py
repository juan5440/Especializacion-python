from empleado import Empleado, EmpleadoPorComision, EmpleadoPorHora

e1 = Empleado('alicia')
e2 = EmpleadoPorComision('beto', 2000.00, 0.3)
e3 = EmpleadoPorHora('eva', 200,7,10)

print(f'el sueldo de {e1.nombre} es: {e1.calcular_sueldo()}')
print(f'el sueldo de {e2.nombre} es: {e2.calcular_sueldo()}')
print(f'el sueldo de {e3.nombre} es: {e3.calcular_sueldo()}')

if isinstance(e3, object):
    print("e3 es de tipo object")

if isinstance(e3, Empleado):
    print("e3 es de tipo Empleado")

if isinstance(e3, EmpleadoPorHora):
    print("e3 es de tipo Empleado Por Hora")