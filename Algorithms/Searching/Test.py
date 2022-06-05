from typing import NewType, Callable, List, Optional, Generator
Function = NewType("Function", "function")


def test(fun: Callable[[List[int], int], Optional[int]]) -> None:
    arr = [1, 10, 2, 30, 50, 4, 100, 3, 8]
    assert fun(arr, 4) == 5
    assert fun(arr, 100) == 6
    assert fun(arr, 8) == 8


def test_generators(fun: Callable[[List[int], int],
                                  Generator[Optional[int],
                                            None,
                                            None]]) -> None:
    arr = [1, 10, 2, 30, 50, 4, 100, 2, 8]
    i = fun(arr, 2)
    assert next(i) == 2
    assert next(i) == 7

    i = fun(arr, 10)
    assert next(i) == 1


def test_sorted(fun: Callable[[List[int], int], Optional[int]]) -> None:
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    assert fun(arr, 4) == 3
    assert fun(arr, 8) == 7
