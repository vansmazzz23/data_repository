nums = [2,3,4,1]


def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    base = nums[len(nums)//2]
    low = nums[:base]
    high = nums[base:]
    return quick_sort(low) + [base] + quick_sort(high)


quick_sort(nums)


arr = [1,3,2,6,4]
mid = len(arr)//2
print(mid)
print(arr[:mid])
print(arr[mid:])

