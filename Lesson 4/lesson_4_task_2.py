# 1)Создать подобие социальной сети. Описать классы, которые должны выполнять соответствующие функции (Предлагаю насследовать класс
# авторизации от класса регистрации). 
# 2)Добавить проверку на валидность пароля (содержание символов и цифр), проверка на уникальность  логина пользователя. 
# 3)Человек заходит, и имеет возможность зарегистрироваться(ввод логин, пароль, потдверждение пароля), далее входит в свою учетную запись. 
# 4)Добавить возможность выхода из учетной записи, и вход в новый аккаунт. 
# 5)Создать класс User, котоырй должен разделять роли обычного пользователя и администратора. 
# 6)При входе под обычным пользователем мы можем добавить новый пост, с определённым содержимим, так же пост должен содержать дату публикации. 
# 7)Под учётной записью администратора мы можем увидеть всех пользователей нашей системы, дату их регистрации, и их посты.
import datetime

class Registration:
    
    global_user_log = {}

    def __init__(self, user_name, login, password):
        self.user_name = user_name
        self.login = login
        self.password = password

    def Sign_Up(self):
        print("Привет, давай начнем регистрацию!")
        print("Проверьте правильность введенных данных:")
        print(f'Тебя зовут : {self.user_name}, твой логин: {self.login}, твой пароль: {self.password}')
        
        corr = input("Если данные для регистрации введены верно, нажмите Y, если нет то N: ")

        if corr == 'Y':
            Registration.global_user_log = {"user_name" : self.user_name, "login" : self.login, "password" : self.password, "date_registration" : datetime.time()}
            print("Регистрация прошла успешно, спасибо!")
     
        elif corr == 'N':
            print ("Измените данные при присвоении обьекта к классу Registration!")

        else : 
            print ("Вы ввели неправильное значение!", "\n", "Введите Y или N")


class Authorisation(Registration):
    
    def Sign_In(self):

        pass

    def Exit(self):
        pass

    def Change_Account(self):
        pass

class User:
    
    def Post(self):
        pass


input("")
Pavel = Registration('Pavel', 'pav', 'pav333')
Pavel.Sign_Up()
print(Registration.global_user_log)