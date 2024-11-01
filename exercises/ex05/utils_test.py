"""utils testing"""

from utils import only_evens, sub, add_at_index
import pytest


# only evens
def test1_only_evens() -> list[int]:
    """only evens normal case - return"""
    test: list[int] = [200, 400, 301, 501]
    assert only_evens(input=test) == [200, 400]


def test2_only_evens() -> list[int]:
    """only evens edge case"""
    test: list[int] = []
    assert only_evens(input=test) == []


def test3_only_evens() -> list[int]:
    """only evens normal case - no mutate"""
    test: list[int] = [-200, -400, 301, 501]
    only_evens(input=test)
    assert test == [-200, -400, 301, 501]


# sub
def test1_sub() -> None:
    """sub normal case"""
    test: list[int] = [200, 400, 301, 501]
    assert sub(input=test, start=1, end=3) == [400, 301]


def test2_sub() -> None:
    """sub normal case - no mutate"""
    test: list[int] = [200, 400, 301, 501]
    sub(input=test, start=-4, end=6)
    assert test == [200, 400, 301, 501]


def test_sub() -> None:
    """sub edge case"""
    test: list[int] = []
    assert sub(input=test, start=5, end=3) == []


# add_at_index
def test1_add_at_index() -> None:
    """add_at_index normal case"""
    test: list[int] = [11, 12, 23, 25]
    add_at_index(input=test, element=44, idx=2)
    assert test == [11, 12, 44, 23, 25]


def test2_add_at_index() -> None:
    """add_at_index normal case - mutate"""
    test: list[int] = [4]
    add_at_index(input=test, element=5, idx=1)
    assert test == [4, 5]


def test3_add_at_index() -> None:
    """add_at_index normal case"""
    test: list[int] = [1, 2, 3, 5]
    with pytest.raises(IndexError):
        add_at_index(input=test, element=2, idx=5)
