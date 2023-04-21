#2. Составить программу, которая изменяет последовательность слов в строке на обратную.
def str_return():
    print('Введите строку')
    sentence = input().split(" ")[::-1]
    print(' '.join(sentence))
str_return()