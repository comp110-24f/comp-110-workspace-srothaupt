"""dictionary activity"""

__author__ = "730673654"


# make sure to throw KeyError. set up dict before hand, update dict with new version
def invert(input: dict[str, str]) -> dict[str, str]:
    vert: dict[str, str] = {}
    for key in input:
        if input[key] in vert:
            raise KeyError("More than one of same key exists.")
        else:
            vert[input[key]] = key
    return vert


# count new list of colors? or maybe dict. then cycle through this new dict and pull the color with most counts
def favorite_color(input: dict[str, str]) -> str:
    if len(input) == 0:
        return ""
    count: dict[str, int] = {}
    for key in input:
        if key in count:
            count[input[key]] += 1
        if key not in count:
            count[input[key]] = 1
    highest: str = ""
    max_count: int = 0
    for color in count:
        if count[color] > max_count:
            highest = color
            max_count = count[color]
    return highest


# print(favorite_color({"Marc": "yellow", "John": "purple"}))
# print(favorite_color({}))


# cycle through list and check if val is in list to update counts
def count(input: list[str]) -> dict[str, int]:
    val: dict[str, int] = {}
    for i in input:
        if i not in val:
            val[i] = 1
        else:
            val[i] += 1
    return val


# print(count(["a", "b", "a", "c"]))


# cycle through each
def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    alpha: dict[str, list[str]] = {}
    idx: int = 0
    for i in input:
        if i[0] in alpha:
            old: list[str] = alpha[i[0]]
            old.append(i)
            alpha[i[0].lower()] = old
        if i[0] not in alpha:
            fresh: list[str] = []
            fresh.append(i)
            alpha[i[0].lower()] = fresh
    return alpha


# print(alphabetizer(["cat", "apple", "boy", "angry", "bad", "car"]))


def update_attendance(input: dict[str, list[str]], day: str, student: str) -> None:
    if day in input:
        old: list[str] = input[day]
        if student not in old:
            old.append(student)
        input[day] = old
    if day not in input:
        fresh: list[str] = []
        fresh.append(student)
        input[day] = fresh


# attendance_log: dict = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
# update_attendance(attendance_log, "Monday", "Vrinda")
# print(attendance_log)
