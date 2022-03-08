from typing import Any, List

def insertionSort(l: List[vars]) -> None:
    n = len(l)
    for i in range(1,n):
        key = l[i]
        j = i-1
        while(j>=0 and l[j]>key):
            l[j+1]=l[j]
            j=j-1 
            l[j+1]=key

def insertionSortDesc(l: List[vars]) -> None:
    n = len(l)
    for i in range(1,n):
        key = l[i]
        j = i-1
        while(j>=0 and l[j]<key):
            l[j+1]=l[j]
            j=j-1 
            l[j+1]=key


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

insertionSort(list)
insertionSort(list2)
insertionSort(list3)
insertionSort(list4)
insertionSort(list5)
insertionSort(list6)
insertionSort(list7)
insertionSort(list8)
insertionSort(list9)
insertionSort(list10)

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

insertionSortDesc(list)
insertionSortDesc(list2)
insertionSortDesc(list3)
insertionSortDesc(list4)
insertionSortDesc(list5)
insertionSortDesc(list6)
insertionSortDesc(list7)
insertionSortDesc(list8)
insertionSortDesc(list9)
insertionSortDesc(list10)

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