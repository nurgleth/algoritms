# O(n log n)
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        barrier = array[0]
        left = [i for i in array[1:] if i <= barrier]
        right = [i for i in array[1:] if i > barrier]
        return quicksort(left) + [barrier] + quicksort(right)

a = [2, 10,5,1,11,0]
print(quicksort(a))
