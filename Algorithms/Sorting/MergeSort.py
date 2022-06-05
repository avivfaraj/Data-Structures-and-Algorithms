from General import test
from typing import List


def merge(arr: List[int], start: int, middle: int, stop: int) -> None:
    """
    Merge two sorted lists

    Input:
    arr     -> Array with numerical elements
    start   -> index of the first element
    middle  -> index of the middle element
    stop    -> index of the last element
    """
    first_section = arr[start: middle + 1]
    second_section = arr[middle + 1: stop + 1]

    i, j = 0, 0

    for k in range(start, stop+1):
        if i >= len(first_section):
            arr[k] = second_section[j]
            j += 1
        elif j >= len(second_section):
            arr[k] = first_section[i]
            i += 1
        elif second_section[j] > first_section[i]:
            arr[k] = first_section[i]
            i += 1
        else:
            arr[k] = second_section[j]
            j += 1


def merge_sort(arr: List[int], start: int, stop: int) -> None:
    """
    Implementation of merge sort

    Input:
    arr     -> Array with numerical elements
    start   -> index of the first element
    stop    -> index of the last element
    """

    # Terminate recursion
    if start >= stop:
        return

    # Avoid overflow
    middle = int(start + ((stop - start) / 2))

    # Recursive iterations
    # Left
    merge_sort(arr, start, middle)
    # Right
    merge_sort(arr, middle+1, stop)

    # Merge elements
    merge(arr, start, middle, stop)


def msort(arr: List[int]):
    merge_sort(arr, 0, len(arr)-1)


if __name__ == "__main__":
    test(10, msort)
