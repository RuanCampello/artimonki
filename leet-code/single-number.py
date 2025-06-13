from typing import List


def singleNumber(nums: List[int]) -> int:
    return next(filter(lambda num: nums.count(num) == 1, nums))


print(singleNumber([2, 2, 1]))
print(singleNumber([4, 1, 2, 1, 2]))
print(singleNumber([1]))
