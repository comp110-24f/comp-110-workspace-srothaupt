my_dict: dict[int, str] = {0: "dog", 1: "cat", 2: "mouse", 3: "bird", 4: "whale"}

for x in range(0, 2):
    print(my_dict[x])


def merge_list(first: list[str], second: list[int]) -> dict[str, int]:
    new: dict[str, int] = {}
    if len(first) != len(second):
        return new
    for f in first:
        for s in second:
            new[f] = s
    return new


a: list[str] = ["a", "b", "c"]
b: list[int] = [1, 37, 3]

print(merge_list(a, b))

c: dict[int, str] = {2: "a", 1: "b", 0: "c"}
for key in c:
    print(c[key])
