from typing import List


def findDifference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
    ans1 = list(filter(lambda x: x not in nums2, set(nums1)))
    ans2 = list(filter(lambda x: x not in nums1, set(nums2)))
    return [ans1, ans2]


print(findDifference([1, 2, 3], [2, 4, 6]))
print(findDifference([1, 2, 3, 3], [1, 1, 2, 2]))
