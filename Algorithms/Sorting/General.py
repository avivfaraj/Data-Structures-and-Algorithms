import random
import time
from typing import List, Callable


def swap(arr: List[int], a: int, b: int) -> None:
    """
    Swap elements in an array

    Input:
    arr -> Array with numerical elements
    a   -> index of the first element
    b   -> index of the second element
    """

    ind_ls = [i for i in range(0, len(arr))]
    if a in ind_ls and b in ind_ls:
        # Swap array's elements in indices a,b
        arr[a], arr[b] = arr[b], arr[a]
    else:
        print("** Error ** One or more indices is invalid")


def is_sorted(arr: List[int]) -> bool:
    """
    Check wether an array is sorted or not

    Input:
    arr   -> Array with numerical elements

    Returns:
    True if the array is sorted, False otherwise.
    """
    i = 1
    while(i < len(arr)):
        if(arr[i] < arr[i-1]):
            return False
        i += 1

    return True


def test(num: int, fun: Callable[[List[int]], None]) -> None:
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

    # Print array before sorting
    print(f"Unsorted array: {arr}")
    print()
    # Measure time of sorting
    start = time.time()

    # Sort
    fun(arr)

    # Measure time of sorting
    stop = time.time()

    if is_sorted(arr):
        # Print sorted array
        print(f"Sorted Array: {arr}")
        print()
        print(f"Runtime: {stop-start:.2f} seconds")
    else:
        print("Something went wrong....")
