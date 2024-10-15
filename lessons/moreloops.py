my_list: list[str] = ["hello", "world"]
new_list: list[str] = []
for elem in my_list:
    new_list.append(elem)
print(new_list)


pets: list[str] = ["Louie", "Bo", "Bear"]
for animal in pets:
    print(f"Good boy, {animal}!")


names: list[str] = ["Alyssa", "Janet", "Vrinda"]
for idx in range(0, len(names)):
    print(f"{idx}: {names[idx]}")
