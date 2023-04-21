# Вариант 10
# 2. Дан одномерный массив из 15 элементов. Элементам массива меньше 10
# присвоить нулевые значения, а элементам больше 20 присвоить 1. Вывести на
# экран монитора первоначальный и преобразованный массивы в строчку.
begin_massive = [5, 15, 25, 37, 2, 10, 20, 17, 4, 17, 54, 74, 62, 175, 1]
final_massive = begin_massive.copy()
def define_massive(final_massive):
    i = 0
    while i < len(final_massive):
        if final_massive[i] < 10:
            final_massive[i] = 0
        elif final_massive[i] > 20:
            final_massive[i] = 1
        i += 1
    return final_massive

final_massive = define_massive(final_massive)
print(begin_massive)
print(final_massive)
