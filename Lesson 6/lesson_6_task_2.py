# 2) Создать свою структуру данных Словарь, которая поддерживает методы,
# get, items, keys, values. Так же перегрузить операцию сложения для
# словарей, которая возвращает новый расширенный объект.

class NewDict:


    def __init__(self, *args, **kwargs):
        self.struct = {}


    def __getitem__(self, key):
        return self.struct[key]


    def __setitem__(self, key, value):
        self.struct[key] = value


    def get(self, key):
        return self.struct[key]

    def items(self, value):
        for key, value in self.struct():
            print(key, value)

    def keys(self, index, value):
        for key, value in self.struct():
            print(key)
        

    def values(self, item):
        for _key, value in self.struct():
            print(value)

        
    def __str__(self):
        return str(self.struct)

    def __add__(self, other):
        self.struct += other
        return self.struct


my_list = NewDict()

