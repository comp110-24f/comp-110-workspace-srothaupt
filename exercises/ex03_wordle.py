"""making a legit wordle game"""

__author__ = "730673654"


def input_guess(secret_word_len: int) -> str:
    # function should test length of user's guess to ensure it matches the length of the secret word
    guess = input(f"Enter a {secret_word_len} character word: ")
    lgth = len(guess)
    while lgth != secret_word_len:
        # get them to fix it!!
        guess = input(f"That wasn't {secret_word_len} chars! Try again: ")
        lgth = len(guess)
    return guess


def contains_char(secret_word: str, char: str) -> bool:
    # cross reference the character at each index of the guess with entire secret word to see if there is a match at all
    assert len(char) == 1
    idx: int = 0
    match = False
    while idx < len(secret_word):
        if char == secret_word[idx]:
            match = True
        idx += 1
    return match


def emojified(guess: str, secret: str) -> str:
    # add emojis based on if char in specific index is an exact match vs if present in the word vs if not in word (3 options!!)
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
        elif contains_char(secret_word=secret, char=guess[idx]):
            build += YELLOW_BOX
        else:
            build += WHITE_BOX
        idx += 1
    return build


def main(secret: str) -> None:
    """entrypoint of the program and main game loop"""
    # turns is a new variable to define, should only run 6 times
    turns: int = 1
    while turns < 7:
        # make it take one guess and then print result immediately after, prob need interim variable for this
        print(f"=== Turn {turns}/6 ===")
        response = input_guess(secret_word_len=len(secret))
        print(emojified(guess=response, secret=secret))
        if secret == response:
            print(f"You won in {turns}/6 turns!")
            return
        turns += 1
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
