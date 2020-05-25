'''
Задание №3.
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
'''
with open('text_3.txt', encoding = 'utf-8') as f_obj:
    content = f_obj.readlines()
date_employees_list = [el.split(' ') for el in content]
sum_salary = 0
for el in date_employees_list:
    if float(el[1]) < 20000:
        print(el[0])
    sum_salary += float(el[1])
average_income = sum_salary / len(date_employees_list)
print('Средняя величина дохода сотрудников:', round(average_income, 2))
