"""Practice from class."""

__author__ = "730673654"


def guess_a_number() -> None:
    # create local variables, make sure to remember formatting
    secret: int = 7
    x = int(input("Guess a number: "))
    print("Your guess was", x)
    # 3 different paths, = < or >
    if x == secret:
        print("You got it!")
    elif x < secret:
        print("Your guess was too low! The secret number is", secret)
    else:
        print("Your guess was too high! The secret number is", secret)
    return None


if __name__ == "__main__":
    guess_a_number()
