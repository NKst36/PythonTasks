#Вариант 10
#Расположить столбцы матрицы D[M, N] в порядке возрастания
#элементов k-й строки (1 <= k <= М).


k = 2-1 #1-я строка
kataya_stroka = []
matrix = [[5, 10, 1, 4],
          [5, 15, 2, 4],
          [9, 8, 3, 4]]
for i in range(len(matrix[k])):
    kataya_stroka.append(matrix[k][i])
print("Печать k-той строки")
print(kataya_stroka)

kataya_stroka.sort()
print("Печать сортированной k-той строки")
print(kataya_stroka)

#Каждый элемент index_stroki означает порядковый номер в соответствии с которым
#будут выставлены столбцы
index_stroki = [0] * (len(matrix[k]))
finish_matrix = [0] * len(matrix) #итоговая матрица
#print(matrix[0][1])

for q in range(len(matrix)):
    finish_matrix[q] = [0] * len(matrix[k])

#print(len(matrix[k])-1)

for j in range(len(matrix[k])):
    for n in range(len(matrix[k])):
        if matrix[k][j] == kataya_stroka[n]:
            index_stroki[j] = n
print("Печать массива с порядковыми номерами")
print(index_stroki)

for row in range(len(matrix)):
    for a in range(len(matrix[k])):
        finish_matrix[row][index_stroki[a]] = matrix[row][a]

print("Начальная матрица")
print(matrix)
print("Итоговая матрица")
print(finish_matrix)

