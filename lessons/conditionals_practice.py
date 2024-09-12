"""Practice from 9/9 class for conditionals with Booleans."""


def check_first_letter(word: str, letter: str) -> str:
    if word[0] == letter[0]:
        return print("match!")
    else:
        return print("no match!")


check_first_letter(word="quordle", letter="q")
