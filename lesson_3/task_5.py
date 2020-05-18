# Задание №5.
# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел
# к полученной ранее сумме и после этого завершить программу.

all_elem_sum = 0
attempt = 0

while True:
    if attempt == 0:
        numbers = input('Введите числа через пробел: ')
    else:
        numbers = input('Введите числа через пробел и '
                        'если хотите завершить введите символ "q" сразу или через пробел после введенных чисел: ')
    list_numbers = numbers.split(' ')
    i = 0
    shutdown = None
    if list_numbers[i] == 'q':
        break
    else:
        while i < len(list_numbers):
            if list_numbers[i] == 'q':
                shutdown = list_numbers.pop(i)
            else:
                list_numbers[i] = float(list_numbers[i])
                i += 1
        all_elem_sum += sum(list_numbers)
        if attempt == 0:
            print('Сумма чисел вашей строки', all_elem_sum)
        else:
            print(f'Сумма чисел вашей строки {float(sum(list_numbers))} и общая сумма всех ваших строк {all_elem_sum}')
    attempt += 1
    if shutdown == 'q':
        break