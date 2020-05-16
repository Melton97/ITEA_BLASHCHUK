# Создать декоратор с аргументами.
# Который будет вызывать функцию, определенное кол-во раз, 
# будет выводить кол-во времени затраченного на выполнение данной функции и ее название.
import random
import time

def my_decorator(func):

    def wrapper(val2):
        start_time = time.time()

        for i in range(val2):
            result = func(val2)
            print (result)
        my_time = time.time() - start_time
        print(f'Время выполнения программы {func.__name__}: {my_time}')
        return result 
        
    return wrapper


@my_decorator
def my_func(val2):
   return random.randint(1, val2)
   

my_func(100)