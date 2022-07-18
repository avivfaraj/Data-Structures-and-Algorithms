from typing import List
from utils import time_sorted, swap


def insertion_sort(arr: List[int]) -> None:
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
    time_sorted(100, insertion_sort)
