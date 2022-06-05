import random
from General import swap
from General import test
from typing import List


def partition(arr: List[int], start: int, stop: int) -> int:
    """
    Sort part of the array around a random pivot

    Input:
    arr   -> Array with numerical elements
    start -> index of the first element
    stop  -> index of the last element

    Output:
    i     -> index of the pivot
    """
    # Random index
    random_index = random.randint(start, stop)

    # Swap random index with the last element
    swap(arr, stop, random_index)

    pivot = arr[stop]
    i = start

    # Iterate over all elements
    for j in range(start, stop):

        # Ensure smaller than pivot
        if arr[j] < pivot:

            # Swap if smaller.
            swap(arr, i, j)
            i += 1

    # Put pivot back in place
    swap(arr, i, stop)

    return i


def qsort(arr: List[int]):
    quick_sort(arr, 0, len(arr) - 1)


def quick_sort(arr: List[int], start: int, stop: int):
    """
    Recursive function that implements quick sort

    Input:
    arr   -> Array with numerical elements
    start -> index of the first element
    stop  -> index of the last element
    """
    if start < stop:
        pivot = partition(arr, start, stop)

        quick_sort(arr, start, pivot - 1)
        quick_sort(arr, pivot + 1, stop)


if __name__ == "__main__":
    test(100, qsort)
