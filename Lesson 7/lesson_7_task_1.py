# 1) Написать контекстный менеджер для работы с SQLite DB.

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


with MyContextManagerSQLite('students.db') as db_file:
    cursor = db_file.cursor()
    res = cursor.execute("INSERT INTO FACULTY ('id', 'name_faculty') VALUES (13, 'Факультет Метафизики')")
    print(res)

