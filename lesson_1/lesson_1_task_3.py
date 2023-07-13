# 3. Написать программу, которая генерирует в указанных пользователем границах:
# a. случайное целое число,
# b. случайное вещественное число,
# c. случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный
# символ от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ алфавита от 'a'
# до 'f' включительно.

# Изи

import numpy as np
import random

# Ввод границ диапазона
response1 = input('Введите нижнюю границу диапазона: ')
response2 = input('Введите верхнюю границу диапазона: ')

# Проверка ввода и обработка
if response1.isdigit() and response2.isdigit() and int(response1) < int(response2):
    data1 = int(response1)
    data2 = int(response2)
elif response1.replace(".", "").isdigit() and response2.replace(".", "").isdigit() and float(response1) < float(response2):
    data1 = float(response1)
    data2 = float(response2)
elif response1.isalpha() and response2.isalpha() and 97 <= ord(response1) <= 122 and 97 <= ord(response2) <= 122 and response1 < response2:
    data1 = response1
    data2 = response2
else:
    print("Неверный ввод. Введите верное значение.")
    exit()

# Генерация случайного числа
if isinstance(data1, float):
    random_el = random.uniform(data1, data2)
elif isinstance(data1, int):
    random_el = int(np.random.randint(data1, data2, 1))
elif isinstance(data1, str):
    random_el = chr(int(np.random.randint(ord(data1), ord(data2), 1)))

print(random_el)


# Хард

# boundaries = ['нижнюю границу диапазона', 'верхнюю границу диапазона']
# data = []
#
# # Цикл для ввода значений границ диапазона
# for i in boundaries:
#     while True:
#         response = input(f'Введите {i}: ')
#         try:
#             # Проверка ввода и обработка для числовых значений
#             if response.isdigit() and (data == [] or isinstance(data[0], int)) and (data == [] or data[0] < int(response)):
#                 data.append(int(response))
#                 break
#             # Проверка ввода и обработка для числовых значений с плавающей точкой
#             elif (not response.isalpha() and not response.isdigit()) and (data == [] or isinstance(data[0], float)) \
#                     and (data == [] or data[0] < float(response)):
#                 data.append(float(response))
#                 break
#             # Проверка ввода и обработка для буквенных значений
#             elif 97 <= ord(response) <= 122 and (data == [] or isinstance(data[0], str)) and (data == [] or data[0] < response):
#                 data.append(response)
#                 break
#             else:
#                 print("Неверный ввод. Введите верное значение.")
#         except TypeError:
#             print("Неверный ввод. Введите верное значение.")
#
# # Генерация случайного числа в указанном диапазоне
# if isinstance(data[0], float):
#     random_el = random.uniform(data[0], data[1])
# elif isinstance(data[0], int):
#     random_el = int(np.random.randint(data[0], data[1], 1))
# elif isinstance(data[0], str):
#     random_el = chr(int(np.random.randint(ord(data[0]), ord(data[1]), 1)))
#
# print(random_el)






