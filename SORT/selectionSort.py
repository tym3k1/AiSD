from typing import Any, List


def selectionSort(l :List[vars]) -> None:
    n = len(l)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if(l[j]<l[min_index]):
                min_index = j
        l[i],l[min_index]=l[min_index],l[i]

def selectionSortDesc(l :List[vars]) -> None:
    n = len(l)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if(l[j]>l[min_index]):
                min_index = j
        l[i],l[min_index]=l[min_index],l[i]

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

selectionSort(list)
selectionSort(list2)
selectionSort(list3)
selectionSort(list4)
selectionSort(list5)
selectionSort(list6)
selectionSort(list7)
selectionSort(list8)
selectionSort(list9)
selectionSort(list10)

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

selectionSortDesc(list)
selectionSortDesc(list2)
selectionSortDesc(list3)
selectionSortDesc(list4)
selectionSortDesc(list5)
selectionSortDesc(list6)
selectionSortDesc(list7)
selectionSortDesc(list8)
selectionSortDesc(list9)
selectionSortDesc(list10)

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