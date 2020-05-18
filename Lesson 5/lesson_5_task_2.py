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
url2 = 'https://upload.wikimedia.org/wikipedia/commons/5/56/El_Greco_-_Saint_James_the_Younger_-_Google_Art_Project.jpg'
url3 = 'https://upload.wikimedia.org/wikipedia/commons/0/09/Alessandro_Magnasco_-_Praying_Monks_-_WGA13854.jpg'
url4 = 'https://upload.wikimedia.org/wikipedia/commons/9/98/Alessandro_Magnasco_-_Entombment_of_a_Soldier_-_WGA13858.jpg'
url5 = 'https://upload.wikimedia.org/wikipedia/commons/c/c1/Santo_Domingo_en_oraci%C3%B3n.jpg'
url6 = 'https://upload.wikimedia.org/wikipedia/commons/f/fa/Titian_-_Madonna_and_Child_with_Saints_%28detail%29_-_WGA22792.jpg'
url7 = 'https://upload.wikimedia.org/wikipedia/commons/4/4f/Giorgione%2C_Portrait_of_a_Young_Man_2.jpg'
url8 = 'https://upload.wikimedia.org/wikipedia/commons/f/ff/Pissarro_Self_portrait_DMA_1985-R-44.jpg'
url9 = 'https://upload.wikimedia.org/wikipedia/commons/e/ee/Schepkina-Kupernik_by_Repin.jpg'
url10 = 'https://upload.wikimedia.org/wikipedia/commons/9/9c/The_Death_of_Dido_%281781%29%3B_Joshua_Reynolds.jpg'

list_of_urls = [url2, url1, url3, url4, url5, url6, url7, url8, url9, url10]
download_func(list_of_urls)