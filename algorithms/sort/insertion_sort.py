arr = [31, 41, 59, 26, 41, 58]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            arr[j] = key
            j = j - 1
        # print(f'{i} = {key} ={arr}')
    return arr


def inverse_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            arr[j] = key
            j = j - 1
        # print(f'{i} = {key} ={arr}')
    return arr


print(insertion_sort(arr))
print(inverse_insertion_sort(arr))
