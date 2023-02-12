import random
import time

# time complexity O(n)
def find_max_crossing_subarray(list, low=0, mid=0, height=0):
    sum, left_sum, left_index = 0, 0, 0
    for i in range(mid, low-1, -1):
        sum += list[i]
        if sum > left_sum:
            left_sum = sum
            left_index = i

    sum, right_sum, right_index = 0, 0, mid
    for j in range(mid+1, height):
        sum += list[j]
        if sum > right_sum:
            right_sum = sum
            right_index = j
    return left_index, right_index, left_sum + right_sum


# time complexity O(n * log(n))
def find_max_subarray(list, low=0, height=0):
    if low == height:
        return low, height, list[low]
    mid = (low + height) // 2
    # time complexity T(n/2)
    left_min, left_max, left_sum = find_max_subarray(list, low, mid)
    # time complexity T(n/2)
    right_min, right_max, right_sum = find_max_subarray(list, mid+1, height)
    # time complexity T(n)
    cross_min, cross_max, cross_sum = find_max_crossing_subarray(list, low, mid, height)
    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_min, left_max, left_sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_min, right_max, right_sum
    else:
        return cross_min, cross_max, cross_sum


if __name__ == '__main__':
    list = random.sample(range(-20, -10), 10)
    print(list)
    start = time.time()
    min_index, max_index, sum = find_max_subarray(list, 0, len(list) - 1)
    end = time.time()
    print(f'min_index = {min_index}, max_index = {max_index}, sum = {sum}')
    print("The time  :",
          (end-start) * 10**3, "ms")