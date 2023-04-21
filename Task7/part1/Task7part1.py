#Вариант 10.
#1. На отрезке [100, N] (210 < N < 231) найти количество чисел, составленных из
#цифр а, b, с.)
print('Введите N (210 < N < 231):')
N = int(input())

print('Введите a:')
a = input()

print('Введите b:')
b = input()

print('Введите c:')
c = input()

""""
def count_elements(N, a, b, c):
    count = 0
    massive = [a, b, c]
    for first_position in massive:
        for second_position in massive:
            for third_position in massive:
                number1 = third_position * 100 + second_position * 10 + first_position
                if number1 >= 100 and number1 <= N:
                    count += 1
    return count

print(count_elements(N,a,b,c))
"""
def count_elements(N, a, b, c):
    counter = 0
    for i in range(100, N + 1):
        digit = str(i)
        if a in digit and b in digit and c in digit:
            counter += 1
    print(counter)
print('Количество чисел')
count_elements(N, a, b, c)
