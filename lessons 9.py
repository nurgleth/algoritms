# рекурсивные сортировки

def merge(A: list, B: list):
    """
    алгоритм слияния
    :param A: один масив
    :param B: второй масив
    :return: третий отсартированый масив из А и B
    """
    C = [] * (len(A) + len(B))
    i = k = n = 0
    while i < len(A) and A[i] <= B[k]:
        if A[i] < B[k]:
            C[n] = A[i]
            i += 1
            n += 1
        else:
            C[n] = B[k]
            k += 1
            n += 1

    while i < len(A):
        C[n] = A[i]
        i += 1
        n += 1

    while k < len(B):
        C[n] = B[k]
        k += 1
        n += 1
    return C


def merg_sort(A):
    """
    Алгорит Соритровка слиянием
    :param A: список
    :return: сортирует список
    """
    if len(A) <= 1:  # крайний случай
        return
    middle = len(A) // 2
    L = [A[i] for i in range(0, middle)]  # можно и срезами
    R = [A[i] for i in range(middle, len(A))]
    merg_sort(L)
    merg_sort(R)
    C = merge(L, R)
    for i in range(len(A)):
        A[i] = C[i]
    return


# Сортировка Тони Хоара

def hoar_sort(A):
    if len(A) <= 1:
        return
    barrier = A[0]  # барьерный элемент
    L = []  # левая часть
    M = []  # середина
    R = []  # правая часть
    for x in A:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else:
            R.append(x)
        hoar_sort(L)
        hoar_sort(R)
        k = 0  # счетчик заполности для переливания соритрованого массива обратно
        for x in L + M + R:
            A[k] = x
            k += 1


# алгоритм проверки соритрован ли массив
def check_sorted(A, assending=True):
    """
    алгоритм проверки сортирован ли массив на убвание или возрастание
    :param A: массив
    :param assending: парамметр True для соритрован ли массив по возсрастанию
    :return: возвращает правду или ложь
    """
    flag = True
    s = 2*int(assending) - 1 # параметр для массива на убывание
    for i in range(0, (len(A)-1)):
        if s*A[i] > s*A[i+1]:
            flag = False
            break
    return flag


