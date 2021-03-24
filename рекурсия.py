def reckersia(i):
    print(i)
    if i <= 1:
        return
    else:
        reckersia(i - 1)


reckersia(10)


def sum(arr):
    """
    функция суммирования массива
    :param arr: массив
    :return: сумму чисел в массиве
    """
    total = 0
    for x in arr:
        total += x
    return total


a = [1, 5, 10]
print(sum(a))


def rec_sum(arr: list):
    """
    рекурсивная сумма массива
    :param arr: массив
    :return: сумма массива
    """
    if arr == []:
        return 0
    return arr[0] + rec_sum(arr[1:])


print(rec_sum(a))


def rec_sum1(arr: list):
    """
    рексрсивная функция подсчета элементов в массиве
    :param arr: массив
    :return: количество элементов
    """
    if arr == []:
        return 0
    return 1 + rec_sum1(arr[1:])


print(rec_sum1(a))


def max(arr:list):
    """
    рекурсиваня функци нахождения наибольшего числа в списке
    :param arr: список
    :return: наибольшее число
    """
    if len(arr) == 2:
        return arr[0] if arr[0]> arr[1] else arr[1]
    sub_max = max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max
print(max(a))