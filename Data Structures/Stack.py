from Node import Node

class Stack():

	def __init__(self):
		self.head = None
		self.size = 0

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
		self.size += 1

	def pop(self) -> None:

		if self.head == None:
			return

		self.head = self.head.next
		self.size -=1 

	def __repr__(self) -> str:
		pass

	def __len__(self) -> int:
		return self.size




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
	print(len(st))


