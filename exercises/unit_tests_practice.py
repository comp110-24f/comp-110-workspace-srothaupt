def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def test_is_prime_use_case() -> None:
    assert is_prime(7) is True
    assert is_prime(8) is False
