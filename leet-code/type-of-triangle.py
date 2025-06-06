from typing import List, Set


def triangleType(nums: List[int]) -> str:
    lesser, medium, greater = sorted(nums)
    if medium + lesser <= greater:
        return "none"

    not_duplicates: Set[int] = set()

    for num in nums:
        not_duplicates.add(num)

    match len(not_duplicates):
        case 1:
            return "equilateral"
        case 2:
            return "isosceles"
        case 3:
            return "scalene"
        case _:
            return "none"


print(triangleType(nums=[3, 3, 3]))
print(triangleType(nums=[3, 4, 5]))
print(triangleType([4, 4, 4]))
print(triangleType([8, 4, 2]))
print(triangleType([8, 4, 4]))
print(triangleType([10, 10, 6]))
