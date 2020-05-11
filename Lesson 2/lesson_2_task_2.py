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
        self.Total_value += self.value

    def plusser(self):
        Market.Total_value += self.value
        return Market.Total_value


Allo = Market('Allo', 400)
Citrus = Market('Citrus', 500)

Allo.plusser()
Citrus.plusser()  
print(Market.Total_value)






