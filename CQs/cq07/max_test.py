__author__ = "730673654"

from find_max import find_and_remove_max


# make 3 tests, one edge and two normal. normal should check return & mutate thing
def test1_find_and_remove_max() -> None:
    """use case - return value"""
    test: list[int] = [11, 12, 23, 25]
    assert find_and_remove_max(test) == 25


def test2_find_and_remove_max() -> None:
    """use case - mutate value"""
    test: list[int] = [-10, 25, 12, 23, 25]
    find_and_remove_max(test)
    assert test == [-10, 12, 23]


def test3_find_and_remove_max() -> None:
    """edge case"""
    test: list[int] = []
    assert find_and_remove_max(test) == -1
