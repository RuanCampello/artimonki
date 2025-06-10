t = int(input())

for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    current = set()
    seen = set()
    ans = 0
    for num in array:
        current.add(num)
        seen.add(num)
        if len(current) == len(seen):
            ans += 1
            seen.clear()
    print(ans)

