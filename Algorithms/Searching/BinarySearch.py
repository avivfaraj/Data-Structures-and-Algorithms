from Test import test_sorted
from typing import Optional, List

def binary_search(arr: List, item: int) -> Optional[int]:
	
	start, stop = 0, len(arr) - 1

	while start <= stop:

		# Avoid overflow
		middle = int(start + (stop - start) / 2)

		if item == arr[middle]:
			return middle

		if item < arr[middle]:
			stop = middle - 1

		else:
			start = middle + 1

	return None

	

def binary_recursive(arr: List, item: int) -> Optional[int]:
	return recursive_iteration(arr, item, 0, len(arr) - 1)


def recursive_iteration(arr: List, item: int, start: int, stop: int) -> Optional[int]:

	if start > stop:
		return

	middle = int(start + (stop - start) / 2)

	if item == arr[middle]:
		return middle

	if item < arr[middle]:
		return recursive_iteration(arr, item, start, middle - 1)

	return recursive_iteration(arr, item, middle + 1, stop)

if __name__ == "__main__":
	test_sorted(binary_search)
	test_sorted(binary_recursive)
