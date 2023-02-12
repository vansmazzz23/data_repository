import random

array = random.sample(range(5, 40), 10)

def bubble_sort(array):
    for i in range(len(array) - 1):
        j = len(array) -1
        for j in range(j, i, -1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
    return array


print(array)
print(bubble_sort(array))
print(sorted(array))

