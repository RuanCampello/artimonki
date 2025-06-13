def tribonacci(n: int) -> int:
    trib = [0] * (n + 1)
    trib[1] = trib[2] = 1

    for idx in range(3, n + 1):
        trib[idx] = trib[idx - 1] + trib[idx - 2] + trib[idx - 3]
    return trib[n]


print(tribonacci(4))
print(tribonacci(25))
