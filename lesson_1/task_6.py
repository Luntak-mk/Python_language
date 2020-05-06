# Задание №6
# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
a = int(input('Введите сколько вы пробегаете за 1 день километров: '))
b = int(input('Введите сколько вы хотите пробегать километров за день: '))
day = 1
print(f'{day}-й день: {a}')
while a < b:
    a *= 1.1
    day += 1
    print (f'{day}-й день: {round (a, 2)}')
print(f'На {day}-й день вы достигли вашего результата — пробегать не менее {b} километров за день, '
      f'увеличивая вашу дистанцию на 10% каждый день.')
