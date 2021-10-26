from typing import Any

class Node:
    value: Any
    next: 'Node'
    def __init__(self, value:Any) -> None:
        self.value = value
        self.next = None

class LinkedList:
    head: Node
    tail: Node
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.num = 0

    def count(self, value):
        self.num += value

    def push(self, value:Any) -> None:
        if self.head == None:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
            self.count(1)
        else:
            newNode = Node(value)
            newNode.next = self.head
            self.head = newNode
            self.count(1)

    def append(self, value:Any) -> None:
        if self.head == None:
            self.push(value)
        else:
            newNode = Node(value)
            self.tail.next = newNode
            self.tail = newNode
            self.count(1)
         

    def node(self, at:int) -> None:
        tmp = self.head
        poz = 0
        while tmp:
            if poz == at:
                return tmp
            poz+=1
            tmp = tmp.next

    def insert(self, value: Any, after: Node) -> None:
        if after is None:
               "#self.push(value)"
        elif after == self.tail:
                self.append(value)
        else:
            newNode = Node(value)
            newNode.next = after.next
            after.next = newNode
            self.count(1)
#zwrocvu?
    def pop(self) -> Any:
        if self.head != None:
            tmp = self.head
            self.head = self.head.next
            self.count(-1)
            return tmp.value

    def remove_last(self) -> Any:
        if self.head == None:
            "return self.head"
        elif self.head.next == None:
            self.pop()
        else:
            tmp = self.head
            while tmp.next != self.tail:
                tmp = tmp.next
            ret = tmp.next
            tmp.next = None
            tmp = self.tail
            self.count(-1)
            return ret.value
          
    def remove(self, after: Node) -> Any:
        if after == self.tail:
            self.remove_last()
        else:
            perv = after
            tmp = after.next
            perv.next = tmp.next
            tmp = None
   

    def __str__(self):
        s = ''
        tmp = self.head
        while tmp:
            if tmp.next==None:
                s += f"{tmp.value}"
            else:
                s += f"{tmp.value} -> "
            tmp = tmp.next
        return s
    
    def __len__(self):
        return self.num

list_ = LinkedList()

assert list_.head == None

list_.push(1)
list_.push(0)


list_.append(9)
list_.append(10)


middle_node = list_.node(at=1)
list_.insert(5, after=middle_node) 

first_element = list_.node(at=0)
returned_first_element = list_.pop()

assert first_element.value == returned_first_element


last_element = list_.node(at=3)
returned_last_element = list_.remove_last()

assert last_element.value == returned_last_element
assert str(list_) == '1 -> 5 -> 9'

second_node = list_.node(at=1)
list_.remove(second_node)

assert str(list_) == '1 -> 5'


print(list_)

 