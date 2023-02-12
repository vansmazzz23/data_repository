# array = [3, 41, 52, 26, 38, 57, 9, 49]
array = [2,3,8,6,1,0,0]

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
print(array)