from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    chars = list(zip(*strs))
    cursor = 0
    backtrack = -1

    for idx, str in enumerate(chars):
        if len(set(str)) == 1:
            if backtrack + 1 == idx:
                cursor += 1
                backtrack = idx

    return strs[-1][0:cursor]


print(longestCommonPrefix(strs=["dog", "racecar", "car"]))
print(longestCommonPrefix(strs=["flower", "flow", "flight"]))
print(longestCommonPrefix(["cir", "car"]))
