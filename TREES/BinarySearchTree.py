from BinaryNode import *
from typing import Any, List


class BinarySearchTree:
    root: BinaryNode

    def __init__(self) -> None:
        self.root = None

    def insert(self, value: Any) -> None:
        if not self.root:
            self.root = BinaryNode(value)
        else:
            self._insert(self.root, value)
        return self.root

    def _insert(self, node: BinaryNode, value) -> BinaryNode:
        if value < node.value:
            node.left_child = BinaryNode(value)
        else:
            node.right_child = BinaryNode(value)

    def insertlist(self, list: List[Any]) -> None:
        for element in list:
            self.insert(element)

    def contains(self, value: Any) -> bool:
        if self.root.left_child is None or self.root.right_child is None:
            return False
        return self.root.contains(value)

    def remove(self, value:Any) -> None:
        if self.root is None:
            return self.root
        else:
            self._remove(self.root, value)
        return self.root

    def _remove(self, node: BinaryNode, value: Any) -> BinaryNode:
        if value < node.value:
            node.left_child = self._remove(node.left_child, value)
        elif value > self.root.value:
            node.right_child = self._remove(node.right_child, value)
        else:
            if node.left_child is None:
                tmp = node.right_child
                node.root = None
                return tmp
            elif node.right_child is None:
                tmp = node.left_child
                self.root = None
                return tmp
            
            tmp = node.right_child.min()
            node.value = tmp.value
            node.right_child = self._remove(node.right_child, tmp.value)
        return self.root


    def show(self):
        return self.root.display()

root = BinarySearchTree()
root.insert(7)
root.insert(11)
root.insert(3)
root.remove(3)

root.contains(3)

root.show()
