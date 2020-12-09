from .particula import Particula
import json

class Libreria:
    def __init__(self):
        self.__particulas = []
    
    def agregar_final(self, particula:Particula):
        self.__particulas.append(particula)

    def agregar_inicio(self, particula:Particula):
        self.__particulas.insert(0, particula)

    def mostrar(self):
        for particula in self.__particulas:
            print(particula)

    def __str__(self):
        return "".join(str(libro) + '\n'for libro in self.__particulas)

    def guardar(self, ubicacion):
        try:
            with open(ubicacion, 'w') as archivo:
                lista = [particula.to_dict() for particula in self.__particulas]
                print(lista)
                json.dump(lista, archivo, indent=5)
            return 1
        except:
            return 0
            
    def abrir(self, ubicacion):
        try:
            with open(ubicacion, 'r') as archivo:
                lista = json.load(archivo)
                self.__particulas = [Particula(**particula) for particula in lista]
            return 1
        except:
            return 0

#l01 = Particula(id=1, origen_x=2, origen_y=3, destino_x=4, destino_y=5, velocidad=6, red=7, green=8, blue=9)
#l02 = Particula("9", "10", "11", "12", "13", "14", "15", "16", "17")
#libreria = Libreria()
#libreria.agregar_final(l01)
#libreria.agregar_inicio(l02)
#libreria.agregar_inicio(l01)
#libreria.mostrar()