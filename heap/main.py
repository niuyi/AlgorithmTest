import random

initList = [25, 20, 22, 17, 19, 10, 12, 15, 7, 9, 18]
random.shuffle(initList)

# initList = [1, 2]
heap = []


def changeOrder(myHeap, index):
    if index == 0:
        return

    last = myHeap[index]
    parentIndex = (index - 1) / 2
    parent = myHeap[parentIndex]

    if last > parent:
        myHeap[parentIndex] = last
        myHeap[index] = parent
        changeOrder(myHeap, parentIndex)


def insertToHeap(myHeap, value):
    myHeap.append(value)
    changeOrder(myHeap, len(myHeap) - 1)


def extractFromHeap(myHeap):
    heap_size = len(myHeap)

    if heap_size == 0:
        return -1

    header = myHeap[0]
    myHeap[0] = myHeap[-1]
    del myHeap[-1]

    heap_size = len(myHeap)

    start = 0

    while True:
        left_pos = start * 2 + 1
        right_pos = start * 2 + 2
        to_change = start

        if (left_pos <= heap_size - 1) and (myHeap[left_pos] > myHeap[start]):
            to_change = left_pos
        else:
            to_change = start

        if (right_pos <= heap_size - 1) and (myHeap[right_pos] > myHeap[to_change]):
            to_change = right_pos

        if to_change == start:
            break

        temp = myHeap[start]
        myHeap[start] = myHeap[to_change]
        myHeap[to_change] = temp

        start = to_change

    return header


for i in initList:
    insertToHeap(heap, i)

print heap

print extractFromHeap(heap)
print extractFromHeap(heap)
print extractFromHeap(heap)
print heap
