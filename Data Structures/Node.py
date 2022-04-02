
class Node():

	def __init__(self, v = None, n = None):
		self.value = v
		self.next = n


class DoubleNode():

	def __init__(self, v = None, n = None, p = None):
		self.value = v
		self.next = n
		self.previous = p
