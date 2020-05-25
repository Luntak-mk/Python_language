'''
Задание №6.
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный
предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их
количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по
нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''
with open('text_6.txt', encoding = 'utf-8') as f_obj:
    content = f_obj.readlines()
elem_list = [el.split(' ') for el in content]
lessons_list = []
hours_list = []
my_dict = {}
for el in elem_list:
    sum_hours_lesson = []
    for i in range(len(el)):
        if el[i] == el[0]:
            el[i] = el[i][:-1]
            lessons_list.append(el[i])
        else:
            for j in range(len(el[i])):
                if el[i][j] == '(':
                    el[i] = int(el[i][:j])
                    sum_hours_lesson.append(el[i])
                    break
    hours_list.append(sum(sum_hours_lesson))

my_dict = my_dict.fromkeys(lessons_list)
i = 0
for key in my_dict.keys():
    my_dict[key] = hours_list[i]
    i += 1
print(my_dict)

