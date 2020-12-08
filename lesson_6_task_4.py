class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        return f'{self.name} начала движение'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f'Скорость автомобиля {self.name} составляет {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость автомобиля {self.name} составляет {self.speed}')

        if self.speed > 40:
            return f' {self.name} превышает скоростной лимит'
        else:
            return f' {self.name} не превышает скоростной лимит'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость автомобиля {self.name} составяет {self.speed}')

        if self.speed > 60:
            return f' {self.name} превышает скоростной лимит'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police is True:
            return f'{self.name} автомобиль полиции'
        else:
            return f'{self.name} не автомобиль полиции'


my_sport_car = SportCar(190, 'Синий', 'Nissan Skyline', False)
my_town_car = TownCar(50, 'Розовый', 'Kia Rio', False)
my_work_car = WorkCar(50, 'Черный', 'Camry', False)
my_police_car = PoliceCar(100, 'Белый',  'Patrol', True)
print(my_work_car.turn_left())
print(my_town_car.show_speed())
print(my_sport_car.show_speed())
print(my_town_car.show_speed())
print(my_police_car.police())
print(my_police_car.show_speed())
print(my_sport_car.color)
print(my_work_car.name)
