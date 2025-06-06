from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    chars = list(zip(*strs))

    for str in chars:
        print(len(set(str)))

    return ""


longestCommonPrefix(strs=["dog", "racecar", "car"])
