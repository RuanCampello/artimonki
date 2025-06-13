from collections import defaultdict


deck = input().strip()
# deck = "13P02P01P03P04P05P06P07P08P09P10P11P12P"
# deck = "13P02P01P03P04P05P06P07P08P09P10P11P12P"


def parse_suits(deck: str):
    suits = defaultdict(list)

    for idx in range(0, len(deck), 3):
        if idx + 3 > len(deck):
            break
        card = deck[idx : idx + 3]
        value = card[:2]
        suit = card[2]
        suits[suit].append(value)

    res = list()
    for letter in ["C", "E", "U", "P"]:
        if letter not in suits:
            res.append(13)  # all cards missing
            continue

        cards = suits[letter]

        if len(cards) != len(set(cards)):
            res.append("erro")
            continue

        present = set(int(value) for value in cards)
        expected = set(range(1, 14))
        missing = expected - present

        if missing:
            res.append(len(missing))
        else:
            res.append(0)

    return res


result = parse_suits(deck)
print("\n".join(map(str, parse_suits(deck))))
