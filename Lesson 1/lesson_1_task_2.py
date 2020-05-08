# Создать словарь Страна: Столица. Создать Список стран
# Не все страны со списка должны сходиться с названиями стран со словаря
# С помощью оператора in проверить на вхождение элемента страны в словарь, 
# и если такой ключ действительно существует, вывести столицу

my_dict = {
    'Ukraine': 'Kyiv',
    'Russia': 'Moskow',
    'Belarus': 'Minsk',
    'Francia': 'Paris',
    'Germany': 'Berlin'
}

my_list = ['Ukraine', 'Russia', 'Belarus', 'Poland', 'Romonia', 'Italy']
print ('Совпадают страны с такими столицами:')
for i in my_list:
    if i in my_dict.keys():
        print (my_dict.get(i))