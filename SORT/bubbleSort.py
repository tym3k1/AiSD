from typing import Any, List


def bubbleSort(l :List[vars]) -> None:
    n = len(l)
    for i in range(n):
        for j in range(n):
            if(l[i]<l[j]):
                temp = l[i]
                l[i] = l[j]
                l[j] = temp

def bubbleSortDesc(l :List[vars]) -> None:
    n = len(l)
    for i in range(n):
        for j in range(n):
            if(l[i]>l[j]):
                temp = l[i]
                l[i] = l[j]
                l[j] = temp


list = [6, 1, 7, 3, 4, 9, 2, 5, 8, 0]
list2 = [8, 5, 4, 2, 1, 7, 9, 6, 0, 3]
list3 = [3, 4, 0, 7, 1, 5, 2, 8, 9, 6]
list4 = [3, 4, 1, 2, 5, 0, 9, 8, 6, 7]
list5 = [3, 5, 8, 7, 1, 6, 9, 4, 0, 2]
list6 = [0, 7, 9, 4, 8, 6, 5, 3, 2, 1]
list7 = [9, 2, 1, 5, 8, 0, 6, 4, 3, 7]
list8 = [4, 5, 2, 7, 0, 9, 1, 3, 6, 8]
list9 = [0, 8, 2, 7, 6, 3, 9, 1, 5, 4]
list10 = [2, 0, 7, 3, 4, 5, 8, 6, 9, 1]

bubbleSort(list)
bubbleSort(list2)
bubbleSort(list3)
bubbleSort(list4)
bubbleSort(list5)
bubbleSort(list6)
bubbleSort(list7)
bubbleSort(list8)
bubbleSort(list9)
bubbleSort(list10)

print(list)
print(list2)
print(list3)
print(list4)
print(list5)
print(list6)
print(list7)
print(list8)
print(list9)
print(list10)

bubbleSortDesc(list)
bubbleSortDesc(list2)
bubbleSortDesc(list3)
bubbleSortDesc(list4)
bubbleSortDesc(list5)
bubbleSortDesc(list6)
bubbleSortDesc(list7)
bubbleSortDesc(list8)
bubbleSortDesc(list9)
bubbleSortDesc(list10)

print(list)
print(list2)
print(list3)
print(list4)
print(list5)
print(list6)
print(list7)
print(list8)
print(list9)
print(list10)