import random
import time

def swap(arr: "List", a: int, b: int) -> None:
	"""
	Swap elements in an array

	Input:
	arr -> Array with numerical elements
	a   -> index of the first element
	b   -> index of the second element
	"""

	ind_ls = [i for i in range(0,len(arr))]
	if a in ind_ls and b in ind_ls:
		# Swap array's elements in indices a,b
		arr[a], arr[b] = arr[b], arr[a]
	else:
		print("** Error ** One or more indices is invalid")


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