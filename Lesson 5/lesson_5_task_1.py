# Создать декоратор, который будет запускать функцию в отдельном потоке. 
# Декоратор должен принимать следующие аргументы:
# название потока, является ли поток демоном.

from threading import Thread
import time

def deco_thread(func):

    def wrapper(name_of_thread, daemon):

        name_of_thread = Thread(target = func, args = (name_of_thread), daemon = daemon )
        time.sleep(2)

    return wrapper

@deco_thread
def my_func(name_of_thread, daemon):
    
    with open("ITEA_Lessons/my_file_5_2", "w") as mf:
        mf.write("For a test in lesson 5, task 1")
    
    return name_of_thread, daemon

my_func('gg', False)

    
