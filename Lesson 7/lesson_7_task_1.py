# 1) Написать контекстный менеджер для работы с SQLite DB.

import sqlite3

class MyContextManagerSQLite:

    def __init__(self, name_file):
        self.name_file = name_file
        self.conn = sqlite3.connect(self.name_file)

    def __enter__(self):
        return self.conn

    def write(self, request):
        cursor = self.conn.cursor()
        res = cursor.execute(request)

        print(res)


    def __exit__(self, exc_type, exc_val, exc_tb):
        
        self.conn.commit()

        if exc_type == AttributeError:
            print('Есть проблемы с атрибутом функции!')
            print(exc_tb)
        self.conn.close()
        return True




# with MyContextManagerSQLite(test.db) as db_file:
#     db_file.write()


# import sqlite3

# conn = sqlite3.connect('cars.db')

# cursor = conn.cursor()


# res = cursor.execute("INSERT INTO cars ('price', 'make', 'model', 'num_of_wheels') VALUES (3000, 'BMW', 'e39', 4)")

# print(res)
# conn.commit()
# conn.close()