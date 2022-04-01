import random, time
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

