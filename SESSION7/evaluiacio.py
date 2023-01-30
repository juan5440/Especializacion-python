class Producto:
    def __init__(self, nombre_producto, precio, cantidad):
        self.producto = nombre_producto
        self.precio = precio
        self.cantidad = cantidad
    def mostrar_datos(self):
        print(
            f'Nombre de Producto : {self.producto}\n'
            f'Precio : {self.precio}\n'
            f'cantidad : {self.cantidad}\n'
        )
    def get_precio(self):
        return self.precio
    def set_precio(self, precio):
        self.precio = precio
    def get_producto(self):
        return self.producto
    def __str__(self):
        return self.producto

p = Producto('Azucar',1.50 ,  2)
#print(p)

class cliente:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def mostrar_cliente(self):
        print(
            f'Nombre : {self.nombre}\n'
            f'Edad : {self.edad}\n'
        )
    def __str__(self):
        return self.nombre

c = cliente('pepito', 20)

class factura_emitida(Producto,cliente):
    def __init__(self, n_factura, id_factura, fecha, c):
        self.factura = n_factura
        self.id = id_factura
        self.fecha = fecha
        self.c = c
    def mostrar_factura(self):
        print(
            f'Numero de factura : {self.factura}\n'
            f'Id de factura : {self.id}\n'
            f'Fecha : {self.fecha}\n'
            f'cliente : {self.c}\n'
        )

    def get_fecha(self):
        return self.fecha
    def __str__(self):
        return self.factura

f = factura_emitida(232, 1, "09/11/2021", f'{c.nombre}')

print(f"numero de factur es: {f.factura}")
print(f"nombre de cliente: {c.nombre}")
print(f"Producto: {p.producto}")
print(f"Fecha Hemitida: {f.get_fecha()}")