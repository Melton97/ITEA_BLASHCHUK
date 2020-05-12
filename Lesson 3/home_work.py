# Создать класс структуры данных Стек, Очередь.
# Создать класс комплексного числа и реализовать для него 
# арифметические операции.

from collections import deque
import random

class MyStack:

    def __init__(self, rand, val):
        self.rand = rand
        self.val = val

    def init_stack(self, rand, val):
        my_stack = deque()
        for i in range(1, self.val):
            a = random.randint(1, self.rand)
            my_stack.append(a)
        print (my_stack)


    
q = MyStack(100, 1000)

q.init_stack(100, 1000)
            




