# Создать класс структуры данных Стек, Очередь.
# Создать класс комплексного числа и реализовать для него 
# арифметические операции.

from collections import deque
import random

class MyStack:

    def __init__(self, new_list):
        self.new_stack = []

    def push(self, val):
        return self.new_stack.append(val)

    def pop(self):
        return self.new_stack.pop()

class MyRow:

    def __init__(self, new_row):
        self.new_row = new_row.deque()

    def queue(self, val):
        return self.new_row.insert(0, val)

    def deque(self):
        return self.new_row.pop()


class MyComplex:
    
    def __init__(self, re, imag):
        self.re = re
        self.imag = imag


    def __add__(self, other):
        new_compl2 = MyComplex(self.re + other.re, self.imag + other.imag)
        return new_compl2

    def __sub__(self, other):
        new_compl2 = MyComplex(self.re - other.re, self.imag - other.imag)
        return new_compl2

    def __mul__(self, other):
        new_compl2 = MyComplex((self.re*other.re) - (self.imag*other.imag), (self.imag*other.re)+(self.re*other.imag))
        return new_compl2

    def __truediv__(self, other):
        new_compl2 = MyComplex((self.re*other.re + self.imag*other.imag)/(other.re**2 + other.imag**2), (self.imag*other.re - self.re*other.imag)/(other.re**2 + other.imag**2))
        return new_compl2

    def __str__(self):
        return f'({self.re}, {self.imag}j)'
    

my_compl1 = MyComplex(10, 100)

my_compl2 = MyComplex(20, 20)

print(my_compl1 * my_compl2)
print(my_compl1 / my_compl2)






