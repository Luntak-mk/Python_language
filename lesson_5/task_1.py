'''
Задание №1.
Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
'''

with open('text_1.txt', 'w', encoding = 'utf-8') as f:
    text_list = []
    text = None
    while True:
        text = input('Введите текст для записи в файл, чтобы перестать нажмите Enter: ')
        if text == '':
            break
        else:
            text_list.append(text)
    f.write('\n'.join(text_list))