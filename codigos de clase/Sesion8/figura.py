class Figura:

    def __init__(self, inicio, privado):
        self.inicio = inicio
        self.__privado = privado

    def mostrar_inicio(self):
        print(self.inicio)