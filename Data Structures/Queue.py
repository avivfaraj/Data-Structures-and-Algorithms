from Node import Node

class Queue():

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

	def enqueue(self, value: int) -> None:

		# New node with value, but next -> None
		newNode = Node(value)

		if self.head == None:
			self.head = newNode
			self.tail = newNode

		else:
			self.tail.next = newNode
			self.tail = newNode

	def dequeue(self) -> None:

		# Empty queue 
		if self.head == None:
			return

		# Moving to the next in line
		self.head = self.head.next

		# Check wether its the end of the line
		if self.head == None:
			self.tail = None


	def __repr__(self) -> None:

		

		if self.front() == None:
			return "Queue is Empty!"

		output = "Head -> "
		helper_node = self.head

		while helper_node != None:
			output += str(helper_node.value) + " -> " 
			helper_node = helper_node.next

		return output + "Tail"


if __name__ == "__main__":
	q = Queue()
	q.enqueue(10)
	q.enqueue(20)
	q.enqueue(30)
	q.enqueue(20)
	q.enqueue(100)

	print(q)



