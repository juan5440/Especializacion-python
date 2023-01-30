from figura import Figura
from color import Color

class Rectangulo(Figura, Color):
    
    def __init__(self, inicio, privado, color, base, altura):
        # una clase padre
        # super().__init__(inicio, privado)
        Figura.__init__(self, inicio, privado)
        Color.__init__(self, color)
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base*self.altura

    def calcular_perimetro(self):
        return (self.base+self.altura)*2

r1 = Rectangulo('este es inicio',20, 'verde', 10, 30)
print(f'inicio: {r1.inicio}')
print(f'color: {r1.color}')
r1.mostrar_inicio()
r1.mostrar_color()
# r1.__privado # no es accesible
print(f'el area es: {r1.calcular_area()}')
print(f'el perimetro es: {r1.calcular_perimetro()}')