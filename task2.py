class Road:
    _length = None
    _width = None
    __asphalt = 25 #кг
    __depth = 0.05 #м

    def __init__(self, length, width):
        self._width = width
        self._length = length

    def calculate(self):
        return self._length * self._width * self.__asphalt * self.__depth


road = Road(length=4000, width=25)
print(road.calculate())