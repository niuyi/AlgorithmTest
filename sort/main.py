import random
init_list = range(1, 5)

print init_list
random.shuffle(init_list)

print init_list


def insert_sort(myList):
    size = len(myList)
    for i in range(1, size):
        current = myList[i]
        print "cur",current

        for j in range(0, i):
            if current < myList[j]:
                print "do insert", j, current
                myList.insert(j, current)
                print myList

    # print myList


insert_sort(init_list)

# print init_list

