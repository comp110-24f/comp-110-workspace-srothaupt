"""Calculations to throw the best tea party ever. (yes, even better than Boston's)"""

__author__: str = "730673654"


# MAIN PLANNER; make these match the notes
# don't forget that people=guests must be used
def main_planner(guests: int) -> None:
    """Return output to the screen."""
    print("A Cozy Tea Party for", guests, "People!")
    print("Tea Bags:", tea_bags(people=guests))
    print("Treats:", treats(people=guests))
    print(
        f"Cost: ${cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests)):.2f}"
    )
    return None


# TEA BAGS -- 2 per person
def tea_bags(people: int) -> int:
    """Return the number of tea bags needed at the tea party."""
    return people * 2


# TREATS - need 1.5 treats per tea but need to think about number of guests first


def treats(people: int) -> int:
    """Return the number of treats needed"""
    return round(tea_bags(people) * 1.5)


# COST which is function of tea_pags and treats


def cost(tea_count: int, treat_count: int) -> float:
    """Return the cost of the awesomest tea party ever."""
    return (tea_count * 0.5) + (treat_count * 0.75)


# making the program runnable, must be at end or else nothing will happen

if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
