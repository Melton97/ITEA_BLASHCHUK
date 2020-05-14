# Создать класс структуры данных Стек, Очередь.
# Создать класс комплексного числа и реализовать для него 
# арифметические операции.

from collections import deque
import random

class MyStack:

    def __init__(self, new_list):
        self.new_list = new_list

    def create_stack(self):
        new_stack = deque()
        for i in self.new_list:
            new_stack.append(i)   

        return new_stack
        
    def __str__(self):
        return deque()

class MyRow:

    def __init__(self, new_row):
        self.new_row = new_row

    def create_row(self):
        new_row = deque()
        for i in self.new_row:
            new_row.append(i)   

        return new_row     

    def pop(self):
        self.new_row.pop(0)

    def __str__(self):
        return deque()

class Complex:
    
    def __init__(self, re, imag):
        self.re = re
        self.imag = imag

    def create_compl(self):

        new_compl = complex(self.re, self.imag)
        return new_compl 

    def __add__(self, other):
        new_compl2 = complex(self.re + other.re, self.imag + other.imag)
        return new_compl2

    def __sub__(self, other):
        new_compl2 = complex(self.re - other.re, self.imag - other.imag)
        return new_compl2

    def __mul__(self, other):
        new_compl2 = complex((self.re*other.re) - (self.imag*other.imag), (self.imag*other.re)+(self.re*other.imag))
        return new_compl2

    def __truediv__(self, other):
        new_compl2 = complex( (self.re*other.re + self.imag*other.imag)/(other.re**2 + other.imag**2), (self.imag*other.re - self.re*other.imag)/(other.re**2 + other.imag**2) )
        return new_compl2

    def __str__(self):
        pass 
    

my_compl1 = Complex(10, 100)
my_compl2 = Complex(20, 20)

print(my_compl1 * my_compl2)
print(my_compl1 / my_compl2)

q = [ i for i in range(10)]
q = MyStack(q)
print(q.create_stack())
            
r = [ i for i in range(10)]
r = MyRow(r)
print(r.create_row())
r.pop()
print(r.create_row())





