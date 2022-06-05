from Node import Node
from typing import Generator, Optional


class Stack():

    def __init__(self):
        self.head = None
        self.size = 0

    # Setters and Getters
    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, h):
        self._head = h

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, s):
        self._size = s

    # Stack Methods
    def is_empty(self) -> bool:
        """
        Function to check if there are elements in the Stack

        Return:
        True if empty, False otherwise.
        """
        if self.head is None:
            return True

        return False

    def top(self) -> Optional[int]:
        """
        Top of the Stack

        Return:
        Value of the Top node in the Stack (int)
        """
        if self.head is None:
            return None

        return self.head.value

    def push(self, value: int) -> None:
        """
        Push a new node in the front of the Stack
        """
        newNode = Node(value, self.head)

        self.head = newNode
        self.size += 1

    def pop(self) -> Optional[int]:
        """
        Remove top node from the Stack

        Return:
        Value of the removed element (int). Returns None if empty
        """

        if self.head is None:
            return None

        val = self.head.value
        self.head = self.head.next
        self.size -= 1

        return val

    def get_item(self, pop: bool = True) -> Generator[int, bool, None]:
        """
        Generator function to iterate over nodes in Stack

        Input:
        pop -> True to remove nodes from Stack while iterating,
               False otherwise.

        Return:
        Yield value of current node (int).
        """
        helper_node = self.head

        while helper_node is not None:
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
    st = Stack()
    st.push(10)
    st.push(20)
    st.push(30)

    assert st.top() == 30
    assert len(st) == 3
    assert st.is_empty() is False

    st.pop()
    assert st.top() == 20
    assert st.is_empty() is False

    st.pop()
    assert len(st) == 1

    st.push(101)
    st.push(250)
    iter_wo_pop = [i for i in st.get_item(pop=False)]
    assert len(st) == 3
    assert iter_wo_pop == [250, 101, 10]

    iter_with_pop = [i for i in st.get_item(pop=True)]
    assert len(st) == 0
    assert iter_with_pop == [250, 101, 10]
    assert st.is_empty() is True

    print("Works Fine!")


if __name__ == "__main__":
    test()
