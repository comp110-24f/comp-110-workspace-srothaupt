"""Mutating functions."""

__author__ = "730673654"


# manually append by adding stuff
def manual_append(your_list: list[int], two: int) -> None:
    your_list.append(two)


# make two lists to test with second = first
list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

manual_append(list_1, 4)

print(list_1)


# double each digit in list
def double(new_list: list[int]) -> None:
    idx: int = 0
    while idx < len(new_list):
        new_list[idx] = new_list[idx] * 2
        idx += 1


double(list_2)
print(list_1)
print(list_2)
