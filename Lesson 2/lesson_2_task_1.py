# Создать класс автомобиля. Описать общие атрибуты. 
# Создать классы легкового автомобиля и грузового.
# Описать в основном классе базовые атрибуты для автомобилей.
# Бдует плюсом если в классах наследниках переопределите методы базового класса.

class Car:

    description = 'The main class of cars'

    def __init__(self, wheels, motor, body):

        self.wheels = wheels
        self.motor = motor
        self.body = body

    def move(self):
        print('Lets mooovee !')

    def brake(self):
        print('Braking now !')

class LittleCar(Car):

    def move(self):
        print('Lessles move...')

class BigCar(Car):

    def brake(self):
        print('Lessles braking...')

BMW = Car(4, 4.4, 'f15')
BMW.move()
BMW.brake()

Audi = LittleCar(4, 4.0, 8)
Audi.move()

Kamaz = BigCar(10, 3.0, 10)
Kamaz.brake()