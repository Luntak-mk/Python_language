# Задание №2.
# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
my_list = []
start_index = 0
end_index = 1
while True:
    elem = input('Введите ваше значение для добавления в список. Чтобы остановить добавление, введите "stop": ')
    if elem == 'stop':
        break
    my_list.append(elem)
print(f'Так выглядит наш список {my_list}')
if len(my_list) % 2 != 0:
    last_elem = my_list.pop()
    for i in range(0, len(my_list), 2):
        my_list[start_index], my_list[end_index] = my_list[end_index], my_list [start_index]
        start_index += 2
        end_index += 2
    my_list.append(last_elem)

else:
    for i in range(0, len(my_list), 2):
        my_list[start_index], my_list[end_index] = my_list[end_index], my_list [start_index]
        start_index += 2
        end_index += 2

print(f'Так выглядит наш список после изменения {my_list}')