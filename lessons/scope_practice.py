def remove_chars(msg: str, char: str) -> str:
    copy: str = ""
    idx: int = 0
    while idx < len(msg):
        if char == msg[idx]:
            None
        else:
            copy += msg[idx]
        idx += 1
    return copy


print(remove_chars(msg="football", char="o"))


word: str = "yoyo"
print(remove_chars(word, "y"))
print(remove_chars(word, "o"))
