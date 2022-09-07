"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""

"""
При замерах рекурсии выдается каждая операция и замер прозводится на стадии выполнения каждой ф-и
Получается при каждом вызове ф-и рекурсии происходит зомер времени
Для решения данной проблеммы был использован декоратор
"""

from memory_profiler import profile


@profile
def rec_wrapper(dec_func):
    def wrapper(*args):
        res = dec_func(*args)
        return res

    return wrapper


def funct(k):
    n = k - 1
    return ((-1) ** n) / (2 ** n)


@rec_wrapper
def recurs3(n):
    return funct(n) if (n == 1) else funct(n) + recurs3(n - 1)


print(recurs3(3))
