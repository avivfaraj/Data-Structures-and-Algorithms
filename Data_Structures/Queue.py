from Data_Structures.Node import Node
from typing import Optional, Generator


class Queue():

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Getters and Setters
    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, h):
        self._head = h

    @property
    def tail(self):
        return self._tail

    @tail.setter
    def tail(self, t):
        self._tail = t

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, s):
        self._size = s

    # Queue Methods
    def is_empty(self) -> bool:
        """
        Function to check if there are elements in Queue

        Return:
        True if empty, False otherwise.
        """
        if self.head is None:
            return True

        return False

    def front(self) -> Optional[int]:
        """
        Front of the Queue

        Return:
        Value of the front node in the Queue (int)
        """
        if self.head is None:
            return None

        return self.head.value

    def enqueue(self, value: int) -> None:
        """
        Insert a new node to the Queue
        """
        # New node with value, but next -> None
        newNode = Node(value)

        if self.head is None:
            self.head = newNode
            self.tail = newNode

        else:
            self.tail.next = newNode
            self.tail = newNode

        self.size += 1

    def dequeue(self) -> Optional[int]:
        """
        Remove the front node of Queue
        """
        # Empty queue
        if self.head is None:
            return None

        val = self.head.value
        # Moving to the next in line
        self.head = self.head.next
        self.size -= 1

        # Check wether its the end of the line
        if self.head is None:
            self.tail = None

        return val

    def get_item(self, pop: bool = True) -> Generator[int, bool, None]:
        """
        Generator function to iterate over nodes in Queue

        Input:
        pop -> True to remove nodes from Queue while iterating,
               False otherwise.

        Return:
        Yield value of current node (int).
        """
        helper_node = self.head

        while helper_node is not None:
            val = helper_node.value
            helper_node = helper_node.next
            if pop:
                self.dequeue()

            yield val

    def __repr__(self) -> str:
        """
        Represent the Queue in a string

        Return:
        String representation of Queue
        """
        if self.front() is None:
            return "Queue is Empty!"

        output = "Front -> "
        helper_node = self.head

        while helper_node is not None:
            output += str(helper_node.value) + " -> "
            helper_node = helper_node.next

        return output + "Tail"

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
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(20)
    q.enqueue(100)
    front = q.dequeue()

    assert len(q) == 4
    assert front == 10

    front = q.dequeue()
    assert len(q) == 3
    assert front == 20
    assert q.is_empty() is False
    assert q.front() == 30

    iterable = [i for i in q.get_item(pop=False)]
    assert len(q) == 3
    assert iterable == [30, 20, 100]
    assert q.is_empty() is False

    iterable = [i for i in q.get_item(pop=True)]
    assert len(q) == 0
    assert iterable == [30, 20, 100]
    assert q.is_empty() is True
    print("Works Fine!")


if __name__ == "__main__":
    test()
