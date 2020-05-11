# Создать декоратор с аргументами.
# Который будет вызывать функцию, определенное кол-во раз, 
# будет выводить кол-во времени затраченного на выполнение данной функции и ее название.
import random

def my_decorator(func):

    def wrapper():
        i = 10
        result = i*func()
        print (result)
        return result
        

    return wrapper

@my_decorator
def my_func():

   return random.randint(1, 100)

my_func()