'''
Задание №7.

Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
'''
import json

result = []

with open('text_7.txt', encoding = 'utf-8') as f_obj:
    firm_info = f_obj.readlines()

firm_info_list = [el.split(' ') for el in firm_info]

firm_profit_dict = {}
profit_list = []
losses_firm = {}

for elem in firm_info_list:
    firm_info_dict = {}
    key_firm = [elem[0]]
    val_profit = int(elem[2]) - int(elem[3])
    if val_profit < 0:
        firm_info_dict = firm_info_dict.fromkeys(key_firm, val_profit)
        losses_firm.update(firm_info_dict)
    else:
        firm_info_dict = firm_info_dict.fromkeys(key_firm, val_profit)
        firm_profit_dict.update(firm_info_dict)
        profit_list.append(val_profit)

aver_profit = {'average_profit': sum(profit_list) / len(profit_list)}
losses_dict = {'loses': losses_firm}
result.append(firm_profit_dict)
result.append(aver_profit)
result.append(losses_dict)

with open('text_7.json', 'w', encoding = 'utf-8') as f:
    json.dump(result, f, ensure_ascii= False)
