"""making a bunch of functions"""

__author__ = "730673654"


def get_first(one: list[str]) -> str:
    first: str = one[0]
    return first


def remove_first(two: list[str]) -> None:
    two.pop(0)


def get_and_remove(three: list[str]) -> str:
    first: str = three[0]
    remove_first(three)
    return first


# print(get_first(one=["a", "b", "c"]))
three = ["a", "b", "c"]
print(get_and_remove(three))
print(three)
