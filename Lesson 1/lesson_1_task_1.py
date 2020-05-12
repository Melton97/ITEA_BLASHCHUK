#Создать список из N элементов (от 0 до n с шагом 1)
#В этом списке вывести все четные значения


n = int(input())

my_list = []

for i in range(0, n+1, 1):
    my_list.append(i)

print(my_list)

for i in my_list:
    if i%2==0 :
        print(i)