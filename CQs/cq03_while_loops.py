"""September 18th challenge question with while loops"""

__author__ = "73067354"


def num_instances(phrase: str, search_char: str) -> int:
    # start with a count variable that counts number of times char appears
    # also use an index to loop through
    count: int = 0
    idx: int = 0
    while idx < len(phrase):
        if search_char == phrase[idx]:
            count += 1
        # change the index so this isn't an infinite loop!!
        idx += 1
    return count
