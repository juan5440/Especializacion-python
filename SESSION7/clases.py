class Persona:
    def __init__(self, nombres, apellidos, edad, dui):
        self. nombres = nombres
        self._apellidos = apellidos
        self.__edad = edad
        self.__dui = dui
    def mostrar_datos(self):
        print(
            f'Nombre : {self.nombres}\n'
            f'Apellidos : {self._apellidos}\n'
            f'Edad : {self.__edad}\n'
            f'DUI : {self.__dui}\n'
        )
    def get_edad(self):
        return self.__edad
    def set_edad(self, edad):
        self.__edad = edad
    def get_dui(self):
        return self.__dui
    def __str__(self):
        return self.__dui

p = Persona('alicia','hernandez', 27, '123456677')
print(p)
print(f'el nombre es: {p.nombres}')
print(f'los apellidos son: {p._apellidos}')
#en python el ambiente protegido no se cumple
#print(f'la edad es: {p.__edad}')
#atributo privado, solo disponible dentro de la misma
print(f'la edad es: {p.get_edad()}')
p.nombres = "ALICIA"
p.set_edad(20)
p.mostrar_datos()
print('************************************************')
p_beto = Persona('beto', 'garcia', 25, '4356565676')
p_beto.mostrar_datos()
