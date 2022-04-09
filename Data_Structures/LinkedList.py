from Node import Node
from typing import Tuple

class LinkedList():

	def __init__(self):
		self.head = None
		self.size = 0

	## Getters and Setters

	@property
	def head(self):
		return self._head
	
	@head.setter
	def head(self, h):
		self._head = h

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
		new_node = Node(v = value)
		if self.head:
			new_node.next = self.head
			self.head = new_node
		else:
			self.head = new_node

	def delete(self, value: int = None, front = False) -> bool:
		"""
		Delete an item from the list

		Return:
		True if item was deleted, False otherwise.
		"""

		if value:
			try:
				node, prev_node = self.search_rec(value, self.head)
			except TypeError:
				return False

			if prev_node:
				prev_node.next = node.next
				del node
				return True
			else:
				front = True

		if front:
			node = self.head
			self.head = self.head.next
			del node
			return True

		return False





	def display(self, current_node = None, initial = True) -> None:

		"""
		 Recursive function that prints the items in the linked list.
		"""
		if initial:
			current_node = self.head
			print("Head ->", end = " ")

		
		if current_node != None:
			if current_node.next:
				print(str(current_node.value), end = " -> ")
			else:
				print(str(current_node.value), end = "\n")
			self.display(current_node.next, False)

	def search_rec(self, value: int, current_node = None, previous_node = None) -> Tuple[Node,Node]:

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
			return (current_node, previous_node)
		
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

	def iter_items(self) -> int:
		"""
		Generator function to iterate over nodes in Deque

		Input:
		forward -> True to start at the Front and move toward the end,
				   False to start at the End and move backward to the front

		pop     -> Remove nodes from Deque while iterating if True. 
		Return:
		Yield value of current node (int).
		"""
		current_node = self.head

		while current_node:
			yield current_node.value
			current_node = current_node.next

	def __repr__(self) -> None:
		"""
		Represent the Deque in a string

		Return:
		String representation of Deque
		"""
		if self.front() == None:
			return "Queue is Empty!"

		output = "Front -> "
		helper_node = self.head

		while helper_node != None:
			output += str(helper_node.value) + " <-> "
			helper_node = helper_node.next

		return output[:-2] + " Tail"


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
	# de = Deque()
	# de.push_front(10)
	# de.push_front(20)
	# de.push_back(30)
	# de.push_front(101)
	# de.push_back(202)

	# assert len(de) == 5
	# assert de.front() == 101
	# assert de.back() == 202

	# back = de.pop_back()
	# assert back == 202
	# assert len(de) == 4

	# front = de.pop_front()
	# assert front == 101
	# assert len(de) == 3

	# # Iterable - Forward without pop
	# iter_wo_pop = [i for i in de.get_item(forward = True,pop = False)]
	# assert len(de) == 3
	# assert iter_wo_pop == [20, 10, 30]
	# assert de.is_empty() == False

	# # Iterable - Reverse without pop
	# iter_wo_pop = [i for i in de.get_item(forward = False,pop = False)]
	# assert len(de) == 3
	# assert iter_wo_pop == [30, 10, 20]
	# assert de.is_empty() == False

	# # Iterable - Forward with pop
	# iter_wo_pop = [i for i in de.get_item(forward = True,pop = True)]
	# assert len(de) == 0
	# assert iter_wo_pop == [20, 10, 30]
	# assert de.is_empty() == True

	# # Iterable - Reverse with pop
	# de.push_front(30)
	# de.push_front(10)
	# de.push_front(40)
	# iter_wo_pop = [i for i in de.get_item(forward = False,pop = True)]
	# assert len(de) == 0
	# assert iter_wo_pop == [30, 10, 40]
	# assert de.is_empty() == True

	# print("Works Fine!")

if __name__ == "__main__":
	# 
	lls = LinkedList()
	lls.insert(10)
	lls.insert(20)
	lls.insert(30)
	# print(lls.delete(20))
	# lls.display()
	# print(lls.search(10))
	for i in lls.iter_items():
		print(i)

