# 7. Определить, является ли год, который ввел пользователь, високосным или не високосным.

# Ввод года
year = int(input('Введите год: '))

# Проверка условия високосности года
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f'Данный год високосный')
else:
    print('Данный год не високосный')


