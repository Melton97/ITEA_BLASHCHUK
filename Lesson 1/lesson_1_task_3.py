# Напишите программу, которая выводит на экран числа от 1 до 100.
# При этом вместо чисел, кратных трем, программа должна выводить слово Fizz,
# а вместо чисел, кратных пяти - слово Buzz.
# Если число кратно пятнадцати, то программа должна выводить слово FizzBuzz 

my_list = []

for i in range(1, 101, 1):
    my_list.append(i)

for i in my_list:
    
    if i%3 is not 0 and i%5 is not 0 and i%15 is not 0:
        print (i)
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    elif i%15==0:
        print('FizzBuzz')
