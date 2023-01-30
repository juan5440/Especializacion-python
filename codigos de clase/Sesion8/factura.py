class Factura:
    # aqui van las variables de clase
    cantidad_facturas = 0
    def __init__(self, cliente, total, nfactura):
        self.cliente = cliente
        self.total = total
        self.nfactura = nfactura
        Factura.cantidad_facturas += 1

    @classmethod
    def mostrar_cantidad_facturas(cls):
        print(f'la cantidad de facturas emitidas es {cls.cantidad_facturas}')

    @staticmethod
    def sumar_facturas(lista_facturas):
        total_facturas = 0
        for f in lista_facturas:
            total_facturas += f.total
        return total_facturas

f1 = Factura('alicia', 100, 1)
f2 = Factura('beto', 200, 2)
f3 = Factura('carlos', 300, 3)
Factura.mostrar_cantidad_facturas()
lista = [f1,f2,f3]
print(f'el total en facturas es {Factura.sumar_facturas(lista)}')
print(f1.cantidad_facturas, f2.cantidad_facturas, f3.cantidad_facturas)
print(Factura.cantidad_facturas)
print(f1.nfactura, f2.nfactura, f3.nfactura)