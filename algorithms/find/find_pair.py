import random

array = random.sample(range(2, 20), 15)
search = random.randint(2, 20)
# step one - merge_sort about n*log(n)

def merge(arr, p, q, r):
    left = arr[p: q+1]
    right = arr[q+1: r+1]
    i, j, k = 0, 0, p
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    if i < len(left):
        arr[k: r+1] = left[i:]
    if j < len(right):
        arr[k: r+1] = right[j:]

def merge_sort(arr, p=0, r=None):
    if r is None:
        r = len(arr) - 1
    if p >= r:
        return
    q = (p + r) // 2
    merge_sort(arr, p, q)
    merge_sort(arr, q+1, r)
    merge(arr, p, q, r)

merge_sort(array)

# step two - search elements about n

def find_pair(array, search):
    low = 0
    high = len(array) - 1
    while low < high:
        if array[low] + array[high] == search:
            return array[low], array[high]
        elif array[low] + array[high] < search:
            low += 1
        else:
            high -= 1
    return None

print(array)
print(f'search = {search}')
print(f'element = {find_pair(array, search)}')
print(f'complexity = O(n*log(n)) + O(n) = O(n*log(n))')