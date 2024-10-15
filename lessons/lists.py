"""list practice"""

my_numbers: list[float] = []
my_numbers.append(1.5)
print(my_numbers)

print(len(my_numbers))

game_points: list[int] = [102, 86, 94]
game_points[1] = 88
game_points.append(102)
game_points.pop(1)

print(game_points)


print(["Kris", "Kaki"][1])


def display(your_list: list) -> None:
    idx: int = 0
    while idx < len(your_list):
        print(your_list[idx])
        idx += 1
    return None


game_points: list[int] = [1, 2, 3, 4, 5]

display(game_points)
