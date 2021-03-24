# Редакционное расстояние расстояние Ливинштейна или расстояние между строками
def levenstein(A, B):
    """
    Вычисляет наименьшее количество правок для строк, чтобы они были равны
    :param A: строка
    :param B: строка
    :return: возвращает минимальное редакционное расстояние
    """
    # создаем массив массиве(двумерный массив) количество элементов на 1 больше(нулевые включены)    #
    F = [[i + j if i * j == 0 else 0 for j in range(len(B) + 1)] for i in range(len(A) + 1)]
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                F[i][j] = F[i - 1][j - 1]
            else:
                F[i][j] = 1 + min(F[i - 1][j], F[i][j - 1], F[i - 1][j - 1])
    return F[len(A)][len(B)]


# проверка равенства строк
def eqel(A, B):
    if len(A) != len(B):
        return False
    for i in range(len(A)):
        if A[i] != B[i]:
            return False
    return True


# проверка вхождения подстроки в строку
def search_substring(s, sub):
    """
    наивно сравниваем вхождение sub в s смещаясь по одному элементу до конца s
    :param s: строка
    :param sub: подстрока
    :return: место совпадение sub в s
    """
    for i in range(0, len(s) - len(sub)):
        if eqel(s[i:i + len(sub)], sub):
            print(i)
