# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

# first_num, razn, col_num = int(input("первый элемент ")),int(input("разница ")),int(input("количество элементов "))
# print(f"ввод: {first_num}, {razn}, {col_num}")
# list = [first_num + (i - 1) * razn for i in range(1,col_num+1)]
# print(f"Вывод: {list}")

#  Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

import random
list_nums = random.sample(range(-10,10),20)
min_znach = int(input("введите минимальное значение: "))
max_znach = int(input("введите максимальное значение: "))
list_indx = []
print(list_nums)
for indx,nums in enumerate(list_nums):
    if nums>=min_znach and nums<=max_znach:
        list_indx.append(indx)
print(list_indx)