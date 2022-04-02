from Node import Node

class Stack():

	def __init__(self):
		self.head = None
		self.size = 0

	def is_empty(self) -> bool:
		"""
		Function to check if there are elements in the Stack

		Return:
		True if empty, False otherwise.
		"""
		if self.head == None:
			return True

		return False

	def top(self) -> int:
		"""
		Top of the Stack

		Return:
		Value of the Top node in the Stack (int)
		"""
		if self.head == None:
			return None

		return self.head.value

	def push(self, value: int) -> None:
		"""
		Push a new node in the front of the Stack
		"""
		newNode = Node(value, self.head)

		self.head = newNode
		self.size += 1

	def pop(self) -> int:
		"""
		Remove top node from the Stack

		Return:
		Value of the removed element (int). Returns None if empty
		"""

		if self.head == None:
			return

		val = self.head.value
		self.head = self.head.next
		self.size -=1

		return val

	def get_item(self, pop = True) -> int:
		"""
		Generator function to iterate over nodes in Stack

		Input:
		pop -> True to remove nodes from Stack while iterating, False otherwise.
		
		Return:
		Yield value of current node (int).
		"""
		helper_node = self.head

		while helper_node != None:
			val = helper_node.value
			helper_node = helper_node.next
			if pop:
				self.pop()

			yield val

	def __repr__(self) -> str:
		"""
		Represent the Stack in a string

		Return:
		String representation of the Stack
		"""
		if self.size == 0:
			return "Stack is Empty!"

		output = "Front -> "
		helper_node = self.head

		while helper_node != None:
			output += str(helper_node.value) + " -> " 
			helper_node = helper_node.next

		return output + "Tail"

	def __len__(self) -> int:
		"""
		Return:
		Length of the Deque (int)
		"""
		return self.size




if __name__ == "__main__":
	st = Stack()
	st.push(10)
	st.push(20)
	st.push(35)
	print(st)
	print(st.top())
	print(st.pop())
	print(st.top())
	st.pop()
	print(st.top())
	print(len(st))
	print([i for i in st.get_item(pop = False)])
	assert len(st) == 1



