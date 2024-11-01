"""practice"""


def less_than_10(num: int) -> None:
    """Tell me if num is < 10."""
    dub: int = num * 2
    dub = dub - 1
    print(dub)
    if num < 10:
        print("Small number!")
    else:
        print("Big number!")
    print("Have a nice day!")


less_than_10(num=5)

diction: dict[int, str] = {0: "a", 2: "b", 1: "c"}
for x in range(0, len(diction)):
    print(diction[x])
