from Node import Node

class Stack():

	def __init__(self):
		self.head = None


	def is_empty(self) -> bool:
		if self.head == None:
			return True

		return False

	def top(self) -> int:
		if self.head == None:
			return None

		return self.head.value

	def push(self, value: int) -> None:
		
		newNode = Node(value, self.head)

		self.head = newNode

	def pop(self) -> None:

		if self.head == None:
			return

		self.head = self.head.next


if __name__ == "__main__":
	st = Stack()
	st.push(10)
	st.push(20)
	st.push(35)
	print(st.top())
	st.pop()
	print(st.top())
	st.pop()
	print(st.top())



