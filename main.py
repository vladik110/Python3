#!/usr/bin/env python3
# coding=utf-8

import random


# функция для получения массива случайных чисел
def random_array(n, m, max_value=21):
    array = []  # основной массив
    for i in range(0, n):
        sub_array = []  # подмассив с числами
        for j in range(m):
            # от минимального числа (-20) до максимального -1 (max_value - 1 = 20) с шагом (1)
            number = random.randrange(0, max_value, 1)
            sub_array.append(number)  # добавление случайного числа в подмассив
        array.append(sub_array)  # добавление подмассива в массив
    return array  # возвращается массив с подмассивами внутри


# функция для вывода массива
def print_array(array):
    print()
    for i in array:  # перебор по подмассивам(строкам)
        for j in i:  # перебор по элементам строк
            print("%4d\t" % j, end='')
        print()


# функция для нахождения элементов условия (количество четных элементов,
# расположенных перед максимальным элементом таблицы)
def counting(array):
    print()
    # т.к. в массиве только положительные числа, то как начальное значение для макс -1
    max_value = -1
    max_j = -1
    max_i = -1
    count = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] >= max_value:
                max_value = array[i][j]
                max_i = i
                max_j = j
    print("Максимум: %d в ячейке: [%d][%d]" % (max_value, max_i + 1, max_j + 1))
    for i in range(max_i + 1):
        if i == max_i:
            for j in range(max_j):
                if (array[i][j] % 2) == 0:
                    count += 1
        else:
            for j in range(len(array[i])):
                if (array[i][j] % 2) == 0:
                    count += 1
    print("Количество четных элементов: %d" % count)
    print()
    return count, max_i, max_j


def main():
    # вызов функции рандома массива, которая возвращает полученный массив
    array = random_array(4, 5)  # можно изменить размер
    print("Условие задания:\n"
          "Подсчитать количество четных элементов,\n"
          "расположенных перед максимальным элементом таблицы\n"
          "и увеличить на это значение максимальный элемент")
    # вызов функции вывода массива
    print_array(array)
    # вызов функции массива по условию, который возвращает элементы для проверки условия
    count, max_i, max_j = counting(array)
    while True:
        print("1. Заполнить массив случайными числами;")
        print("2. Выполнить задание;")
        print("3. Выход.")
        key = input('Введите команду (1, 2 или 3): ')
        if key == '1':  # рандом, вывод и новые значения по условию нового массива
            array = random_array(4, 5)
            print_array(array)
            count, max_i, max_j = counting(array)
        elif key == '2':
            # выполнения результата совпадения условия,
            # в данном случае макс + count
            array[max_i][max_j] += count
            print("Макс. элемент таблицы (последний, если их больше одного) "
                  "был увеличен на количество четных элементов расположенных до него.")
            print_array(array)
            break  # выход из цикла
        elif key == '3':
            exit(0)  # выход из программы


if __name__ == '__main__':
    main()
