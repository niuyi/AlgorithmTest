import random

init_list = range(1, 10)

print init_list
random.shuffle(init_list)

print init_list


def insert_sort(myList):
    size = len(myList)
    for i in range(1, size):
        current = myList[i]

        for j in range(0, i):
            if current < myList[j]:
                # myList.remove(current)
                del myList[i]
                myList.insert(j, current)
                break


# insert_sort(init_list)
# print init_list


def findMiddle(myList, start, end):
    # subList = list(myList[start:end])
    #
    # random.shuffle(subList)
    # a = subList[0]
    #
    # random.shuffle(subList)
    # b = subList[0]
    #
    # random.shuffle(subList)
    # c = subList[0]

    a = myList[start]
    b = myList[end]
    c = myList[(end - start) / 2]

    new_list = [a, b, c]
    new_list.sort()
    middle_value = new_list[1]
    # middle_value = 28

    while True:
        while myList[end] > middle_value:
            end -= 1

        while myList[start] < middle_value:
            start += 1

        print start, end
        if start >= end:
            break
        else:
            temp = myList[start]
            myList[start] = myList[end]
            myList[end] = temp

    return end

# init_list = [24, 52, 11, 94, 28, 36, 14, 80]
middle_value = findMiddle(init_list, 0, len(init_list) - 1)


def quick_sort(myList, start, end):
    while start < end:
        middle_value = findMiddle(myList, start, end)
        quick_sort(myList, start, middle_value)

        start = middle_value + 1

quick_sort(init_list, 0, len(init_list) - 1)
print "init_list", init_list
