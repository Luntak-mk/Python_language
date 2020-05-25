'''
Задание №2.
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
подсчет количества строк, количества слов в каждой строке.
'''

with open('text_2.txt', encoding = 'utf-8') as f:
    content = f.readlines()
print(f'В файле всего {len(content)} строк.')
length = 1
number_words = 0
for el in content:
    number_words = len(el.split(' '))
    print(f'В строке {length} {number_words} слов')
    length += 1