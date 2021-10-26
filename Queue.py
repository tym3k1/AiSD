from linkedList import *

class Queue:
    def __init__(self) -> None:
        self.queue = LinkedList()

    def peek(self) -> Any:
        return self.queue.tail.value

    def enqueue(self, element: Any) -> None:
        self.queue.append(element)

    def dequeue(self) -> Any:
        return self.queue.pop()

    def __len__(self):
        return len(self.queue)

    def __str__(self):
        s = ""
        for x in range(len(self.queue)):
            if x == len(self.queue)-1:
                s+= str(self.queue.node(x).value)
            else:
                s+= str(self.queue.node(x).value)+", "
        return s + str(self.queue.tail.value)


queue = Queue()


assert len(queue) == 0

queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')

assert str(queue) == 'klient1, klient2, klient3'
print(queue.peek)
client_first = queue.dequeue()

assert client_first == 'klient1'
assert str(queue) == 'klient2, klient3'
assert len(queue) == 2

print(queue)