'''
== Лото ==

Правила игры в лото.

Игра ведется с помощью спе циальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
    Если цифра есть на карточке - она зачеркивается и игра продолжается.
    Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
    Если цифра есть на карточке - игрок проигрывает и игра завершается.
    Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
'''

from random import randint, shuffle, randrange

class Card:
    def __init__(self, name):
        self.result = [name, Card._get_card()]

    def __getitem__(self, index):
        return self.result[index]
    @staticmethod
    def _get_card():
        card = [[], [], []]
        for i in range(len(card)):
            j = 0
            while j < 5 :
                el = randint(1, 90)
                if card[0].count(el) == 0 and card[1].count(el) == 0 and card[2].count(el) == 0:
                    card[i].append(el)
                    j += 1
            card[i] = sorted(card[i])

            for _ in range(4):
                card[i].insert(randrange(6), ' ')
        return card

    def __str__(self):
        if self.result[0] == 'Игрок':
            text_card = '-' * 14 + self.result[0] + '-' * 15 + '\n'
            for i in range(len(self.result[1])):
                text_card += "\t".join(map(str, self.result[1][i])) + '\n'
            text_card += '-' * 34
        if self.result[0] == 'Компьютер':
            text_card = '-' * 12 + self.result[0] + '-' * 13 + '\n'
            for i in range(len(self.result[1])):
                text_card += "\t".join(map(str, self.result[1][i])) + '\n'
            text_card += '-' * 34
        return text_card

class GameLoto:
    def __init__(self, human_plaeyr, comuter_player):
        self._card_1 = human_plaeyr[1]
        self._card_2 = comuter_player[1]
        self.name_1 = human_plaeyr[0]
        self.name_2 = comuter_player[0]


    def start(self):
        def get_result(card_1, card_2, keg):
            cours_next = 0
            win = 0
            lose = 0
            for el_1 in card_1:
                if el_1.count(keg) == 1:
                    cours_next = el_1.count(keg)
                    el_1[el_1.index(keg)] = '-'
                win += el_1.count('-')
            for el_2 in card_2:
                if el_2.count(keg) == 1:
                    el_2[el_2.index(keg)] = '-'
                lose += el_2.count('-')

            if cours_next != 1 and answer == 'y':
                return '-=GAME OVER=-'

            elif cours_next == 1 and answer == 'n':
                return '-=GAME OVER=-'

            elif get_draw (card_1, card_2) == '-=DRAW=-':
                return '-=DRAW=-'

            elif win == 15:
                return '-=YOU WIN=-'

            elif lose == 15:
                return '-=GAME OVER=-'

        def get_draw(card_1, card_2):
            new_list_1 = []
            new_list_2 = []
            for i in range(len(card_1)):
                for elem in card_1[i]:
                    if str (elem).isdigit () == True :
                        new_list_1.append(elem)
            for i in range(len(card_2)):
                for elem in card_2[i]:
                    if str(elem).isdigit () == True :
                        new_list_2.append(elem)
            new_list_1.sort()
            new_list_2.sort()
            if new_list_1 == new_list_2:
                return '-=DRAW=-'

        def text(par, card):
            if par == 'Игрок':
                text_card = '-' * 14 + par + '-' * 15 + '\n'
                for i in range(len(card)):
                    text_card += "\t".join(map(str, card[i])) + '\n'
                text_card += '-' * 34
            if par == 'Компьютер':
                text_card = '-' * 12 + par + '-' * 13 + '\n'
                for i in range(len(card)):
                    text_card += "\t".join(map(str, card[i])) + '\n'
                text_card += '-' * 34
            return text_card

        bag_with_keg = [el for el in range(1, 91)]
        i = 0

        while i < 90:
            shuffle(bag_with_keg)
            keg = bag_with_keg.pop()
            print(f'Новый бачонок: {keg} (Осталось {len(bag_with_keg)})')
            print(text(self.name_1, self._card_1))
            print(text(self.name_2, self._card_2))
            answer = (input('Зачеркнуть цифру? (y/n): ')).lower()
            while True:
                if answer == 'y':
                    break
                elif answer == 'n':
                    break
                else:
                    answer = input('Нужно ввести верный символ (y/n): ')
            result = get_result(self._card_1, self._card_2, keg)
            if result == '-=GAME OVER=-':
                print('-=GAME OVER=-')
                break
            elif result == '-=DRAW=-':
                print('-=DRAW=-')
                break
            elif result == '-=YOU WIN=-':
                print('-=YOU WIN=-')
                break
            i += 1

human_player = Card('Игрок')
computer_player = Card('Компьютер')

game = GameLoto(human_player, computer_player)
game.start()