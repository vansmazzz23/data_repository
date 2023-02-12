import random


def find_max_subarray_linear_time(list):
    sum = 0
    sub_sum = 0
    for item in list:
        sub_sum += item
        sub_sum = max(sub_sum, 0)
        sum = max(sum, sub_sum)
    return sum


if __name__ == '__main__':
    list = random.sample(range(-20, 20), 10)
    print(list)
    sum = find_max_subarray_linear_time(list)
    print(f'sum = {sum}')