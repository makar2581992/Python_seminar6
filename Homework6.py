# Решение, которое было:

# 1 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# from random import randint
# list = []
# for i in range(6):
#    list.append(randint(0, 10))
# print(list)
# total = 0
# for i in range(len(list)):
#    if i%2 != 0:  
#        total += list[i]
# print(total)      

# Решение, которое стало:

# list = [input('Введите элемент: ') for i in range(int(input('Введите кол-вл элементов: ')))]
# list2 = []
# count = 0
# for count, i in enumerate(list):
#    if count % 2 == 1:
#         list2.append(i)
# print(list5)        
# print(list2)





# Решение, которое было:

# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# text = input("Введите текст через пробел:")
# print(f"Введенный текст: {text}")
# find_text = "абв"
# lst = [i for i in text.split() if find_text not in i]
# print(f'Результат: {" ".join(lst)}')



# Решение, которое стало:

# list = (filter(lambda txt: not 'абв' in txt, 'Я неабв знаю какабв что вы сделалиабв делали прошлым летом'.split()))
# print(f'Результат: {" ".join(list)}')



# Решение, которое было:

# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# list = [input('Введите элемент: ') for i in range(int(input('Введите количество элементов: ')))]
# print(f"Список: {list}")
# new_list = []
# [new_list.append(i) for i in list if i not in new_list]
# print(f"Неповторяющиеся элементы: {new_list}")


# Решение, которое стало:

#list = [2, 5, 6, 6, 5, 3, 2, 1, 8]
#print(tuple(filter(lambda x: list.count(x) == 1, list)))

