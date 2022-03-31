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


def is_sorted(arr: "List") -> bool:
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