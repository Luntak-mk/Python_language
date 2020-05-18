# Задание №1.
# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def division_func (arg_1, arg_2):
    """
    Производит деление двух чисел и возвращает результат.
    :param arg_1: Делимое. Тип данных float
    :param arg_2: Делитель. Тип данных float
    :return: Возврашает тип данных float с округлением до 2-х знаков.
    """
    try:
        round(arg_1 / arg_2, 2)
    except ZeroDivisionError:
        while arg_2 == 0:
            arg_2 = float(input('Делитель не может быть "0", пожалуйста введите число, кторое отлично от "0": '))
    return round(arg_1 / arg_2, 2)

num_1 = float(input('Введите делимое число: '))
num_2 = float(input('Введите число делитель: '))

print(division_func(num_1, num_2))