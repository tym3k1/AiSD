from linkedList import *

class Stack:
    _storage: LinkedList
    def __init__(self) -> None:
        self.stack = LinkedList()

    def push(self, element: Any) -> None:
        self.stack.push(element)

    def pop(self) -> Any:
        return self.stack.pop()

    def __len__(self):
        return len(self.stack)
        
    def __str__(self):
        s = ""
        for x in range(len(self.stack)):
            s+= str(self.stack.node(x).value)+"\n"
        return s



stack = Stack()

stack.push(3)
stack.push(10)
stack.push(1)

assert len(stack) == 3

top_value = stack.pop()

assert top_value == 1


assert len(stack) == 2


print(stack)
