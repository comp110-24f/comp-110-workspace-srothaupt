__author__ = "730673654"


# need two loops
def find_and_remove_max(input: list[int]) -> int:
    if len(input) != 0:
        max: int = input[0]
        for i in input:
            if i > max:
                max = i
        idx: int = 0
        while idx < len(input):
            if input[idx] == max:
                input.pop(idx)
                idx = idx - 1
            idx += 1
    if len(input) == 0:
        max = -1
    return max


a: list[int] = [13, 9, 10, 12, 13, 13, 9, 8, 7]
# max: int = a[1]
print(find_and_remove_max(a))
print(a)
