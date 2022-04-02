from Node import DoubleNode


class Deque():

	def __init__(self):
		self.head = None
		self.tail = None

	def is_empty(self) -> bool:
		if self.head == None:
			return True

		return False

	def front(self) -> int:
		if self.head == None:
			return None

		return self.head.value

	def back(self) -> int:
		if self.tail == None:
			return None

		return self.tail.value

	def push_front(self, value: int) -> None:

		# New node with value, but next,previous -> None
		newNode = DoubleNode(value)

		if self.head == None:
			self.head = newNode
			self.tail = newNode
		else:
			self.head.previous = newNode
			newNode.next = self.head
			self.head = newNode

	def push_back(self, value) -> None:

		# New node with value, but next,previous -> None
		newNode = DoubleNode(value)

		if self.tail == None:
			self.head = newNode
			self.tail = newNode
		else:
			self.tail.next = newNode
			newNode.previous = self.tail
			self.tail = newNode


	def pop_front(self) -> None:

		if self.head == None:
			return

		if self.head == self.tail:
			self.head, self.tail = None, None
			return

		self.head = self.head.next

		if self.head != None:
			self.head.previous = None

	def pop_back(self) -> None:

		if self.head == None:
			return

		if self.head == self.tail:
			self.head, self.tail = None, None
			return

		self.tail = self.tail.previous

		if self.tail != None:
			self.tail.next = None

	def get_item(self, forward = True) -> int:

		helper_node = self.head if forward else self.tail

		while helper_node != None:
			val = helper_node.value
			helper_node = (helper_node.next
						   if forward
						   else helper_node.previous
							)

			yield val


	def __repr__(self) -> None:

		if self.front() == None:
			return "Queue is Empty!"

		output = "Front -> "
		helper_node = self.head

		while helper_node != None:
			output += str(helper_node.value) + " <-> "
			helper_node = helper_node.next

		return output[:-2] + " Tail"


if __name__ == "__main__":
	q = Deque()
	q.push_front(10)
	q.push_back(20)
	q.push_back(30)
	# print(q)
	# q.push_front(40)
	# q.push_front(100)
	# q.pop_back()
	# q.pop_front()
	# q.pop_front()
	print(q)
	print([i for i in q.get_item(False)])