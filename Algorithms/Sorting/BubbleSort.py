import random
import time
from General import swap, is_sorted, test


def bubble_sort(arr: "List") -> None:
	"""
	Function that implements Bubble Sort O(n^2)

	Input:
	arr -> array to be sorted
	"""

	size = len(arr)

	# Iteration until array is sorted
	swapped = True
	while swapped:

		swapped = False

		# Iteration over elements
		for i in range(1, size):

			# Ensure unsorted
			if arr[i-1] > arr[i]:

				# Swap and continue loop
				swap(arr, i-1, i)
				swapped = True


if __name__ == "__main__":
	test(1000, bubble_sort)