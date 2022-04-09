from Node import DoubleNode

class DoublyLinkedList():

	def __init__(self):
		self.head = None
		self.last = None
		self.size = 0

	## Getters and Setters

	@property
	def head(self):
		return self._head
	
	@head.setter
	def head(self, h):
		self._head = h

	@property
	def last(self):
		return self._last
	
	@last.setter
	def last(self, l):
		self._last = l

	@property
	def size(self):
		return self._size
	
	@size.setter
	def size(self, s):
		self._size = s


	## LinkedList Methods

	def is_empty(self) -> bool:
		"""
		Check if the list is empty

		Return:
		True if empty, False otherwise.
		"""
		if self.head == None:
			return True

		return False

	def insert(self, value: int) -> None:
		"""
		Insert a new element to the list

		"""
		new_node = DoubleNode(v = value)
		if self.head:
			new_node.next = self.head
			self.head.previous = new_node
			self.head = new_node

		else:
			self.head = new_node
			self.last = new_node

		self.size += 1

	def delete(self, value: int = None, front = False) -> bool:
		"""
		Delete an item from the list

		Return:
		True if item was deleted, False otherwise.
		"""

		if value:
			try:
				node = self.search_rec(value, self.head)
			except TypeError:
				return False

			if node.previous:
				temp_node = node.previous
				temp_node.next = node.next

				temp_node = node.next
				if temp_node:
					temp_node.previous = node.previous
				else:
					self.last = node.previous

				del node
				self.size -= 1
				return True
			else:
				front = True

		if front:
			node = self.head
			self.head = self.head.next
			self.head.previous = None
			del node
			self.size -= 1
			return True

		return False


	def display(self, current_node = None, initial = True, forward = True) -> None:

		"""
		 Recursive function that prints the items in the linked list.
		"""
		if initial:
			if forward:
				current_node = self.head
				print("Head ->", end = " ")
			else:
				current_node = self.last
				print("Last ->", end = " ")

		if current_node != None:
			if (forward and current_node.next) or (not forward and current_node.previous):
				print(str(current_node.value), end = " <-> ")
			else:
				print(str(current_node.value), end = "\n")

			if forward:
				self.display(current_node.next, False, True)
			else:
				self.display(current_node.previous, False, False)


	def search_rec(self, value: int, current_node = None, previous_node = None) -> DoubleNode:

		"""
		Search an element in the linked list

		Return:
		Tuple(Current Node, Previous Node). 

		NOTE: The method returns tuple because it is being utilized 
		in delete method where the previous node is required.
		"""

		# Ensure end of list
		if not current_node:
			# Item does not exist
			return None

		# Ensure item exists 
		if current_node.value == value:
			return current_node
		
		# Recursive call 
		return self.search_rec(value, current_node.next, current_node)

	def search(self, value: int) -> bool:
		"""
		Search an element in the linked list

		Return:
		True if element exists in the list, False otherwise.
		"""
		node = self.search_rec(value, self.head)

		if node:
			return True

		return False

	def print_last(self):
		print(self.last.value) 

	def iter_items(self, forward = True) -> int:
		"""
		Generator function to iterate over nodes in Deque

		Input:
		forward -> True to start at the Front and move toward the end,
				   False to start at the End and move backward to the front

		pop     -> Remove nodes from Deque while iterating if True. 
		Return:
		Yield value of current node (int).
		"""
		if forward:
			current_node = self.head
		else:
			current_node = self.last

		while current_node:
			yield current_node.value

			if forward:
				current_node = current_node.next
			else:
				current_node = current_node.previous

	def __repr__(self) -> None:
		"""
		Represent the Deque in a string

		Return:
		String representation of Deque
		"""
		if self.head == None:
			return "List is Empty!"

		output = "Head -> "
		helper_node = self.head

		while helper_node != None:
			output += str(helper_node.value) + " <-> "
			helper_node = helper_node.next

		return output[:-4]


	def __len__(self) -> int:
		"""
		Return:
		Length of the Deque (int)
		"""
		return self.size



def test() -> None:
	"""
	Run tests on Queue class
	"""
	doubly_ls = DoublyLinkedList()

	assert doubly_ls.is_empty() == True
	doubly_ls.insert(10)
	doubly_ls.insert(20)
	doubly_ls.insert(30)
	assert doubly_ls.delete(10) == True
	print(doubly_ls)
	doubly_ls.display(forward = False)
	doubly_ls.display(forward = True)

	assert len(doubly_ls) == 2
	i = doubly_ls.iter_items(forward = False)
	assert next(i) == 20
	assert next(i) == 30

	doubly_ls.insert(50)
	doubly_ls.insert(100)

	# Reverse iteration
	for j, k in zip(doubly_ls.iter_items(forward = False),[20, 30, 50, 100]):
		assert j == k

	# Forward iteration
	for j, k in zip(doubly_ls.iter_items(forward = True),[100, 50, 30, 20]):
		assert j == k

	assert doubly_ls.search(10) == False
	assert doubly_ls.search(20) == True
	assert doubly_ls.is_empty() == False
	
	# print(lls)
	print("Works Fine!")

if __name__ == "__main__":
	test()

