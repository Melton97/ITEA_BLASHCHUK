# 3) Написать свой контекстный менеджер для работы с файлами.


class MyContextManager:

    def __init__(self, name_file, method):
        self.name_file = name_file
        self.method = method
        self.file_obj = open(name_file, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        
        if exc_type == AttributeError:
            print('Есть проблемы с атрибутом функции!')
            print(exc_tb)
        self.file_obj.close()
        return True




with MyContextManager('test.txt', 'w') as op_file:
    op_file.wat_funct('Privet!')