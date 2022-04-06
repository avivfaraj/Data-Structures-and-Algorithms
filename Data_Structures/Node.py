
class Node():
	"""
	Node class for Queue and Stack.
	"""

	def __init__(self, v = None, n = None):
		self.value = v
		self.next = n

	@property
	def value(self):
		return self._value
	
	@value.setter
	def value(self, v):
		self._value = v

	@property
	def next(self):
		return self._next
	
	@next.setter
	def next(self, n):
		self._next = n



class DoubleNode():
	"""

@value.setter
	Node class for Deque. 
	"""
	def __init__(self, v = None, n = None, p = None):
		self.value = v
		self.next = n
		self.previous = p

	@property
	def value(self):
		return self._value
	
	@value.setter
	def value(self, v):
		self._value = v

	@property
	def next(self):
		return self._next
	
	@next.setter
	def next(self, n):
		self._next = n

	@property
	def previous(self):
		return self._previous
	
	@previous.setter
	def previous(self, p):
		self._previous = p



class BTNode():
	"""
	Node class for Binary Tree. 
	Similar to DoubleNode with renamed attributes:
	next, previous ----> left, right.
	"""
	def __init__(self, v = None, l = None, r = None):
		self.value = v
		self.left = l
		self.right = r


	@property
	def value(self):
		return self._value
	
	@value.setter
	def value(self, v):
		self._value = v

	@property
	def left(self):
		return self._left
	
	@left.setter
	def left(self, l):
		self._left = l

	@property
	def right(self):
		return self._right
	
	@right.setter
	def right(self, r):
		self._right = r




