"""EX02 - Chardle. A cute step toward Wordle."""

__author__ = "730673654"


def input_word() -> str:
    user_word = input("Enter a 5-character word: ")
    if len(user_word) == 5:
        return user_word
    else:
        print("Error: Word must contain 5 characters.")
        exit()
        return user_word


def input_letter() -> str:
    user_char = input("Enter a single character: ")
    if len(user_char) == 1:
        return user_char
    else:
        print("Error: Character must be a single character.")
        exit()
        return user_char


# print("Searching for" + input_letter + "in" + input_word)


def contains_char(word: str, letter: str) -> None:
    print("Searching for", letter, "in", word)
    count = 0
    if word[0] == letter:
        print(letter, "found at index 0")
        count = count + 1
    if word[1] == letter:
        print(letter, "found at index 1")
        count = count + 1
    if word[2] == letter:
        print(letter, "found at index 2")
        count = count + 1
    if word[3] == letter:
        print(letter, "found at index 3")
        count = count + 1
    if word[4] == letter:
        print(letter, "found at index 4")
        count = count + 1
    if count == 0:
        print("No instances of", letter, "found in", word)
    if count != 0:
        print(count, "instances of", letter, "found in", word)


# contains_char(word="kitty", letter="k")


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
