# Задание №3
# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
answer = input('Введите число n: ')
result = int(answer) + int(answer * 2) + int(answer * 3)
print(f'Найдем сумму числе (n + nn + nnn) {answer} + {answer * 2} + {answer * 3} = {result}.')