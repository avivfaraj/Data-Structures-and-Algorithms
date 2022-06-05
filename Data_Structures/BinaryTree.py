from Node import BTNode
import matplotlib.pyplot as plt # type: ignore
import networkx as nx # type: ignore
from typing import Optional


class BinaryTree():

    def __init__(self):
        self.root = None

    # Getters and Setters
    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, r):
        self._root = r

    # BST Methods
    def is_empty(self) -> bool:
        """
        Function to check if there are elements in Deque

        Return:
        True if empty, False otherwise.
        """
        if self.root is None:
            return True

        return False

    def get_root(self) -> BTNode:
        """
        Function to check if there are elements in Deque

        Return:
        True if empty, False otherwise.
        """
        return self.root.value

    def height(self,
               current_node: BTNode = None,
               initial: bool = True) -> int:

        if initial:
            current_node = self.root

        if current_node is None:
            return 0

        left_height = self.height(current_node.left, False)
        right_height = self.height(current_node.right, False)

        if right_height > left_height:
            return right_height + 1

        return left_height + 1

    def find(self,
             value: int,
             current_node: BTNode = None,
             initial: bool = True) -> int:
        """
        Front of the Deque

        Return:
        Value of the front node in the Deque (int)
        """
        if initial:
            current_node = self.root

        if not current_node:
            return False

        if current_node.value == value:
            return True

        if current_node.value > value:
            return self.find(value, current_node.left, False)

        return self.find(value, current_node.right, False)

    def insert(self, value: int) -> None:

        """
        Push a new node in the front of the Deque
        """
        self.root = self.insert_recursive(value, self.root)

    def insert_recursive(self,
                         value: int,
                         current_node: BTNode) -> BTNode:
        """
        Push a new node to the end of the Deque
        """
        # New node with value, but next,previous -> None
        if current_node is None:
            return BTNode(v=value)

        if current_node.value == value:
            return current_node

        if current_node.value > value:
            current_node.left = self.insert_recursive(value,
                                                      current_node.left)
        else:
            current_node.right = self.insert_recursive(value,
                                                       current_node.right)

        return current_node

    def print(self, order: str = "pre") -> None:

        if order == "pre":
            self.preorder_rec(self.root)
        elif order == "post":
            self.postorder_rec(self.root)
        elif order == "in":
            self.inorder_rec(self.root)
        else:
            raise ValueError("No such order!")

        print()

    def preorder_rec(self, current_node: BTNode) -> None:
        if current_node:
            print(current_node.value, end=" ")
            self.preorder_rec(current_node.left)
            self.preorder_rec(current_node.right)
        else:
            print("N", end=" ")

    def postorder_rec(self, current_node: BTNode) -> None:
        if current_node:
            self.postorder_rec(current_node.left)
            self.postorder_rec(current_node.right)
            print(current_node.value, end=" ")
        else:
            print("N", end=" ")

    def inorder_rec(self, current_node: BTNode) -> None:
        if current_node:
            self.inorder_rec(current_node.left)
            print(current_node.value, end=" ")
            self.inorder_rec(current_node.right)
        else:
            print("N", end=" ")

    def min(self,
            current_node: BTNode = None,
            initial: bool = True):

        # Ensure current node points at the root at the initial run
        if initial:
            current_node = self.root

        # Tree is empty
        if not current_node:
            return None

        # Ensure minimum
        if not current_node.left:

            # Return min value
            return current_node.value

        # Lower values will be on the left
        return self.min(current_node.left, False)

    def max(self,
            current_node: BTNode = None,
            initial: bool = True) -> Optional[int]:

        # Ensure current node points at the root at the initial run
        if initial:
            current_node = self.root

        # Tree is empty
        if not current_node:
            return None

        # Ensure Maxmimum
        if not current_node.right:

            # Return min value
            return current_node.value

        # Lower values will be on the left
        return self.max(current_node.right, False)

    def delete(self,
               value: int,
               mors: bool = True) -> None:

        self.root = self.delete_value(value, self.root, mors)

    def delete_value(self,
                     value: int,
                     current_node: BTNode = None,
                     mors: bool = True) -> Optional[BTNode]:

        if not current_node:
            return None

        if current_node.value == value:
            return self.delete_node(current_node, mors)

        if current_node.value > value:
            current_node.left = self.delete_value(value,
                                                  current_node.left,
                                                  mors)

        current_node.right = self.delete_value(value, current_node.right, mors)
        return current_node

    def delete_node(self,
                    current_node: BTNode = None,
                    mors: bool = True) -> Optional[BTNode]:

        if not current_node.left:
            return current_node.right

        if not current_node.right:
            return current_node.left

        if mors:
            # Minimum of the right side
            min_value = self.min(current_node.right, False)

            current_node.value = min_value

            current_node.right = self.delete_value(min_value,
                                                   current_node.right,
                                                   mors)

        else:
            # Maximum of the left side
            max_value = self.max(current_node.left, False)

            current_node.value = max_value

            current_node.left = self.delete_value(max_value,
                                                  current_node.left,
                                                  mors)

        return current_node

    def draw_bst(self) -> None:

        # Initialize Directed Graph
        G = nx.DiGraph()

        # Recursively add nodes and edges
        # Starting from root
        self.draw_recursive(G, self.root, None)

        # Define Hierarchical graph ("dot")
        # NOTE: This line requires pygraphviz installed!
        pos = nx.nx_agraph.graphviz_layout(G, prog="dot")

        # Draw nodes, labels and edges
        nx.draw_networkx_nodes(G, pos=pos)
        nx.draw_networkx_labels(G, pos=pos)
        nx.draw_networkx_edges(G, pos=pos, edgelist=G.edges(data=True))

        # Show tree
        plt.title("Binary Search Tree Graph")
        plt.show()

    def draw_recursive(self,
                       graph,
                       current_node: BTNode,
                       prev_node: BTNode) -> None:

        if current_node:
            graph.add_node(current_node.value)

            if prev_node:

                graph.add_edge(prev_node.value,
                               current_node.value)
            if current_node.left:
                self.draw_recursive(graph, current_node.left, current_node)

            if current_node.right:
                self.draw_recursive(graph, current_node.right, current_node)


def test():
    test = BinaryTree()
    test.insert(6)
    test.insert(4)
    test.insert(10)
    test.insert(1)
    test.insert(5)
    test.insert(8)
    test.insert(12)
    test.insert(9)
    test.insert(7)
    print(test.find(5))
    print(test.min())
    print(test.get_root())
    print(test.height())
    print("Inorder: ", end="")
    test.print(order="in")
    print("Postorder: ", end="")
    test.print(order="post")
    print("Preorder: ", end="")
    test.print(order="pre")
    test.delete(6)
    test.print(order="pre")
    test.draw_bst()


if __name__ == "__main__":
    test()
