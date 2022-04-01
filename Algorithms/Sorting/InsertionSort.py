import random
import time
from General import swap, is_sorted

def insertion_sort(arr: "List") -> None:
	"""
	Function that implements Insertion Sort O(n^2)

	Input:
	arr -> array to be sorted
	"""
	size = len(arr)

	for i in range(1, size):

		for j in range(i,0, -1):

			if arr[j-1] > arr[j]:
				swap(arr, j-1, j)				

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
	insertion_sort(arr)

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
	test(500)