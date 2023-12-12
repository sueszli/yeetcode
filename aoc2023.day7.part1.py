INPUT = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""


cards, bids = zip(*list(map(str.split, INPUT.strip().splitlines())))

# types:
# case 1 - 5
# case 2 - 4, 1 <
# case 3 - 3, 2 <
# case 4 - 3, 1, 1 <
# case 5 - 2, 2, 1 <
# case 6 - 2, 1, 1, 1
# case 7 - 1, 1, 1, 1, 1


def getwinner(str1, str2, res):
    if res == 0:
        return "draw"
    elif res > 0:
        return str1
    else:
        return str2


def compare(str1: str, str2: str) -> int:
    o1 = {c: str1.count(c) for c in str1}
    o2 = {c: str2.count(c) for c in str2}
    if len(o1) != len(o2):
        print("(1)", str1, "vs", str2, "=>", getwinner(str1, str2, len(o2) - len(o1)))
        return len(o2) - len(o1)

    max1 = max(o1.values())
    max2 = max(o2.values())
    if max1 != max2:
        print("(2)", str1, "vs", str2, "=>", getwinner(str1, str2, max1 - max2))
        return max1 - max2

    rank = "AKQJT98765432"
    for c1, c2 in list(zip(str1, str2)):
        if c1 != c2:
            print("(3)", str1, "vs", str2, "|", c1, "vs", c2, "=>", getwinner(str1, str2, rank.index(c2) - rank.index(c1)))
            return rank.index(c2) - rank.index(c1)

    return 0


from functools import cmp_to_key

sorted_cards = sorted(cards, key=cmp_to_key(compare))
print("before:", cards)
print("after:", sorted_cards)
print("solution:", ["32T3K", "KTJJT", "KK677", "T55J5", "QQQJA"])
