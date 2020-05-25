'''
Задание №4.
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно
данные. При этом английские числительные должны заменяться на русские. Новый блок строк
должен записываться в новый текстовый файл.
'''
with open('text_4.txt', encoding = 'utf-8') as f_obj:
    content = f_obj.readlines()

elem_list = [el.split(' ') for el in content]
new_content = []
for elem in elem_list:
    if elem[0] == 'One':
        elem[0] = 'Один'
    elif elem[0] == 'Two':
        elem[0] = 'Два'
    elif elem[0] == 'Three':
        elem[0] = 'Три'
    else:
        elem[0] = 'Четыри'
    new_content.append(' '.join(elem))

with open('new_text_4.txt', 'w', encoding = 'utf-8') as f:
    f.writelines(new_content)

