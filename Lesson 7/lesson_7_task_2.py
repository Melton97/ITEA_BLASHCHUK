# 2) Создать базу данных студентов. У студента есть факультет, группа, оценки, номер студенческого билета. 
# Написать программу, с двумя ролями: Администратор, Пользователь. 
# Администратор может добавлять, изменять существующих студентов.
# Пользователь может получать список отличников, список всех
# студентов, искать студентов по по номеру студенческого, получать
# полную информацию о конкретном студенте (включая оценки, факультет)

import sqlite3

class Administrator():
    def __init__(self, admin_key):
        self.admin_key = admin_key

    def add_student(self):

        pass


    def update_student(self):

        pass



class User():
    
    def 


class MyContextManagerSQLite:


    def __init__(self, name_file):
        self.name_file = name_file


    def __enter__(self):
        self.conn = sqlite3.connect(self.name_file)
        return self.conn


    def __exit__(self, exc_type, exc_val, exc_tb):
        
        self.conn.commit()

        if exc_type:
            raise
        self.conn.close()
        return True


with MyContextManagerSQLite('students.db') as db_file:
    cursor = db_file.cursor()
    res = cursor.execute("INSERT INTO FACULTY ('id', 'name_faculty') VALUES (12, 'Факультет Информатики')")
    print(res)