from collections import defaultdict

responses = defaultdict(list)
messages = defaultdict(list)
pending = set()
time = 0


def timeout(msg: str):
    global time
    kind = msg[0].lower()
    value = int(msg[-1]) if len(msg) > 1 else 0

    if kind == "t":
        time += value
        return None
    increment = 1

    if kind == "r":
        messages[value].append(time)
        pending.add(value)
    elif kind == "e" and value in pending:
        received = messages[value].pop()
        if not messages[value]:
            pending.remove(value)
        responses[value].append(time - received)

    time += increment
    return None


def timeout_print():
    result = []
    for friend in sorted(responses):
        result.append((friend, sum(responses[friend])))

    for friend in sorted(pending):
        result.append((friend, -1))  # missing friends
    for friend, total in sorted(result):
        print(friend, total)


quant = int(input())
for _ in range(quant):
    timeout(input())
print(timeout_print())
