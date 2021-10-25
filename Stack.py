from linkedList import *

class Stack:
    _storage: LinkedList
    def __init__(self) -> None:
        self.stack = LinkedList()

    def push(self, element: Any) -> None:
        self.stack.push(element)

    def pop(self) -> Any:
        self.stack.pop()

    def __len__(self):
        return len(self.stack)
        
    def __str__(self):
        s = ""
        for x in range(len(self.stack)):
            s+= str(self.stack.node(x).value)+"\n"
        return s


