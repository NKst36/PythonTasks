#Вариант 10
#Расположить столбцы матрицы D[M, N] в порядке возрастания
#элементов k-й строки (1 <= k <= М).
with open('Matrixnew.txt', 'r') as file:
    lines = file.readlines()
    #print(lines)
#print(len(lines))
for i in range(len(lines)):
    lines[i] = list(map(int,(lines[i].rstrip()).split()))
print(lines)


k = 2
kataya_stroka = []
'''
matrix = [[5, 10, 1, 4],
          [5, 15, 2, 4],
          [9, 8, 3, 4]]
'''
for i in range(len(lines[k])):
    kataya_stroka.append(lines[k][i])
print(kataya_stroka)
kataya_stroka.sort()
print(kataya_stroka)
index_stroki = [0] * (len(lines[k]))
finish_matrix = [0] * len(lines)
for q in range(len(lines)):
    finish_matrix[q] = [0] * len(lines[k])
#n = 0
#j = 0
print(len(lines[k])-1)
for j in range(len(lines[k])):
    for n in range(len(lines[k])):
        if lines[k][j] == kataya_stroka[n]:
            index_stroki[j] = n
print(index_stroki)
for column in range(len(lines)):
    for a in range(len(lines[k])):
        finish_matrix[column][index_stroki[a]] = lines[column][a]
print(finish_matrix)

f = open('Result.txt', 'w')
f.write("\n".join(map(str, finish_matrix)))
f.close()