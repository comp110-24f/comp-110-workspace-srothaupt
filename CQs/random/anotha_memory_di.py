def start_end(word: str) -> str:
    return word[0] + word[len(word) - 1]


start_end(word="kitkat")
print(start_end(word="skittles"))
