from typing import List


def increasingTriplet(nums: List[int]) -> bool:
    first = second = float("inf")  # some crazy things
    for num in nums:
        if num <= first:
            first = num
        elif num <= second:
            second = num
        else:
            return True
    return False


print(increasingTriplet([1, 2, 3, 4, 5]))
print(increasingTriplet([5, 4, 3, 2, 1]))
print(increasingTriplet([2, 1, 5, 0, 4, 6]))
