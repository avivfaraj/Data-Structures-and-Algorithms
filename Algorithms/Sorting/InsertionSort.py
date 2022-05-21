from typing import List
from General import swap
from General import test


def insertion_sort(arr: List) -> None:
    """
    Function that implements Insertion Sort O(n^2)

    Input:
    arr -> array to be sorted
    """
    size = len(arr)

    for i in range(1, size):

        for j in range(i, 0, -1):

            if arr[j-1] > arr[j]:
                swap(arr, j-1, j)


if __name__ == "__main__":
    test(1000, insertion_sort)
