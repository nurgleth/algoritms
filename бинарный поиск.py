# O(log n)
def binary_search(list, item):
    """
    Бинарный поиска значения в отсартированном массиве
    :param list: остартированный массив
    :param item: значение которое нужно найти
    :return: номер в массиве
    """
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return None


a = [1,3,5,7,9]

print(binary_search(a, 5))