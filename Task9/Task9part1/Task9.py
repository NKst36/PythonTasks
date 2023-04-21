#Вариант 10
#1. Найти максимальный среди всех элементов тех строк заданной
#матрицы, которые упорядочены (либо по возрастанию, либо по убыванию).

with open('Mymatrix.txt', 'r') as file:
    lines = file.readlines()
    #print(lines)
#print(len(lines))
for i in range(len(lines)):
    lines[i] = list(map(int,(lines[i].rstrip()).split()))
#print(lines)
'''
matr = [[1, 2, 4, 7],
        [11, 25, 8, 5],
        [8, 10, 6, 1],
        [1, 3, 9, 2]]
'''

element_max = [] # Список максимальных элементов
count_sorted_row = 0 # Количество сортированных строк
for row in lines:
    if row == sorted(row) or row == sorted(row, reverse = True):
        element_max.append(max(row))
        count_sorted_row+=1
f = open('ResultTask.txt', 'w')
if (count_sorted_row == 0):
    f.write("В матрице нет сортированных строк")
else:
    f.write(f'Максмальный элемент: {str(max(element_max))}')
f.close()
