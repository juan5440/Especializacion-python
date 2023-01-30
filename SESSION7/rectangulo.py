from figura import Figura
from color import color

class Rectangulo(Figura, color):


    def __init__(self, inicio, privado, color, base, altura):
        super().__init__(inicio, privado)
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base*self.altura

    def calcular_perimetro(self):
        return (self.base+self.altura)*2

r1 = Rectangulo('este es inicio',20, 10, 30)
print(f'inicio: {r1.inicio}')
r1.mostrar_inicio()
#r1.__privado # no es accesible
print(f'el area es: {r1.calcular_area()}')
print(f'el primero es: {r1.calcular_perimetro()}')