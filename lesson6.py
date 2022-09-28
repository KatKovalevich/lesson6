# задача 1

from time import sleep
class TrafficLight:
    def __init__(self, color):
        self._color = color
    def running(self):
        for key, value in self._color.items():
            sleep(value)
            print(key)
traf = TrafficLight(color={
    "Красный": 7,
    "Желтый": 2,
    "Зеленый": 10})
traf.running()


# задача 2

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 25
        self.height = 5

    def asphalt_mass(self):
        asphalt_mass = self._length * self._width * self.weight * self.height / 1000
        print(f'Для покрытия всего дорожного полотна требуется {round(asphalt_mass)} тонн асфальта')
r = Road(5000, 20)
r.asphalt_mass()


# задача 3

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
    def get_full_name(self):
        return self.name + ' ' + self.surname
    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

p = Position('Ivan', 'Ivanov', 'dir', '1000', '500')
print(p.get_full_name(), p.get_total_income())

# задача 4

class Car:
    def __init__(speed, color, name, is_police = False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        if self.speed != 0:
            print('Машина едет')

    def stop(self):
        if self.speed == 0:
            print('Машина остановилась')

    def turn(self, side):
        if side == 1:
            print('Машина поворачивает влево')
        if side == 2:
            print('Машина поворачивает вправо')

    def show_speed(self, speed):
        self.speed = speed
        print(f'Скорость движения {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Вы превысили скорость!')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Вы превысили скорость!')

class PoliceCar(Car):
    pass

# задача 5

class Stationery:
    def __init__(self, title):
        self.title = title

        def draw(self):
            return f'Запуск отрисовки'

class Pen(Stationery):
    def draw(self):
        return f'Запуск отрисовки ручкой'

class Pencil(Stationery):
    def draw(self):
        return f'Запуск отрисовки карандашом'

class Handle(Stationery):
    def draw(self):
        return f'Запуск отрисовки маркером'






