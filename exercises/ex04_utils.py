"""list utility functions"""

__author__ = "730673654"


# check if a number is in list, prob need to cycle through index and just exit if there is no match
def all(your_list: list[int], check: int) -> bool:
    idx: int = 0
    fig: bool = True
    while fig == True and idx < len(your_list):
        if your_list[idx] == check:
            fig = True
        else:
            fig = False
        idx += 1
    if len(your_list) == 0:
        fig = False
    return fig


# similar to card example from first class, replace high with new high else same
def max(new_list: list[int]) -> int:
    if len(new_list) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        idx: int = 1
        high: int = new_list[0]
        while idx < len(new_list):
            if high < new_list[idx]:
                high = new_list[idx]
            idx += 1
    return high


# check through each index of each list
def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    idx1: int = 0
    idx2: int = 0
    result: bool = True
    while result == True and idx1 < len(list_1) and idx2 < len(list_2):
        if list_1[idx1] == list_2[idx2]:
            result = True
        else:
            result = False
        idx1 += 1
        idx2 += 1
    if len(list_1) == 0 or len(list_2) == 0:
        result = False
    if len(list_1) != len(list_2):
        result = False
    if len(list_1) == 0 and len(list_2) == 0:
        result = True
    return result


# similar to adding on a string
def extend(list_1: list[int], list_2: list[int]) -> None:
    list_1 += list_2
    print(list_1)
