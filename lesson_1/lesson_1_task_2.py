# 2. По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей
# через эти точки.

# Изи

# Ввод координат
x1 = float(input('Введите координату x1: '))
y1 = float(input('Введите координату y1: '))
x2 = float(input('Введите координату x2: '))
y2 = float(input('Введите координату y2: '))

# Вычисление наклона и свободного члена
k = (y2 - y1) / (x2 - x1)
b = y1 - k * x1

# Формирование уравнения прямой
equation = f"y = {k} * x + {b}"

# Вывод уравнения прямой
print("Уравнение прямой: ", equation)


# Хард

# # Создаем пустой список и лэйблы для цикла input()
# coordinates = []
# labels = ['x1', 'y1', 'x2', 'y2']
#
# # Инициируем цикл для ввода значений координат.
# for label in labels:
#     while True:
#         # Вылавливаем возможные ошибки при помощи try/except
#         try:
#             coordinate = float(input(f'Введите координату {label}: '))
#             coordinates.append(coordinate)
#             break
#         except ValueError:
#             print("Неверный ввод. Введите числовое значение.")
#
# x1, y1, x2, y2 = coordinates
#
# # Вычислить значение наклона (k):
# k = (y2 - y1) / (x2 - x1)
#
# # Вычислить значение свободного члена (b):
# b = y1 - k * x1
#
# # Формирование уравнения прямой
# equation = f"y = {k} * x + {b}"
#
# # Вывод уравнения прямой
# print("Уравнение прямой: ", equation)

