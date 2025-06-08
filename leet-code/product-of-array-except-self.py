from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    result: List[int] = [1] * len(nums)

    prefix = 1
    for idx in range(len(nums)):
        result[idx] = prefix
        prefix *= nums[idx]

    postfix = 1
    for idx in range(len(nums) - 1, -1, -1):
        result[idx] *= postfix
        postfix *= nums[idx]

    return result


print(productExceptSelf([1, 2, 3, 4]))
