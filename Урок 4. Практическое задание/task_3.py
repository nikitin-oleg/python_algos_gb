"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""

import cProfile
from timeit import timeit
from random import randint


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


num_10000 = randint(100000000, 10000000000000)

print(
    timeit(
        'revers(num_10000)',
        setup='from __main__ import revers, num_10000',
        number=10000))
print(
    timeit(
        'revers_2(num_10000)',
        setup='from __main__ import revers_2, num_10000',
        number=10000))
print(
    timeit(
        'revers_3(num_10000)',
        setup='from __main__ import revers_3, num_10000',
        number=10000))

print('*' * 30)
cProfile.run('revers(num_10000)')
cProfile.run('revers_2(num_10000)')
cProfile.run('revers_3(num_10000)')

"""Первая функция самая медленная, из-за того, что использует рекурсию. Вторая быстрее, но и она проигрывает
по быстродействию встроенным методам преобразования типов данных """
