from list_fns import (
    get_first,
    remove_first,
    get_and_remove,
)


def test_get_first() -> None:
    """get_first should return first element"""
    dog_breeds: list[str] = ["husky", "golden", "poodle", "lab"]
    assert get_first(dog_breeds) == "husky"


def remove_first() -> None:
    """get_first should return first element"""
    dog_breeds: list[str] = ["husky", "golden", "poodle", "lab"]
    assert remove_first(dog_breeds) == None


def test_remove_first_behavior() -> None:
    """get_first should return first element"""
    dog_breeds: list[str] = ["husky", "golden", "poodle", "lab"]
    remove_first(dog_breeds)
    assert dog_breeds == ["golden", "poodle", "lab"]


def test_get_first_edge_case() -> None:
    assert get_first([]) == ""


# /workspace/lessons/unit_tests/list_fns_test.py
