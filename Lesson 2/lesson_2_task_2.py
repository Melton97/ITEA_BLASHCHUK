# Создать класс магазина. Конструктор должен инициализировать зачения:
# 'Название магазина', 'Количество проданных товаров'. 
# Реализовать методы обьекта, которые будут увеличивать кол-во проданных товаров, 
# и реализовать вывод значения переменной класса, которая будет хранить 
# общее кол-во товаров проданных всеми магазинами.

class Market:

    Total_value = 0

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def plusser(self, value):
        Market.Total_value += value


Allo = Market('Allo', 400)
Citrus = Market('Citrus', 500)

print(Allo.plusser())






