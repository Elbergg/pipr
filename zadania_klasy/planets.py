import math
class Planet:
    
    def __init__(self, x, y, z, name=""):
        self._x = int(x)
        self._y = int(y)
        self._z = int(z)
        self._name = name


    def name(self):
        return self._name
    
    def x(self):
        return self._x


    def y(self):
        return self._y


    def z(self):
        return self._z


    def __str__(self):
        return f'Planet {self._name} has coordinates {self._x}, {self._y}, {self._z}'


    def distance(self, planet2):
        distance = math.sqrt((self._x - planet2._x)**2 + (self._y - planet2._y)**2 + (self._z - planet2._z)**2)
        return distance

 