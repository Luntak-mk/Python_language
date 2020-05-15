# Задание №6.
# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
structure = []
number = int(input('Введите количество товаров: '))

for j in range(number):
    my_dict = {'название': None, 'цена': None, 'количество': None, 'ед': None}
    product = []
    product.append(j + 1)
    for i in my_dict.keys():
        val = input(f'Введите {i} товара №{j+1}: ')
        if i == 'цена' or i == 'количество':
            my_dict[i] = int(val)
        else:
            my_dict[i] = val
    product.append(my_dict)
    structure.append(tuple(product))
print(f'Так выглядит наша структура данных: \n{structure}')

# Необходимо собрать аналитику о товарах. Реализовать словарь,
# в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.
analytics = {'название': None, 'цена': None, 'количество': None, 'ед': None}
name = []
price = []
quantity = []
unit = []
elem_position = 0

while elem_position < number:
    for key_structure in structure[elem_position][1]:
        if key_structure == 'название':
            name.append(structure[elem_position][1][key_structure])
        elif key_structure == 'цена':
            price.append(structure[elem_position][1][key_structure])
        elif key_structure == 'количество':
            quantity.append(structure[elem_position][1][key_structure])
        else:
            unit.append(structure[elem_position][1][key_structure])
    elem_position += 1

for key in analytics:
     if key == 'название':
         analytics[key] = name
     elif key == 'цена':
         analytics[key] = price
     elif key == 'количество':
         analytics[key] = quantity
     else:
         analytics[key] = unit
print(f'\nТак выглядит наша аналитика товаров: \n{analytics}')