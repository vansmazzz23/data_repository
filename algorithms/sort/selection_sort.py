arr = [3, 2, 5, 7, 1]


def selection_sort(arr):
    for i in range(len(arr) - 1):
        smallest = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest]:
                smallest = j
                arr[i], arr[smallest] = arr[smallest], arr[i]
    return arr


selection_sort(arr)
