def is_balanced(string: str) -> bool:
    paren = 0

    for char in string:
        if char == "(":
            paren += 1
        else:
            paren -= 1

        if paren < 0:
            return False
    return paren == 0


def can_break(string: str):
    trim = string[1:-1]
    return "NO" if is_balanced(trim) else "YES"


quant = int(input())
for _ in range(quant):
    bracket = input()
    print(can_break(bracket))
