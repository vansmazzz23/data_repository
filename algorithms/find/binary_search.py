import random


# nums = random.sample(range(8, 100), 9)
# target = nums[3]


def binary_search(nums, target):
    nums.sort()
    low = 0
    high = len(nums) - 1

    if not target in nums:
        return -1

    while high >= low:
        mid = int(int(high + low) / 2)
        if nums[mid] > target:
            high = mid - 1
        if nums[mid] < target:
            low = mid + 1
        if nums[mid] == target:
            return mid

