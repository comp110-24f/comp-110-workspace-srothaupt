"""making a legit wordle game"""

__author__ = "730673654"


def input_guess(secret_word_len: int) -> str:
    guess = input(f"Enter a {secret_word_len}-character word: ")
    lgth = len(guess)
    while lgth != secret_word_len:
        guess = input(f"That wasn't {secret_word_len} chars! Try again: ")
        lgth = len(guess)
    return guess


# input_guess(secret_word_len=7)


def contains_char(secret_word: str, char: str) -> bool:
    assert len(char) == 1
    idx: int = 0
    match = False
    while idx < len(secret_word):
        if char == secret_word[idx]:
            match = True
        idx += 1
    return match


# print(contains_char(secret="fool", char="oo"))


def emojified(guess: str, secret: str) -> str:
    """add emojis to the code"""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    build: str = ""
    idx: int = 0
    while idx < len(secret):
        if guess[idx] == secret[idx]:
            build += GREEN_BOX
        elif contains_char(secret_word=secret, char=guess[idx]) == True:
            build += YELLOW_BOX
        else:
            build += WHITE_BOX
        idx += 1
    return build


# print(emojified(guess="yikyak", secret="tiktok"))


def main(secret: str) -> None:
    """entrypoint of the program and main game loop"""
    turns: int = 1
    while turns < 7:
        print(f"=== Turn {turns}/6 ===")
        response = input_guess(secret_word_len=len(secret))
        print(emojified(guess=response, secret=secret))
        if secret == response:
            print(f"You won in {turns}/6 turns!")
            exit()
        turns += 1
    print("X/6 - Sorry, try again tomorrow!")


main(secret="helper")


if __name__ == "__main__":
    main(secret="codes")
