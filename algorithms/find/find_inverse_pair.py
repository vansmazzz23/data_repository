array = [2,3,8,6,1]


def merge(arr, p, q, r):
    pairs = 0
    left = arr[p: q+1]
    right = arr[q+1: r+1]
    print(f'p = {p}, q = {q}, r = {r}')
    print(left, right)
    i, j, k = 0, 0, p
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
            pairs += q - p - i + 1
            print(f'pairs = {pairs}  i = {i}  j = {j}')
        k += 1

    if i < len(left):
        arr[k: r+1] = left[i:]
    if j < len(right):
        arr[k: r+1] = right[j:]
    return pairs


def merge_sort(arr, p=0, r=None):
    pairs = 0
    if r is None:
        r = len(arr) - 1
    if p >= r:
        return 0
    q = (p + r) // 2
    pairs += merge_sort(arr, p, q)
    pairs += merge_sort(arr, q+1, r)
    pairs += merge(arr, p, q, r)
    return pairs


merge_sort(array)