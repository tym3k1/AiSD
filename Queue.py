from linkedList import *

class Queue:
    def __init__(self) -> None:
        self.queue = LinkedList()

    def peek(self) -> Any:
        return self.queue.head.value

    def enqueue(self, element: Any) -> None:
        self.queue.append(element)

    def dequeue(self) -> Any:
        self.queue.pop()

    def __len__(self):
        return len(self.queue)

    def __str__(self):
        strng = ""
        for x in range(len(self.queue)):
            strng+= str(self.queue.node(x).value)+", "
        return strng




queue = Queue()
assert len(queue) == 0
queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')
print(queue)


client_first = queue.dequeue()
print(client_first)
assert client_first == 'klient1'
assert str(queue) == 'klient2, klient3'
assert len(queue) == 2



