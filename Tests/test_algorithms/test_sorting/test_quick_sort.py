from Algorithms.Sorting.QuickSort import quick_sort
from utils import is_sorted, swap
import pytest
import random
import time
from typing import List


@pytest.mark.parametrize("num",
                         [10, 100] )
def test_quick_sort(num: int) -> None:
    """
    Run test of the quick sort algorithm

    Input:
    num   -> Number of random elements in the array

    Output:
    **
       The function prints the unsorted array,
       sorted array, and the runtime of the algorithm
    **
    """
    # Array with random numbers
    arr = [random.randrange(1, num * 2) for i in range(num)]

    # Sort
    quick_sort(arr, 0, len(arr)-1)

    assert is_sorted(arr) == True
