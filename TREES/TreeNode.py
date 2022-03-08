from typing import Any, List, Callable, Union
import queue 
#import pptree
import random
import string

class TreeNode:
    value: Any
    parent: 'TreeNode'
    children: List['TreeNode']

    def __init__(self, value: Any, parent = None):
        self.value = value
        self.parent = parent
        self.children = []

    def is_leaf(self) -> bool:
        if self.children == []:
            return True
        return False

    def is_root(self):
        if self.parent is None:
            return True
        else:
            return False

    def depth(self):    # Depth of current node
        if self.is_root():
            return 0
        else:
            return 1 + self.parent.depth()

    def add(self, child: 'TreeNode') -> None:
        child.parent = self
        self.children.append(child)
        

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)
        for i in self.children:
            i.for_each_deep_first(visit)


    def search(self, data):
        if self.value==data:
            return 
        else:
            for x in self.children:
                if x.value==data:
                    return 
        return 

    def __str__(self):
        s = ''
        s += str(self.value)
        return s



""" tri = TreeNode(3)
tri1 = TreeNode(4)
tri2 = TreeNode(5)
print(tri.is_leaf())
tri1.add(TreeNode(7))
tri1.add(TreeNode(8))
tri.add(tri1)
print(tri1.is_leaf())
tri.add(tri2)
print(tri2.is_leaf())
tri.for_each_deep_first(print)
print(tri.search(11)) """


    