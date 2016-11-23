#coding:utf-8
print "排序和顺序统计量"

#堆排序，一棵二叉树，定点是最小值。对于节点i，他的父节点是i/2，左子树是2i，右子树是2i+1，i从0开始

def modify_heap(list, i):
    size = len(list)
    left = 2*i + 1
    right = 2*i + 2

    largest = i
    if left <= size - 1 and list[left] > list[largest]:
        largest = left

    if right <= size - 1 and list[right] > list[largest]:
        largest = right

    if largest != i:
        temp = list[i]
        list[i] = list[largest]
        list[largest] = temp
        modify_heap(list, largest)


# init_list = [4, 1, 10, 14, 16, 9, 3, 2, 8, 7]
# print init_list
# #
# modify_heap(init_list, 1)
# #
# print init_list
# print "16, 14, 10, 8, 7, 9, 3, 2, 4, 1"

def build_heap(list):
    size = len(list)
    for i in xrange(size/2 - 1, -1, -1):
        modify_heap(list, i)


def sort_heap(list):
    build_heap(list)
    size = len(list)
    result = []

    for i in xrange(0, size):
        size = len(list)
        result.append(list[0])

        if size == 1:
            break

        list[0] = list[size - 1]
        del list[size - 1]

        modify_heap(list, 0)
        print "loop", i

    print result

init_list = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
sort_heap(init_list)
# print init_list
# build_heap(init_list)
# print init_list