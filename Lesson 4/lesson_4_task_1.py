# 1)Создайте класс ПЕРСОНА с абстрактными методами, позволяющими
# вывести на экран информацию о персоне, а также определить ее возраст (в
# текущем году). 
# 2)Создайте дочерние классы: АБИТУРИЕНТ (фамилия, дата
# рождения, факультет), СТУДЕНТ (фамилия, дата рождения, факультет, курс),
# ПРЕПОДАВАТЕЛЬ (фамилия, дата рождения, факультет, должность, стаж),
# со своими методами вывода информации на экран и определения возраста.
# 3)Создайте список из n персон, выведите полную информацию из базы на
# экран, а также организуйте поиск персон, чей возраст попадает в заданный
# диапазон.

import abc
from datetime import datetime

class PersonAbstract(abc.ABC):
    
    @abc.abstractmethod
    def view (self):
        print("Полная информация:")

    @abc.abstractmethod
    def current_age (self):
        pass
        


class Abiturient(PersonAbstract):
    
    def __init__(self, name, age_old, faculty):
        self.name = name
        self.age_old = age_old
        self.faculty = faculty

    def view(self):
        
        print(f'В системе есть следующая информация:')
        print(f'Фамилия: {self.name}')
        print(f'Дата рождения: {self.age_old}')
        print(f'Факультет: {self.faculty}')

    def current_age (self):
        today = datetime.today()
        date_1 = datetime.strptime(self.age_old, "%d/%m/%Y")

        current_age_of_person = today - date_1
        print(f'Сейчас ему/ей: {current_age_of_person}')

class Student(PersonAbstract):
    
    def __init__(self, name, age_old, faculty, kurs):
        self.name = name
        self.age_old = age_old
        self.faculty = faculty
        self.kurs = kurs

    def view(self):
        
        print(f'В системе есть следующая информация:')
        print(f'Фамилия: {self.name}')
        print(f'Дата рождения: {self.age_old}')
        print(f'Факультет: {self.faculty}')
        print(f'Курс: {self.kurs}')

    def current_age (self):
        pass


class Teacher(PersonAbstract):
    
    def __init__(self, name, age_old, faculty, position, years):
        self.name = name
        self.age_old = age_old
        self.faculty = faculty
        self.position = position
        self.years = years

    def view(self):
        
        print(f'В системе есть следующая информация:')
        print(f'Фамилия: {self.name}')
        print(f'Дата рождения: {self.age_old}')
        print(f'Факультет: {self.faculty}')
        print(f'Должность: {self.position}')
        print(f'Стаж лет: {self.years}')

    def current_age (self):
        pass


ABB1 = Abiturient('Kolesnikov', '14/05/2000', 'fea')

ABB1.view()
ABB1.current_age()