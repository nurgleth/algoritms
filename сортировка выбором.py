# O(n^2)
def finSmallest(arr:list):
    """
    Принимает список и ищет наименьшее значение
    :param arr: Список
    :return: индекс наименьшего значения в списке
    """
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr:list):
    """
    Принимаем список и сортируем по возростанию
    :param arr:  Список
    :return: осортированный по возростанию список
    """
    newArr= []
    for i in range(len(arr)):
        smallest = finSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([5,2,1,2,6,10]))