"""utils testing"""

from utils import only_evens, sub, add_at_index


# only evens
def test1_only_evens() -> list[int]:
    """only evens normal clase"""
    test: list[int] = [200, 400, 301, 501]
    assert only_evens(test) == [200, 400]


def test2_only_evens() -> list[int]:
    """only evens edge case"""
    test: list[str] = []
    assert only_evens(test) == []


def test3_only_evens() -> list[int]:
    """only evens edge case"""
    test: list[str] = [-200, -400, 301, 501]
    assert only_evens(test) == [-200, -400]


# sub
def test1_sub() -> None:
    """sub normal case"""
    test: list[int] = [200, 400, 301, 501]
    assert sub(test, 1, 3) == [400, 301]


def test2_sub() -> None:
    """sub edge case"""
    test: list[int] = [200, 400, 301, 501]
    assert sub(test, -4, 6) == [200, 400, 301, 501]


def test_sub() -> None:
    """sub edge case"""
    test: list[int] = []
    assert sub(test, 5, 3) == []


# add_at_index
def test1_add_at_index() -> None:
    """add_at_index normal case"""
    test: list[int] = [11, 12, 23, 25]
    add_at_index(test, 44, 2)
    assert test == [11, 12, 44, 23, 25]


def test2_add_at_index() -> None:
    """add_at_index edge case"""
    test: list[int] = [4]
    add_at_index(test, 5, 1)
    assert test == [4, 5]


import pytest


def test3_add_at_index() -> None:
    """add_at_index normal case"""
    test: list[int] = [1, 2, 3, 5]
    with pytest.raises(IndexError):
        add_at_index(test, 2, 5)
