class Car:
    # atributes
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # methods
    def go(self):
        return f'{self.name} Паехали'

    def stop(self):
        return f'{self.name} Приехали'

    def turn_right(self):
        return f'{self.name} Повернули на право'

    def turn_left(self):
        return f'{self.name} Повернули на лево'

    def show_speed(self):
        return f'Текущая скорость {self.name} - {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость городской машины {self.name} - {self.speed}')

        if self.speed > 40:
            return f'Скорость {self.name} выше чем должна быть у городской машины'
        else:
            return f'Скорость {self.name} нормальная для городской машины'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'скорость рабочей машины {self.name} это {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name} выше чем должно быть у раб машины'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} Полицейская машины'
        else:
            return f'{self.name} Не полицейская машина'


audi = SportCar(100, 'Red', 'Audi', False)
oka = TownCar(30, 'White', 'Oka', False)
lada = WorkCar(70, 'Rose', 'Lada', True)
ford = PoliceCar(110, 'Blue',  'Ford', True)
print(lada.turn_left())
print(f'Когда {oka.turn_right()}, Когда {audi.stop()}')
print(f'{lada.go()} Со скоростью как {lada.show_speed()}')
print(f'{lada.name} - {lada.color}')
print(f' {audi.name} Полицейская машина? {audi.is_police}')
print(f' {lada.name}  Полицейская машина? {lada.is_police}')
print(audi.show_speed())
print(oka.show_speed())
print(ford.police())
print(ford.show_speed())