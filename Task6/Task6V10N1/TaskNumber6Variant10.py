#Вариант 10
#1. Определите, есть ли в списке повторяющиеся элементы, если да, то вывести
#на экран это значение, иначе сообщение об их отсутствии.


# Cловарь ключ(элемент списка), значение(количество повторений)
test_list = [5, 8, 4, 3, 1, 5, 4]
def dictionary_value_and_repeats(test_list):
    repeats = {}
    for item in test_list:
        if item in repeats:
            repeats[item] += 1
        else:
            repeats[item] = 1
    return repeats
repeats = dictionary_value_and_repeats(test_list)

# Напечатаем элементы количество повторений > 1
def repeats_items(repeats):
    count_el = 0
    for key in repeats.keys():
        if repeats[key] > 1:
            print(key)
            count_el += 1
    if count_el == 0:
        print("В списке нет повторяющихся элементов")
    return repeats
repeats2 = repeats_items(repeats)

