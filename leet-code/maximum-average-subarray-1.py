from typing import List


def findMaxAverage(nums: List[int], k: int) -> float:
    window = sum(nums[:k])
    max_sum = window

    for idx in range(k, len(nums)):
        window += nums[idx] - nums[idx - k]
        max_sum = max(max_sum, window)

    return max_sum / k


print(findMaxAverage([1, 12, -5, -6, 50, 3], 4))
print(findMaxAverage([5], 1))
