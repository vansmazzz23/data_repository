import random

array = random.sample(range(5, 100), 7)

def merge_sort_with_insertion(array, p=0, r=None, threshold=8):
    if r is None:
        r = len(array) - 1
    if p >= r:
        return
    if len(array) <= threshold:
        return insertion_sort(array)
    q = (p + r) // 2
    merge_sort_with_insertion(array, p, q)
    merge_sort_with_insertion(array, q + 1, r)
    merge(array, p, q, r)


def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            array[j] = key
            j -= 1
    return array


def merge(array, p, q, r):
    left = array[p: q + 1]
    right = array[q + 1: r + 1]
    i, j, k = 0, 0, p
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    if i < len(left):
        array[k: r + 1] = left[i:]
    if j < len(right):
        array[k: r + 1] = right[j:]

print(array)
merge_sort_with_insertion(array)
print(array)