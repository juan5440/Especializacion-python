class Empleado:
    def __init__(self, nombres):
        self.nombre = nombres
    def calcular_sueldo(self):
        """
        empleado -> sueldo base
        empleado por comision -> ventas * comision
        empleados por hora -> valor * horas_trabajadas
        """
        return 1000

class EmpleadoPorComision(Empleado):
    def __init__(self, nombres, ventas, comision):
        super().__init__(nombres)
        self.ventas = ventas
        self.ventas = ventas
        self.comision = comision
    def calcular_sueldo(self): # lo sobre escribe
        return self.ventas*self.comision

class EmpleadoPorHora(Empleado):
    def __init__(self, nombres, horas, valor, he):
        super().__init__(nombres)
        self.horas=horas
        self.valor = valor
        self.he = he
    def calcular_sueldo(self):  # lo sobre escribe
        return self.horas*self.valor+self.he*self.valor*2