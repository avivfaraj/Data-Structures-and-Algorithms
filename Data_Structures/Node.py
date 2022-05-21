class Node():
    """
    Node class for Queue and Stack.
    """

    def __init__(self, v=None, n=None):
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
    Node class for Deque.
    """
    def __init__(self, v=None, n=None, p=None):
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
    def __init__(self, v=None, left=None, right=None):
        self.value = v
        self.left = left
        self.right = right

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = val

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, left):
        self._left = left

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, right):
        self._right = right
