from typing import List
from itertools import repeat


def moveZeroes(nums: List[int]) -> None:
    zeroes = nums.count(0)
    nums[:] = filter(lambda x: x != 0, nums)
    nums.extend(repeat(0, zeroes))
    print(nums)


moveZeroes([0, 1, 0, 3, 12])
