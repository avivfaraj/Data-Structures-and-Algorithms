from General import is_sorted
from typing import List
import math
from collections import defaultdict


def radix_sort(arr: List[int]) -> List[int]:
    """
    Implementation of Radix Sort

    Input:
    arr -> array to be sorted
    """
    num_digits = math.floor(math.log10(max(arr))) + 1

    for i in range(0, num_digits):
        dict_ = defaultdict(list)
        for j in arr:
            dig = j // (10 ** (i)) % 10
            dict_[dig].append(j)

        arr = []
        for k in range(0, 10):
            arr.extend(dict_[k])

        del dict_

    return arr


if __name__ == "__main__":
    arr = [1234, 4080, 200, 5010, 203, 40002]
    arr = radix_sort(arr)
    print(is_sorted(arr))
