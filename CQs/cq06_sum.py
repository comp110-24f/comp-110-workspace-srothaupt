"""Summing the elements of a list using different loops"""

__author__ = "73067354"


# loop through idx and add to other sum value
def w_sum(vals: list[float]) -> float:
    idx: int = 0
    sum: float = 0.0
    while idx < len(vals):
        sum += vals[idx]
        idx += 1
    return sum


print(w_sum([1.1, 0.9, 1.0]))


# loop through elements in list
def f_sum(vals: list[float]) -> float:
    sum: float = 0.0
    for val in vals:
        sum += val
    return sum


print(f_sum([1.1, 0.9, 1.0]))


# loop through using range
def f_range_sum(vals: list[float]) -> float:
    sum: float = 0.0
    idx: int = 0
    for idx in range(0, len(vals)):
        sum += vals[idx]
        idx += 1
    return sum


print(f_range_sum([1.0, -3.0, 4.0]))
