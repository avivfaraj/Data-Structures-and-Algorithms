import random
import time
from General import swap, is_sorted, test


def partition(arr: "List", start: int, stop: int) -> int:
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
	random_index = random.randint(start,stop)

	# Swap random index with the last element 
	swap(arr, stop, random_index)

	pivot = arr[stop]
	i = start

	# Iterate over all elements 
	for j in range(start, stop):
		
		# Ensure smaller than pivot
		if arr[j] < pivot:

			# Swap if smaller.
			swap(arr,i,j)
			i += 1

	# Put pivot back in place
	swap(arr,i,stop)

	return i


def quick_sort(arr: "List", start: int, stop: int):
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


def test(num: int) -> None:

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
	arr = [random.randrange(1,num * 2) for i in range(num)]

	# Print array before sorting
	print(f"Unsorted array: {arr}")
	print()
	# Measure time of sorting
	start = time.time()

	# Sort
	quick_sort(arr, 0, len(arr)-1)

	# Measure time of sorting
	stop = time.time()

	if is_sorted(arr):
		# Print sorted array
		print(f"Sorted Array: {arr}")
		print()
		print(f"Runtime: {stop-start:.2f} seconds")
	else:
		print("Something went wrong....")



if __name__ == "__main__":
	test(1000)