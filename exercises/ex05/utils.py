"""utils actual"""

__author__ = "730673654"


# cycle through and check if even
def only_evens(input: list[int]) -> list:
    idx: int = 0
    evens: list = []
    while idx < len(input):
        if input[idx] % 2 == 0:
            evens.append(input[idx])
        else:
            None
        idx += 1
    return evens


# def only_evens(input: list[int]) -> list:

# print(only_evens([100, 200, 300]))


# cycle through range and keep the ones that fit in range
def sub(input: list[int], start: int, end: int) -> list:
    sub: list = []
    if start < 0:
        idx: int = 0
    else:
        idx: int = start
    while idx < end and idx < len(input):
        sub.append(input[idx])
        idx += 1
    return sub


# def sub(input: list[int], start: int, end: int) -> list:


# directions say you may need to move stuff; shift each unit over until you find the idx
def add_at_index(input: list[int], element: int, idx: int) -> None:
    if idx < 0 or idx > len(input):
        raise IndexError("Index is out of bounds for the input list")
    input.append(0)
    for i in range(len(input) - 1, idx, -1):
        input[i] = input[i - 1]
    input[idx] = element


# def add_at_index(input: list[int], element: int, idx: int) -> None:

a_list = [1, 2, 3, 5]
print(a_list)

# print(sub(a_list, -1, 6))
# add_at_index(a_list, 4, 3)
# print(a_list)
# print(a_list)
