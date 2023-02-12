import random

# time complexity O(n)
def find_max_crossing_subarray(list, low=0, mid=0, hight=0):
    if len(list) == 0:
        return 0
    if hight == 0:
        hight = len(list)
    if mid == 0:
        mid = (low + hight) // 2
    sum, left_sum, left_index = 0, 0, 0
    for i in range(mid, low-1, -1):
        sum += list[i]
        if sum > left_sum:
            left_sum = sum
            left_index = i

    sum, right_sum, right_index = 0, 0, 0
    for i in range(mid+1, hight):
        sum += list[i]
        if sum > right_sum:
            right_sum = sum
            right_index = i

    return left_index, right_index, left_sum + right_sum


if __name__ == '__main__':
    list = random.sample(range(-20, 20), 11)
    print(list)
    left_index, right_index, max_crossing_subarray = find_max_crossing_subarray(list)
    print(left_index, right_index, max_crossing_subarray)
