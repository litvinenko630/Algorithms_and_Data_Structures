# 4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

# Изи

label1 = 'Введите первую букву: '  # Лейбл для ввода первой буквы
label2 = 'Введите вторую букву: '  # Лейбл для ввода второй буквы

letter1 = ord(input(label1))  # Ввод первой буквы и получение ее позиции в алфавите
letter2 = ord(input(label2))  # Ввод второй буквы и получение ее позиции в алфавите

print(f'Позиция первой буквы в алфавите {abs(96 - letter1)}')  # Вывод позиции первой буквы в алфавите
print(f'Позиция второй буквы в алфавите {abs(96 - letter2)}')  # Вывод позиции второй буквы в алфавите
print(f'Между буквами располагается {abs(letter1 - letter2)} буквы.')  # Вывод количества букв между введенными буквами


# Хард

# labels = ['Введите первую букву: ', 'Введите вторую букву: ']  # Список с лейблами для ввода букв
# letters = []  # Пустой список для хранения позиций букв в алфавите
#
# for i in labels:
#     while True:
#         response = input(i)  # Ввод буквы
#         if response.isalpha():  # Проверка, является ли введенное значение буквой
#             position = ord(response)  # Получение позиции буквы в алфавите
#             if position > 122:  # Если позиция буквы больше 122, то это русская буква
#                 letters.append(position)  # Добавление позиции буквы в список
#                 print(f'Позиция буквы в алфавите {abs(1071 - position)}')  # Вывод позиции русской буквы в алфавите
#                 break
#             else:  # Если позиция буквы меньше или равна 122, то это английская буква
#                 letters.append(position)  # Добавление позиции буквы в список
#                 print(f'Позиция буквы в алфавите {abs(96 - position)}')  # Вывод позиции английской буквы в алфавите
#                 break
#         else:
#             print('Введите верное значение!')  # Вывод сообщения об ошибке, если введено неверное значение
#
# # Вывод количества букв между введенными буквами
# print(f'Между буквами располагается {abs(letters[0] - letters[1])} буквы.')










