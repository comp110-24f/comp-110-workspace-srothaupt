"""Practice with conditionals."""


def less_than_10(num: int) -> None:
    """Tell me if num is < 10."""
    if num < 10:
        print("Small number!")
    else:
        print("Big number!")
    print("Have a nice day!")


less_than_10(num=11)


def should_i_eat(hungry: bool) -> None:
    """Tells me whether or not to eat based on hunger."""
    if hungry:  # conditional/boolean expression
        # or could be if hungry is True
        print("Eat some food silly goose!")  # 'then' block
    else:
        print("Do your COMP 110 homework.")  # 'else' block
    print("I'm proud of you <3")  # either way, be kind to yourself


should_i_eat(hungry=True)
