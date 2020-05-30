# 1) Создать свою структуру данных Список, которая поддерживает
# индексацию. Методы pop, append, insert, remove, clear. Перегрузить
# операцию сложения для списков, которая возвращает новый расширенный
# объект.

class NewList:


    def __init__(self, *args):
        self.struct = []
        for item in args:
            self.struct.insert(0,item)
        self.struct.reverse()
        print(self.struct)


    def __getitem__(self, index):
        return self.struct[index]


    def __setitem__(self, index, value):
        self.struct[index] = value


    def pop(self):
        self.struct = self.struct[:len(self.struct)-1]

    def append(self, value):
        l = [value]
        self.struct = self.struct + l 

    def insert(self, index, value):
        self.struct[index] = value
        

    def remove(self, item):
        index = self.struct.index(item)
        self.struct = self.struct[:index] + self.struct[index+1:]


    def clear(self):
        self.struct = []
        
    def __str__(self):
        return str(self.struct)

    def __add__(self, other):
        self.struct += other
        return self.struct


my_list = NewList(1,2,3,4,5)

my_list.pop()
print(my_list)
my_list.append(10)
print(my_list)
my_list.insert(0, 100)
print(my_list)
my_list.remove(2)
print(my_list)

my_list_2 = NewList(1, 2, 3)
print(my_list + my_list_2)