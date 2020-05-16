# Создать функцию, которая будет скачивать файл из интернета по ссылке, повесить на неё созданный декоратор. 
# Создать список из 10 ссылок, по которым будет происходить скачивание. 
# Создать список потоков, отдельный поток, на каждую из ссылок. 
# Каждый поток должен сигнализировать, о том, что, он начал работу и по какой
# ссылке он работает, так же должен сообщать когда скачивание закончится.

from threading import Thread
import time
import requests

def deco_thread(func):

    def wrapper(name_of_thread, daemon):

        pass

    return wrapper

#@deco_thread
def download_func():

    req = requests.get("https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/The_Kiss_-_Gustav_Klimt_-_Google_Cultural_Institute.jpg/1024px-The_Kiss_-_Gustav_Klimt_-_Google_Cultural_Institute.jpg")
    req.raise_for_status()
    with open('Kiss.jpg', 'wb') as fd:
        for chunk in req.iter_content(chunk_size=50000):
            print('Received a Chunk')
            fd.write(chunk)

with open("me", "w") as me:
    me.write("gg")
