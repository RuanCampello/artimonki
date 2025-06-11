from typing import Counter, List


def uniqueOccurrences(arr: List[int]) -> bool:
    counter = Counter(arr)
    occurences = list(map(lambda x: counter[x], set(arr)))
    return sorted(occurences) == sorted(set(occurences))


print(uniqueOccurrences([1, 2, 2, 1, 1, 3]))
