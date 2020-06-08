# 2) Создать базу данных студентов. У студента есть факультет, группа, оценки, номер студенческого билета. 
# Написать программу, с двумя ролями: Администратор, Пользователь. 
# Администратор может добавлять, изменять существующих студентов.
# Пользователь может получать список отличников, список всех
# студентов, искать студентов по по номеру студенческого, получать
# полную информацию о конкретном студенте (включая оценки, факультет)

import sqlite3

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



class Administrator():
    def __init__(self, admin_key):
        self.admin_key = admin_key
        if admin_key == 'adminion':
            print("Ок, вы Админ!")


    def add_student(self, stud_card, first_name, second_name, faculty, group):
        params = [stud_card, first_name, second_name, faculty, group]
        with MyContextManagerSQLite('students.db') as db_file:
            cursor = db_file.cursor()
            res = cursor.execute("INSERT INTO STUDENTS_FULL ('stud_card', 'first_name', 'second_name', 'faculty', 'group') VALUES (?, ?, ?, ?, ?)",
            params)
            print('Данные студента внесены в БД:', res)
        


    def update_student(self, stud_card, column, value):

        with MyContextManagerSQLite('students.db') as db_file:
            cursor = db_file.cursor()
            _res = cursor.execute(f"UPDATE STUDENTS_FULL SET {column} = {value} WHERE stud_card = {stud_card}")
            print('Данные студента изменены!')




class User():
    
    def __init__(self, stud_card):
        self.stud_card = stud_card
        t = (stud_card,)
        with MyContextManagerSQLite('students.db') as db_file:
            cursor = db_file.cursor()
            res = cursor.execute("SELECT first_name from STUDENTS_FULL WHERE stud_card=?", t)
            print(f"Привет {res.fetchall()}!")


    def best_students(self):
        with MyContextManagerSQLite('students.db') as db_file:
            cursor = db_file.cursor()
            res = cursor.execute("SELECT first_name, second_name from STUDENTS_FULL INNER JOIN GRADES ON GRADES.student_card = STUDENTS_FULL.stud_card where marks = 5")
            print(res.fetchall())


    def all_students(self):
        with MyContextManagerSQLite('students.db') as db_file:
            cursor = db_file.cursor()
            res = cursor.execute("SELECT * from STUDENTS_FULL")
            print(res.fetchall())


    def search_student_by_stud_id(self, id):
        t = (id, )
        with MyContextManagerSQLite('students.db') as db_file:
            cursor = db_file.cursor()
            res = cursor.execute("SELECT first_name, second_name from STUDENTS_FULL where stud_card = ?", t)
            print(res.fetchall())


    def view_info(self, id):
        t = (id, )
        with MyContextManagerSQLite('students.db') as db_file:
            cursor = db_file.cursor()

            res = cursor.execute("SELECT * from STUDENTS_FULL INNER JOIN GRADES ON GRADES.student_card = STUDENTS_FULL.stud_card INNER JOIN faculty ON FACULTY.id = STUDENTS_FULL.faculty WHERE stud_card = ?", t)
            print(res.fetchall())


me = User(11345)
# me.best_students()
# me.all_students()
# me.search_student_by_stud_id(11345)
me.view_info(11345)
