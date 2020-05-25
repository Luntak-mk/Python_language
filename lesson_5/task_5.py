'''
Задание №5.
Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить
ее на экран.
'''
from functools import reduce

numbers = ['5', '4', '2', '4', '7']

with open('text_5.txt', 'w+', encoding = 'utf-8') as f_obj:
    f_obj.write(' '.join(numbers))
    f_obj.seek(0)
    content = f_obj.readline()
content_list = content.split(' ')
sum_content_numbers = reduce(lambda x, y: int(x) + int(y), content_list)
print(sum_content_numbers)


