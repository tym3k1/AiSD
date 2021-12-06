from BinaryNode import *
from typing import Any, AnyStr, Callable, List

class BinaryTree:
    root: BinaryNode

    def __init__(self, value) -> None:
            if value != type(BinaryNode):
                self.root = BinaryNode(value)
            self.root = value

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_post_order(visit)

    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_pre_order(visit)




binaryNode = BinaryNode(10)
tree = BinaryTree(binaryNode)

assert tree.root.value == 10

binaryNode.add_left_child(6)
binaryNode.add_right_child(9)

assert tree.root.right_child.value == 9

binaryNode.left_child.add_left_child(4)
binaryNode.left_child.add_right_child(2)
binaryNode.right_child.add_left_child(0)
binaryNode.right_child.add_right_child(1)


assert tree.root.left_child.left_child.value == 4
assert tree.root.left_child.left_child.is_leaf() is True
assert tree.root.right_child.is_leaf() is False

binaryNode.left_child.left_child.add_left_child(2)
binaryNode.left_child.right_child.add_right_child(8)

binaryNode.right_child.left_child.add_right_child(3)
binaryNode.right_child.right_child.add_left_child(5)




binaryNode.display()

result = []

def all_equal_paths(tree: BinaryTree, sum_value: Any) ->List[List[BinaryNode]]:
    if tree is None:
        return result
    _all_equal_path(tree, list(), sum_value)
    return result

def _all_equal_path(node: Any, tmp: List[BinaryNode], sum_value: Any):
    if type(node) == BinaryTree:
        tmp.append(node.root.value)
        if node.root.left_child is None and node.root.right_child is None:
            if sum_value == sum(tmp):
                result.append(tmp[:])
            tmp.pop()
            return
        if node.root.left_child:
            _all_equal_path(node.root.left_child, tmp, sum_value)
        if node.root.right_child:
            _all_equal_path(node.root.right_child, tmp, sum_value)
        tmp.pop()
    else:
        tmp.append(node.value)
        if node.left_child is None and node.right_child is None:
            if sum_value == sum(tmp):
                result.append(tmp[:])
                tmp.pop()
                return
        if node.left_child:
            _all_equal_path(node.left_child, tmp, sum_value)
        if node.right_child:
            _all_equal_path(node.right_child, tmp, sum_value)
        tmp.pop()

result = all_equal_paths(tree, 22)
print(result)