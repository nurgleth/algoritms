def bin_serch(l: list, a: int):
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = l[mid]
        if guess == a:
            return mid
        elif guess < a:
            low = mid + 1
        else:
            high = mid - 1
    return False


a = [1, 3, 5, 7, 9]

print(bin_serch(a, 5))
b = [1, 3, 20, 7, 9]

# квадратичные сортировки
def insert_sort(A):
    """
    Сортировка списка А вставками
    :param A: Список А
    :return: Сортированный список А
    """
    N =len(A)
    for top in range(1, N):
        k = top
        while k > 0 and A[k-1]> A[k]:
            A[k], A[k-1] = A[k-1],A[k]
            k-=1

insert_sort(b)
print(b)
b = [1, 3, 20, 7, 9]


def bubble_sort(A):
    """
    Сортировка пузырьком
    :param A: Список А
    :return: Сортированный список А
    """
    N = len(A)
    for bable in range(1, N):
        for k in range(0, N - bable):
            if A[k] > A[k + 1]:
                A[k], A[k + 1] = A[k + 1], A[k]



bubble_sort(b)
print(b)
b = [1, 3, 20, 7, 9]
def wik_sort(arr:list):
    if len(arr) < 2:
        return arr
    else:
        barrier = arr[0]
        left = [i for i in arr[1:] if i <= barrier]
        right = [i for i in arr[1:] if i > barrier]
        return wik_sort(left)+[barrier]+wik_sort(right)

print(wik_sort(b))


def time_value():
    return None