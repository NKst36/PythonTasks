#Вариант 10
#1. Найти максимальный среди всех элементов тех строк заданной
#матрицы, которые упорядочены (либо по возрастанию, либо по убыванию).
'''
matr = [[1, 2, 4, 7],
        [7, 3, 1, 9],
        [8, 7, 6, 1],
        [1, 3, 9, 2]]
print(max([max(row) for row in matr if row == sorted(row) or row[::-1] == sorted(row)]))
'''

matrix = [[15, 2, 4, 7],
        [104, 254, 1, 9],
        [157, 54, 57, 1],
        [1, 3, 70, 28]]
element_max = []
count_sorted_row = 0
for row in matrix:
    if row == sorted(row) or row[::-1] == sorted(row):
        element_max.append(max(row))
        count_sorted_row += 1
if (count_sorted_row == 0):
    print("В матрице нет сортированных строк")
else:
    print(max(element_max))

