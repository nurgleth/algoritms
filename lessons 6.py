# квадратичные сортировки
def insert_sort(A):
    """
    Сортировка списка А вставками
    :param A: Список А
    :return: Сортированный список А
    """
    N = len(A)
    for top in range(1, N):
        k = top
        while k > 0 and A[k - 1] > A[k]:
            A[k], A[k - 1] = A[k - 1], A[k]
            k -= 1 # позиция того элемента


def choise_sort(A):
    """
    Сортировка методом выбора
    :param A: Список А
    :return: Сортированный список А
    """
    N = len(A)
    for pos in range(0, N-1): # позиция минимума
        for k in range(pos+1, N):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]


def bubble_sort(A):
    """
    Сортировка пузырьком
    :param A: Список А
    :return: Сортированный список А
    """
    N = len(A)
    for bypass in range(1, N): # количество проходов
        for k in range(0, N-bypass):
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]


def test_sort(algoritm_sort):
    """
    тест сортировок
    :param algoritm_sort: массив сортировки
    :return: да или нет
    """
    print("Тестируем:", algoritm_sort.__doc__)
    print("testcase #1:", end=" ")
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    algoritm_sort(A)
    print("ok" if A == A_sorted else "Fail")

    print("testcase #2:", end=" ")
    A = list(range(10, 20)) + list(range(0, 10))
    A_sorted = list(range(20))
    algoritm_sort(A)
    print("ok" if A == A_sorted else "Fail")

    print("testcase #3:", end=" ")
    A = [4, 2, 4, 2, 1]
    A_sorted = [1, 2, 2, 4, 4]
    algoritm_sort(A)
    print("ok" if A == A_sorted else "Fail")


if __name__ == '__main__':
    test_sort(insert_sort)
    test_sort(choise_sort)
    test_sort(bubble_sort)

#поиск максимума в масиве
b = [1,7,3,1,4]
print(b[0])
c=[0,0,0,0,0,0,0,0]
c[b[0]] = c[b[0]]+1
print(c)
def new_max(lst):
    max = lst[0]
    for k in range(1, len(lst)):
        if lst[k]> max:
            max = lst[k]
    return max




