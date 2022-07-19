from Algorithms.Sorting.MergeSort import merge_sort
from Algorithms.Sorting.QuickSort import quick_sort
from Algorithms.Sorting.InsertionSort import insertion_sort
from Algorithms.Sorting.BubbleSort import bubble_sort
from Algorithms.Sorting.RadixSort import radix_sort
from utils import is_sorted
import pytest
import random


@pytest.mark.parametrize("num, function",
                         [(10, merge_sort),
                          (100, merge_sort),
                          (10, quick_sort),
                          (100, quick_sort),
                          (10, insertion_sort),
                          (100, insertion_sort),
                          (10, bubble_sort),
                          (100, bubble_sort)])
def test_sorting(num: int, function) -> None:
    """
    Testing sorting algorithms with 10 and 100 random numbers
    """
    # Array with random numbers
    arr = [random.randrange(1, num * 2) for i in range(num)]

    # Testing quick and merge sort
    if function.__name__ in ("quick_sort", "merge_sort"):
        function(arr, 0, len(arr)-1)

    # Testing insertion and bubble sort
    else:
        function(arr)

    assert is_sorted(arr) is True,\
           f"num: {num}, function: '{function.__name__}' had a problem"


@pytest.mark.parametrize("num",
                         [10, 100])
def test_radix_sort(num: int) -> None:
    """
    Testing radix sort with 10 and 100 random numbers.
    Different function because it was implement differently
    and returns the sorted array, rather than modifying the existing array
    """
    # Array with random numbers
    arr = [random.randrange(1, num * 2) for i in range(num)]

    # Testing quick and merge sort
    assert is_sorted(radix_sort(arr)) is True,\
           f"Radix Sort had a problem with num: {num}"
