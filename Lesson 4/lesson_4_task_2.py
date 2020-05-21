# 1)Создать подобие социальной сети. Описать классы, которые должны выполнять соответствующие функции (Предлагаю насследовать класс
# авторизации от класса регистрации). 
# 2)Добавить проверку на валидность пароля (содержание символов и цифр), проверка на уникальность  логина пользователя. 
# 3)Человек заходит, и имеет возможность зарегистрироваться(ввод логин, пароль, потдверждение пароля), далее входит в свою учетную запись. 
# 4)Добавить возможность выхода из учетной записи, и вход в новый аккаунт. 
# 5)Создать класс User, котоырй должен разделять роли обычного пользователя и администратора. 
# 6)При входе под обычным пользователем мы можем добавить новый пост, с определённым содержимим, так же пост должен содержать дату публикации. 
# 7)Под учётной записью администратора мы можем увидеть всех пользователей нашей системы, дату их регистрации, и их посты.

from datetime import datetime, date, time
import re

class Registration:
    
    global_user_log = {}

    def __init__(self, user_name, login, password):
        self.user_name = user_name
        self.login = login
        self.password = password

    def Sign_Up(self):

        print("Проверьте правильность введенных данных:", "\n")
        print(f'Тебя зовут : {self.user_name}, твой логин: {self.login}, твой пароль: {self.password}')
        
        corr = input("Если данные для регистрации введены верно, нажмите Y, если нет то N: ")

        if corr == 'Y' or 'y':
            Registration.global_user_log = {
                self.user_name: {
                    "login": self.login,
                    "password": self.password,
                    "date_registration": datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
                }
            }
            print("Регистрация прошла успешно, спасибо!")
     
        elif corr == 'N':
            print ("Измените данные при присвоении обьекта к классу Registration!")

        else : 
            print ("Вы ввели неправильное значение!", "\n", "Введите Y или N")


class Authorisation(Registration):
    
    posts = {}

    def __init__(self,user_name, login, password):
        self.user_name = user_name
        self.login = login
        self.password = password
    
    def Sign_In(self, login, password):
        if Registration.global_user_log[self.user_name]["login"] == self.login and Registration.global_user_log[self.user_name]["password"] == self.password:
            print(f"Вы ввошли в аккаунт под именем {self.user_name}")        
        else: pass
    def Exit(self):
        return print(f"Вы вышли с аккаунта {self.user_name}")

    def Change_Account(self,user_name, login, password):
        print("Вход в другой аккаунт:")
        if Registration.global_user_log[self.user_name]["login"] == self.login and Registration.global_user_log[self.user_name]["password"] == self.password:
            print(f"Вы ввошли в аккаунт под именем {self.user_name}")        
        else: pass
        

class User(Authorisation):
    
    def Simple_user_post(self):

        post = input("Введите текст поста который нужно опубликовать: \n")

        Authorisation.posts = {
            self.user_name: {
            "post": post,
            "post_date": datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
        }}

        print(Authorisation.posts)
        
    def Admin_user(self, key):

        if key == 'super_user':
            print("Вы ввошли в систему как администратор!")
        else: print("Вы ввели неправильный админ-ключ!")

    def view_global(self, key):
        if key == "super_user":
            print(f"Ниже список всех пользователей системы:\n {Registration.global_user_log}")
            print(f"А также их посты:\n {Authorisation.posts}")
                

def validate(password):
       while True:
           pswd = password
           if len(pswd) < 4:
               print("Пароль должен содержать не менее 4 символов!")
               return False
           elif re.search('[0-9]',pswd) is None:
               print("Пароль должен содержать хотя бы одну цифру!")
               return False
           elif re.search('[A-Z]',pswd) is None: 
               print("Пароль должен содержать хотя бы одну большую букву!")
               return False
           else:
               print("Проверка пароля пошла успешно!")
               return True

def validate_login(login):
    if login in Registration.global_user_log:
        return False
    else: return True


user_name = input("Введите ваше имя для регистрации:")

while True:
    login = input("Введите ваш логин для регистрации:")
    if validate_login(login) is False:
        print("Пользователь с таким логином уже существует!")
    else: 
        print("Проверка логина прошла успешно!")
        break

while True:
    password = input("Введите ваш пароль для регистрации:")
    if validate(password) is True:
        password_double = input("Подтвердите, пожалуйста, ваш пароль:")
        if password == password_double:
            print("Ок, форма регистрации завершена!", "\n")
            break

        else: print("Пароли не совпадают !\n")

    else: pass

admin_key = 'super_user'

user1 = Registration(user_name, login, password)
user1.Sign_Up()
print(Registration.global_user_log)

user1 = Authorisation(user_name, login, password)
user1.Sign_In(login, password)

user1.Exit()
user1.Change_Account(user_name, login, password)

user1 = User(user_name, login, password)
user1.Simple_user_post()
user1.Admin_user(admin_key)
user1.view_global("super_user")