from typing import List


def countBits(n: int) -> List[int]:
    binary = lambda x: bin(x)[2:]
    bits = [binary(x).count("1") for x in range(n + 1)]
    return bits


print(countBits(2))
print(countBits(5))
