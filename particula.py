
class Particula:
    def __init__(self, 
                id=0, origen_x=0, 
                origen_y=0, destino_x=0, destino_y=0,
                velocidad=0, red=0, green=0, blue=0):
        self.__id = id
        self.__origen_x = origen_x
        self.__origen_y = origen_y
        self.__destino_x = destino_x
        self.__destino_y = destino_y
        self.__velocidad = velocidad
        self.__red = red
        self.__green = green
        self.__blue = blue
        
            
    def __str__(self):
        return (
            'Id: ' + self.__id + '\n' +
            'Origen_x: ' + str(self.__origen_x) + '\n' +
            'Origen_y: ' + str(self.__origen_y) + '\n' +
            'Destino_x: ' + str(self.__destino_x) + '\n' + 
            'Destino_y: ' + str(self.__destino_y) + '\n' +
            'Velocidad: ' + self.__velocidad + '\n' +
            'Red: ' + str(self.__red) + '\n' +
            'Green: ' + str(self.__green) + '\n' +
            'Blue: ' + str(self.__blue) + '\n' 
        )

    def to_dict(self):
        return{
            "Id": self.__id,
            "Origen_x": self.__origen_x,
            "Origen_y": self.__origen_y,
            "Destino_x": self.__destino_x,
            "Destino_y": self.__destino_y,
            "Velocidad": self.__velocidad,
            "Red": self.__red,
            "Green": self.__green,
            "Blue": self.__blue        }
#l01 = Libro(id=1, origen_x=2, origen_y=3, destino_x=4, destino_y=5, velocidad=6,
#red=7, green=8, blue=9)
#print (l01)
#l02 = Libro("9", "10", "11", "12", "13", "14", "15", "16", "17")
#print (l02)