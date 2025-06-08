from typing import List


def compress(chars: List[str]) -> int:
    length = 0
    idx = 0

    while idx < len(chars):
        letter = chars[idx]
        quantity = 0
        while idx < len(chars) and letter == chars[idx]:
            quantity += 1
            idx += 1
        chars[length] = letter
        length += 1

        if quantity > 1:
            for char in str(quantity):
                chars[length] = char
                length += 1

    return length


print(compress(["a", "a", "b", "b", "c", "c", "c"]))
print(compress(["a"]))
print(compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))
