# Задание №6.
# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().
def int_func(arg_1):
    """
    Данная функция преобразует первую букву слова в заглавную.

    :param arg_1: Принимает пользовательский ввод. Тип данных str.
    :return: Возвращает результат преобразования.
    """
    return arg_1.title()
i = 0
while i != 2:
    if i == 0:
        answer = input('Введите слово состоящее из маленьких латинских букв: ').lower()
        print(int_func(answer))
    else:
        answer = input('Введите слова состоящее из маленьких латинских букв разделенных пробелом: ').lower()
        print(int_func(answer))
    i += 1

