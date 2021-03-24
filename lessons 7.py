# рекурсии

def matreshka(n):
    """
    реализуем метрешку рекурсией с уровнем вложенности n
    :param n: количество матрешек
    :return: none
    """
    if n == 1:
        print("матрешекчка")
    else:
        print("верх матрешки n=", n)
        matreshka(n - 1)
        print("низ матрешки n=", n)


matreshka(5)


# факториал

def factor(n=int):
    assert n >= 0, "факториал не определен"
    if n == 0:
        return 1
    return factor(n - 1) * n


print(factor(5))


# Алгоритм Евклида

def get(a, b):
    if a == b:
        return a
    elif a > b:
        return get(a - b, b)
    else:
        return get(a, b - a)


# Алгоритм Евклида улучшенный

def get_up(a, b):
    if b == 0:
        return a
    else:
        return get_up(b, a % b)


# Алгоритм Евклида улучшенный ещё

def get_up2(a, b):
    return a if b == 0 else get_up2(b, a % b)


# рекурентный случай возведения в степень

def pow(a: float, n: int):
    return 1 if n == 0 else pow(a, n - 1) * a


# рекурентный случай возведения в степень улучшен
# реальный премер быстрого вычислений большой степени

def pow_up(a: float, n: int):
    if n == 0:
        return 1
    elif n % 2 == 1:  # n - не четное
        return pow_up(a, n - 1) * a
    else:  # n - четное
        return pow_up(a ** 2, n // 2)
