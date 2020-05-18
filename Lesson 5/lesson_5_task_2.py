# Создать функцию, которая будет скачивать файл из интернета по ссылке, повесить на неё созданный декоратор. 
# Создать список из 10 ссылок, по которым будет происходить скачивание. 
# Создать список потоков, отдельный поток, на каждую из ссылок. 
# Каждый поток должен сигнализировать, о том, что, он начал работу и по какой
# ссылке он работает, так же должен сообщать когда скачивание закончится.

from threading import Thread
import time
import requests

def deco_thread(func):

    def wrapper(*args, **kwargs):
        
        name_of_thread = Thread(target = func, args = (), daemon = False)
        name_of_thread.start()

    return wrapper

#@deco_thread
def download_func(list):

    for i in list:
        req = requests.get(i)
        status = req.status_code
        if status == 200:
            with open(str(list.index(i)) +'Kiss.jpg', 'wb') as fd:
                fd.write(req.content)
        else : print("Не установлено соединение с изображением.")
    
    name_of_thread = "Simple_Thread"
    daemon = False
    return name_of_thread, daemon


url1 = 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/The_Kiss_-_Gustav_Klimt_-_Google_Cultural_Institute.jpg/1024px-The_Kiss_-_Gustav_Klimt_-_Google_Cultural_Institute.jpg'
url2 = 'https://www.annaorion.com.ua/wp-content/uploads/2016/05/%D0%9C%D0%BE%D0%BD%D0%B0-%D0%9B%D0%B8%D0%B7%D0%B0.jpg'
url3 = 'https://www.annaorion.com.ua/wp-content/uploads/2016/05/%D0%A0%D0%BE%D0%B6%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5-%D0%92%D0%B5%D0%BD%D0%B5%D1%80%D1%8B.jpg'
url4 = 'https://www.annaorion.com.ua/wp-content/uploads/2016/05/%D0%A1%D0%BE%D1%82%D0%B2%D0%BE%D1%80%D0%B5%D0%BD%D0%B8%D0%B5-%D0%90%D0%B4%D0%B0%D0%BC%D0%B0.jpg'
url5 = 'https://www.annaorion.com.ua/wp-content/uploads/2016/05/%D1%83%D1%82%D1%80%D0%BE-%D0%B2-%D1%81%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%BE%D0%BC-%D0%BB%D0%B5%D1%81%D1%83.jpg'
url6 = 'https://www.annaorion.com.ua/wp-content/uploads/2016/05/%D0%B4%D0%B5%D0%B2%D0%BE%D1%87%D0%BA%D0%B0-%D0%BD%D0%B0-%D1%88%D0%B0%D1%80%D0%B5.jpg'
url7 = 'https://www.annaorion.com.ua/wp-content/uploads/2016/04/%C2%AB%D0%9F%D0%BE%D1%81%D0%BB%D0%B5%D0%B4%D0%BD%D0%B8%D0%B9-%D0%B4%D0%B5%D0%BD%D1%8C-%D0%9F%D0%BE%D0%BC%D0%BF%D0%B5%D0%B8%C2%BB.jpg'
url8 = 'https://www.annaorion.com.ua/wp-content/uploads/2016/05/%D0%B7%D0%B2%D0%B5%D0%B7%D0%B4%D0%BD%D0%B0%D1%8F-%D0%BD%D0%BE%D1%87%D1%8C.jpg'
url9 = 'https://www.annaorion.com.ua/wp-content/uploads/2016/05/%D0%B4%D0%B5%D0%B2%D1%8F%D1%82%D1%8B%D0%B9-%D0%B2%D0%B0%D0%BB.jpg'
url10 = 'https://www.annaorion.com.ua/wp-content/uploads/2016/05/%D0%BF%D0%BE%D1%80%D1%82%D1%80%D0%B5%D1%82.jpg'

list_of_urls = [url2, url1, url3, url4, url5, url6, url7, url8, url9, url10]
download_func(list_of_urls)