from Test import test_generators, test
from typing import List, Optional


def linear_search(arr: List[int], item: int) -> Optional[int]:

    # None if item not in arr
    if item not in arr:
        return None

    i = 0
    while i < len(arr):
        if arr[i] == item:
            return i
        i += 1


def linear_search_gen(arr: List[int], item: int) -> Optional[int]:

    i = 0
    while i < len(arr):
        if arr[i] == item:
            yield i
        i += 1

    return None


def linear_recursive(arr: List[int], item: int) -> Optional[int]:
    return recursive_iteration(arr, item, 0, len(arr) - 1)


def linear_recursive_gen(arr: List[int], item: int) -> int:
    i = -1
    while i < len(arr):
        i = recursive_iteration(arr, item, i + 1, len(arr) - 1)
        yield i


def recursive_iteration(arr: List[int],
                        item: int,
                        start: int,
                        stop: int) -> Optional[int]:

    if start > stop:
        return None

    if item == arr[start]:
        return start

    return recursive_iteration(arr, item, start + 1, stop)


if __name__ == "__main__":
    test(linear_recursive)
    test(linear_search)
    test_generators(linear_recursive_gen)
    test_generators(linear_search_gen)
