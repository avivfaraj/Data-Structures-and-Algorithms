from Node import BTNode


class BinaryTree():

	def __init__(self):
		self.root = None

	## Getters and Setters

	@property
	def root(self):
		return self._root
	
	@root.setter
	def root(self, r):
		self._root = r

	## BST Methods
	def is_empty(self) -> bool:
		"""
		Function to check if there are elements in Deque

		Return:
		True if empty, False otherwise.
		"""
		if self.root == None:
			return True

		return False


	def get_root(self) -> "BTNode":
		"""
		Function to check if there are elements in Deque

		Return:
		True if empty, False otherwise.
		"""
		return self.root.value

	def height(self) -> int:
		return self.tree_height(self.root)

	def tree_height(self, current_node: "BTNode") -> int:

		if current_node == None:
			return 0

		left_height = self.tree_height(current_node.left)
		right_height = self.tree_height(current_node.right)

		if right_height > left_height:
			return right_height + 1

		return left_height + 1

	def find(self, value) -> int:
		"""
		Front of the Deque

		Return:
		Value of the front node in the Deque (int)
		"""
		return self.find_recursive(value, self.root)

	def find_recursive(self, value: int, current_node: "BTNode") -> int:
		"""
		Back of the Deque

		Return:
		Value of the last node in the Deque (int)
		"""

		if current_node == None:
			return False

		if current_node.value == value:
			return True

		if current_node.value > value:
			return self.find_recursive(value, current_node.left)

		return self.find_recursive(value, current_node.right)

	def insert(self, value: int) -> None:

		"""
		Push a new node in the front of the Deque
		"""

		# New node with value, but next,previous -> None
		self.root = self.insert_recursive(value, self.root)


	def insert_recursive(self, value: int, current_node: "BTNode") -> None:
		"""
		Push a new node to the end of the Deque
		"""
		# New node with value, but next,previous -> None
		if current_node == None:
			return BTNode(v = value)

		if current_node.value == value:
			return current_node

		if current_node.value > value:
			current_node.left = self.insert_recursive(value, current_node.left)
		else:
			current_node.right = self.insert_recursive(value, current_node.right)

		return current_node


	def print(self, order : str = "pre") -> str:

		if order == "pre":
			self.preorder_rec(self.root)
		elif order == "post":
			self.postorder_rec(self.root)
		elif order == "in":
			self.inorder_rec(self.root)
		else:
			raise ValueError("No such order!")

		print()



	def preorder_rec(self, current_node : "BTNode") -> None:
		if current_node:
			print(current_node.value, end = " ")
			self.preorder_rec(current_node.left)
			self.preorder_rec(current_node.right)
		else:
			print("N", end = " ")



	def postorder_rec(self, current_node : "BTNode") -> None:
		if current_node:
			self.postorder_rec(current_node.left)
			self.postorder_rec(current_node.right)
			print(current_node.value, end = " ")
		else:
			print("N", end = " ")

	def inorder_rec(self, current_node : "BTNode") -> None:
		if current_node:
			self.inorder_rec(current_node.left)
			print(current_node.value, end = " ")
			self.inorder_rec(current_node.right)
		else:
			print("N", end = " ")



# def test() -> None:
# 	"""
# 	Run tests on Queue class
# 	"""
# 	de = Deque()
# 	de.push_front(10)
# 	de.push_front(20)
# 	de.push_back(30)
# 	de.push_front(101)
# 	de.push_back(202)

# 	assert len(de) == 5
# 	assert de.front() == 101
# 	assert de.back() == 202

# 	back = de.pop_back()
# 	assert back == 202
# 	assert len(de) == 4

# 	front = de.pop_front()
# 	assert front == 101
# 	assert len(de) == 3

# 	# Iterable - Forward without pop
# 	iter_wo_pop = [i for i in de.get_item(forward = True,pop = False)]
# 	assert len(de) == 3
# 	assert iter_wo_pop == [20, 10, 30]
# 	assert de.is_empty() == False

# 	# Iterable - Reverse without pop
# 	iter_wo_pop = [i for i in de.get_item(forward = False,pop = False)]
# 	assert len(de) == 3
# 	assert iter_wo_pop == [30, 10, 20]
# 	assert de.is_empty() == False

# 	# Iterable - Forward with pop
# 	iter_wo_pop = [i for i in de.get_item(forward = True,pop = True)]
# 	assert len(de) == 0
# 	assert iter_wo_pop == [20, 10, 30]
# 	assert de.is_empty() == True

# 	# Iterable - Reverse with pop
# 	de.push_front(30)
# 	de.push_front(10)
# 	de.push_front(40)
# 	iter_wo_pop = [i for i in de.get_item(forward = False,pop = True)]
# 	assert len(de) == 0
# 	assert iter_wo_pop == [30, 10, 40]
# 	assert de.is_empty() == True

# 	print("Works Fine!")

if __name__ == "__main__":
	test = BinaryTree()
	test.insert(6)
	test.insert(4)
	test.insert(10)
	test.insert(1)
	test.insert(5)
	test.insert(8)
	test.insert(12)
	print(test.get_root())
	print(test.height())
	print("Inorder: ", end = "")
	test.print(order = "in")
	print("Postorder: ", end = "")
	test.print(order = "post")
	print("Preorder: ", end = "")
	test.print(order = "pre")