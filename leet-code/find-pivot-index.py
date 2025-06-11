from typing import List


def pivotIndex(nums: List[int]) -> int:
    itemsSum = sum(nums)
    left = 0

    for idx, num in enumerate(nums):
        if left == (itemsSum - left - num):
            return idx
        left += num
    return -1


print(pivotIndex([1, 7, 3, 6, 5, 6]))

