# Задание №4.
# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

def my_func_variant_1(arg_1, arg_2):
    """
    Функция возводит arg_1 в степень arg_2, с помощью оператора **

    :param arg_1: Принимает действительное положительное число.
    :param arg_2: Принимает целое отрицательное число.
    :return: Возвращает результат
    """
    arg_1 ** arg_2
    return arg_1 ** arg_2

def my_func_variant_2(arg_1, arg_2):
    """
    Функция возводит arg_1 в степень arg_2, с помощью цикла.

    :param arg_1: Принимает действительное положительное число.
    :param arg_2: Принимает целое отрицательное число.
    :return: Возвращает результат
    """
    multiplication = 1
    i = 0
    while i != arg_2:
        multiplication *= arg_1
        i -= 1
    result = 1 / multiplication
    return result

num_1 = 2.5
num_2 = -2

# Вариант №1
print(my_func_variant_1(num_1, num_2))

# Вариант №2
print(my_func_variant_2(num_1, num_2))
