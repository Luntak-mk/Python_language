'''
Задание №1.
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
'''
from random import randint
class Matrix:
    def __init__(self, matrix):
        self.matrix_list = matrix
    def __str__(self):
        el = ''
        for i in range(len(self.matrix_list)):
            el += "\t".join(map (str, self.matrix_list[i])) + '\n'
        return el
    def __add__(self, other):
        return Matrix([[self.matrix_list[j][i] + other.matrix_list[j][i] for i in range(len(self.matrix_list[0]))]
                       for j in range(len(self.matrix_list))])


my_matrix_1 = Matrix([[4, 10, -5], [7, 3, 15], [-14, 10, -2]])
my_matrix_2 = Matrix([[5, 7, 6], [1, 58, -20], [7, 35, 50]])
print(my_matrix_1)
print(my_matrix_2)
print(my_matrix_1 + my_matrix_2)



