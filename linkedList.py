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

    def push(self, value:Any) -> None:
        if self.head == None:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode.next
            self.num += 1
        else:
            newNode = Node(value)
            newNode.next = self.head
            self.head = newNode
            self.tail = newNode.next
            self.num += 1

    def append(self, value:Any) -> None:
        if self.head == None:
            self.push(value)
        else:
            newNode = Node(value)
            tmp = self.tail
            tmp.next = newNode
            self.tail = tmp.next
            self.num += 1
#krotsze mozna zrobic
    def node(self, at:int) -> None:
        if at<self.num:
            poz = 0
            tmp = self.head
            while(poz<at):
                tmp = tmp.next
                poz+=1
            return tmp
#if co gdyby
    def insert(self, value: Any, after: Node) -> None:
        newNode = Node(value)
        newNode.next = after.next
        after.next = newNode
        self.num += 1
#if
    def pop(self) -> Any:
        tmp = self.head
        if(tmp!=None):
            self.head = self.head.next
        self.num -= 1
        return tmp.value
#zmien
    def remove_last(self) -> Any:
        if(self.head != None):
            if(self.head.next == None):
                self.head = None
                self.num -= 1
                return self.head.value
            else:
                tmp = self.head
                while(tmp.next.next != None):
                    tmp = tmp.next
                tmpNext = tmp.next
                zm = tmp.next
                tmp.next = None
                tmpNext = None
                self.num -= 1
                self.tail = tmp
                return zm.value
#if co gdyby
    def remove(self, after: Node) -> Any:
        prv = after
        tmp = after.next
        tmpCon = tmp.next
        tmp = None
        prv.next = tmpCon
        self.num -= 1
   

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
        
'''     def len(self):
        tmp = self.head
        pozCount = 0
        while(tmp!=None):
            pozCount += 1
            tmp = tmp.next
        print("len: ", pozCount) '''


list_ = LinkedList()

assert list_.head == None

list_.push(1)
list_.push(0)


list_.append(9)
list_.append(10)
print(list_)
print(list_)
middle_node = list_.node(at=1)
list_.insert(5, after=middle_node)
print(list_)
print('\n')

first_element = list_.node(at=0)
returned_first_element = list_.pop()
assert first_element.value == returned_first_element

print(returned_first_element)

last_element = list_.node(at=3)
returned_last_element = list_.remove_last()
assert last_element.value == returned_last_element

second_node = list_.node(at=1)
list_.remove(second_node)




print(list_)
print(len(list_))

 