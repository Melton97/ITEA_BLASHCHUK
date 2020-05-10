# Создать класс точки, реализовать конструктор который 
# инициализирует 3 координаты (x, y, z). 
# Реализовать методы для получения и изменения каждой из координат.
# перегрузить для этого класса методы сложения, вычитания, деления, умножения.
# Перегрузить один любой унарный метод.

# Ожидаемый результат: умножаю точку с координатами 1, 2, 3 на другую точку 
# с такими же координатами , получаю результат 1, 4, 9

class Dot:

    def __init__(self, x, y, z):

        self._x = x
        self._y = y 
        self._z = z

    def get_x(self):
        return self._x
        
    def get_y(self):
        return self._y
        
    def get_z(self):
        return self._z

    def set_x(self, new_value):
        self._x = new_value    
        
    def set_y(self, new_value):
        self._y = new_value   
        
    def set_z(self, new_value):
        self._z = new_value

    def __add__(self, other):
        return self._x + other._x and self._y + other._y and self._z + other._z
    
    def __sub__(self, other):
        return self._x - other._x and self._y - other._y and self._z - other._z

    def __mul__(self, other):
        return self._x * other._x and self._y * other._y and self._z * other._z

    def __truediv__(self, other):
        return self._x / other._x and self._y / other._y and self._z / other._z


first_dot = Dot(1, 2, 3)
second_dot = Dot(1, 2, 3)



print(first_dot.__mul__(second_dot))

    