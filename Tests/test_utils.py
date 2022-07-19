from utils import is_sorted, swap
import pytest


def test_is_sorted():
    assert is_sorted([1, 2, 4, 3]) is False
    assert is_sorted([1, 2, 4, 4, 5, 5]) is True


def test_swap():
    _ = [1, 2, 3, 4]
    swap(_, 1, 3)
    assert _ == [1, 4, 3, 2]

    _ = [4, 10, 2, 50, 1, 2000]
    swap(_, 3, 0)
    assert _ == [50, 10, 2, 4, 1, 2000]


def test_swap_failure():
    _ = [1, 2, 3, 4]

    with pytest.raises(IndexError) as excinfo:
        swap(_, 1, 4)

    exception_msg = excinfo.value.args[0]
    assert exception_msg == "** Error ** One or more indices is invalid"
