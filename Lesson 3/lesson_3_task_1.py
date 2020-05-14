# Создать декоратор с аргументами.
# Который будет вызывать функцию, определенное кол-во раз, 
# будет выводить кол-во времени затраченного на выполнение данной функции и ее название.
import random
import time

def my_decorator(func):

    def wrapper(*args, **kwargs):
        start_time = time.time()
        for _i in range (1, 1000):
            result = func(*args, **kwargs)
            print (result)
        my_time = time.time()-start_time
        print(f'Время выполнения программы {func}: {my_time}')
        return result 
        
    return wrapper


@my_decorator
def my_func():
   return random.randint(1, 100)

my_func()