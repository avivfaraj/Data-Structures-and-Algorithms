from typing import NewType, Callable, List, Optional, Generator
from Algorithms.Searching.BinarySearch import binary_search, binary_recursive
from Algorithms.Searching.LinearSearch import linear_search, linear_search_gen, linear_recursive, linear_recursive_gen
import pytest


@pytest.mark.parametrize("fun",
                         [linear_search,
                          linear_recursive])
def test_linear(fun: Callable[[List[int], int], Optional[int]]) -> None:
    arr = [1, 10, 2, 30, 50, 4, 100, 3, 8]
    assert fun(arr, 4) == 5
    assert fun(arr, 100) == 6
    assert fun(arr, 8) == 8


@pytest.mark.parametrize("fun",
                         [linear_recursive_gen,
                          linear_search_gen])
def test_generators(fun: Callable[[List[int], int],
                                  Generator[Optional[int],
                                            None,
                                            None]]) -> None:
    arr = [1, 10, 2, 30, 50, 4, 100, 2, 8]
    i = fun(arr, 2)
    assert next(i) == 2
    assert next(i) == 7

    # Checking for StopIteration raised by generator
    _ = -1
    try:
        _ = next(i)
    except StopIteration:
        assert _ == -1

    # Look for a different number
    i = fun(arr, 10)
    assert next(i) == 1

@pytest.mark.parametrize("fun",
                         [binary_search,
                          binary_recursive])
def test_binary(fun: Callable[[List[int], int], Optional[int]]) -> None:
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    assert fun(arr, 4) == 3
    assert fun(arr, 8) == 7
    assert fun(arr, 12) == None
